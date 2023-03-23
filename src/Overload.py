from GraphStructure import GraphStructure
from Build import Build
from typing import List
import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter
import copy
import time
import timeit
import pandas as pd
import random


class Overload:
    def __init__(self):
        pass

    def path_to_edges(self, path):
        edges = []
        for i in range(len(path)-1):
            edge = (path[i], path[i+1])
            edges.append(edge)
        return edges

    def get_just_paths(self, paths):
        result = [path[2] for path in paths if path[1] is True]

        return result

    def resign_graph(self):

        g_copy = copy.deepcopy(self.graph)
        for structure in self.results:
            structure.graph.graph = g_copy
            
    def sources_destination_random(self, graph):
        
        dest_nodes = random.sample(list(graph.nodes()), 1)
        destination = dest_nodes[0]
        random_nodes = random.sample(list(graph.nodes()), 6)

        if destination in random_nodes:
            random_nodes.remove(destination)
            
        return random_nodes, destination
    
    def generate_random_failed_edges(self, graph, fraction):

        number_of_failed_edges = int(fraction * graph.number_of_edges())
        failed_edges = random.sample(graph.edges(), number_of_failed_edges)
        
        return failed_edges

    def compute_paths(self, erdos,sources, destination,failed_edges, version):

        paths = []
        for node in sources:

            g_copy = copy.deepcopy(erdos)
            graph_structure = GraphStructure(
                g_copy, node, destination)
            graph = Build(graph_structure)

            path = graph.build(failed_edges, version)
            paths.append(path)

        return paths
    
    def compute_path_for_one_source(self, erdos,source, destination,failed_edges, version):


        g_copy = copy.deepcopy(erdos)
        graph_structure = GraphStructure(
                g_copy, source, destination)
        graph = Build(graph_structure)

        path = graph.build(failed_edges, version)

        return path

    def load_versions(self, paths):

        if paths is not None and len(paths) > 0:
            all_edges = [frozenset(edge) for path in paths for edge in path]

            counter = Counter(all_edges)
            most_common = [tuple(edge) for edge, count in counter.most_common(
            ) if count == counter.most_common(1)[0][1]]

            edge_load = counter.most_common(1)[0][1]

            return most_common, edge_load

    def load_all_versions(self, paths):

        results = []
        i = 0

        for path_list in paths:
            result = self.load_versions(path_list)
            results.append(result)
            print(f'Result number {i+1} : {result}')
            i += 1

        return results


    def model(self, sizes, fraction):

        edp_times = []
        one_times = []
        multi_times = []

        for number_nodes in sizes:
            random_graph = nx.gnp_random_graph(number_nodes, 0.3)
                
            edp_times.append(timeit.timeit(
                lambda: self.compute_paths(random_graph, fraction, version="edps"), number=1) * 1000)

            one_times.append(timeit.timeit(
                lambda: self.compute_paths(random_graph, fraction, version="onetree"), number=1) * 1000)

            multi_times.append(timeit.timeit(
                lambda: self.compute_paths(random_graph, fraction, version="multitree"), number=1) * 1000)

        df = pd.DataFrame({
            "Sizes": sizes,
            # "Number of Edges": number_of_edges,
            "Edps": edp_times,
            "One Tree": one_times,
            "Multiple Trees": multi_times
        })

        plt.plot(df['Sizes'], df['Edps'], label='Edps')
        plt.plot(df['Sizes'], df['One Tree'], label='One Tree')
        plt.plot(df['Sizes'], df['Multiple Trees'], label='Multiple Trees')
        
        # plt.plot(df['Number of Edges'], df['Edps'], label='Edps')
        # plt.plot(df['Number of Edges'], df['One Tree'], label='One Tree')
        # plt.plot(df['Number of Edges'], df['Multiple Trees'], label='Multiple Trees')

        plt.xlabel('Number of nodes')
        plt.ylabel('Complexity in ms')
        plt.legend()

        plt.show()
        plt.savefig('Runtime5rounds.svg')


    def avg_length_success_rate(self, paths):
    
        total_count = 0
        succ_count = 0
        path_length = 0
    
        for path in paths:
        
            if path[1] is True:
                succ_count += 1
                if path[2] is not None:
                    if len(path[2]) > 0:
                        path_length += len(path[2])
            total_count +=1
        
        avg_path_length = path_length / succ_count if succ_count > 0 else 0
        success_rate = succ_count / total_count * 100
    
        return success_rate, avg_path_length


