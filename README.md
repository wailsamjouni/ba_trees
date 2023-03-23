# Trees based on edge disjoint paths
# Overview
* This repository contains the implementation of the TREE algorithms as outlined in https://arxiv.org/abs/2111.14123
1. The algorithms are divided as follows:
* Edge disjoint paths
* One Tree algorithm (The logest edge disjoint path from source and destination extended to Tree)
* Multiple Trees algorithm (All edge disjoint paths from source and destination extended to Multiple Trees)
* Routing algorithm (Can be found in this paper https://arxiv.org/abs/2111.14123)
# Classes
#### GraphStructure :
* This class contains all the algorithms (One Tree, Multiple Trees, Truncation, Routing)
#### Build :
* This class contains the setup to build the project
#### Graph :
* This class to create some random graphs to test
#### Overload :
* This class contains methods to get the computed paths and perform also the routing (compute the paths, the load,  generate failed edges...)
# Compiling
### 1. Clone repository from Github :
git clone https://github.com/wailsamjouni/ba_trees.git
### 2. Execute the code :
* Open a Python file
* Create an object of the class Overload
* Call the method compute_paths with the desired parameter by setting the paramerter "version" with one of the algorithms (edps, onetree, multitree)
