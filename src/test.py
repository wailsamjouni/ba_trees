import networkx as nx
from Overload import Overload
import random



source = 2
destination = 99

graph = nx.erdos_renyi_graph(150, 0.7)


overload = Overload()
failed_edges = overload.generate_random_failed_edges(graph, 0.15)
# print(f'Failed edges are : {failed_edges}')
path = overload.compute_path_for_one_source(graph,source, destination,failed_edges, 'onetree')

print(path)
