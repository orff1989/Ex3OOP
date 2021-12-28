![image](https://user-images.githubusercontent.com/93159965/147562147-754a2b7c-d5d0-44c8-b6d9-a37ce5fc1b44.png)

# Assignment 3

> Made by Or Finberg and Eitan Wechsler
>
> GitHub pages:  
> [https://github.com/orff1989](https://github.com/orff1989)
> 
> [https://github.com/EitanWex](https://github.com/EitanWex)


# Graph Drawer - python
In this project, we were tasked to recreate our work from the previous assignment (written in Java) to Python.

As you'll see, in this project, you can load graphs from json files, edit the graph and run some algorithms on the graph.

![Screenshot 2021-12-27 233547](https://user-images.githubusercontent.com/43110158/147508794-28eb6cbd-c2db-4b65-89f7-97b7fc79d2c7.png)

Graph with 1,000 Nodes:

![Screenshot 2021-12-27 223355](https://user-images.githubusercontent.com/43110158/147508451-0958ec2e-b77b-4b56-80c3-56ba358ba13f.png)


# Analysis of the performance of the algorithms:

![Screenshot 2021-12-27 232312](https://user-images.githubusercontent.com/43110158/147508128-080c7d0a-e1d4-40e3-af4f-0393b710bbd4.png)

PC specifications: CPU: Intel(R) Core(TM) i7-10510U CPU @ 1.80GHz 2.30 GHz, Ram:16GB, Operating System: Windows 11 64bit.

# UML Diagram

This is a uml of the project:

![Class Diagram](ClassesDiagram.png)

### GUI:
Running the plot_graph() in the GraphAlgo class.

### Download and Run
To get this project you need to clone it into a Pycharm project.

Next, to run it, you need to go to main.py file.

## DiGraph class - implements GraphInterface

This class implement GraphInterface abstract class that represents an interface of a graph.

Each DiGraph contain dictionary of his nodes, and each node contain his edges.\
In addition each DiGraph holds the number of edges in the graph and a mode counter (mc)\
that represent the number of changes (add node, add edge, remove node or remove edge) in the graph.


| **Main methods**      |    **Details**        |
|-----------------|-----------------------|
| `v_size()` | Returns the number of vertices in this graph |
| `e_size()` | Returns the number of edges in this graph |
| `get_mc()` | Returns the current version of this graph |
| `add_edge()` | Adds an edge to the graph |
| `add_node()` | Adds a node to the graph |
| `remove_node()` | Removes a node from the graph |
| `remove_edge()` | Removes an edge from the graph |



## GraphAlgo class - implenents GraphAlgoInterface
This class implement GraphAlgoInterface abstract class that represents an interface of a graph.\
Each GraphAlgo contain a DiGraph on which the algorithm works on.


| **Main methods**      |    **Details**        |
|-----------------|-----------------------|
| `get_graph()` | Rutern the directed graph on which the algorithm works on |
| `load_from_json()` | Loads a graph from a json file |
| `save_to_json()` | Saves the graph in JSON format to a file |
| `shortest_path()` | Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm |
| `TSP()` | Finds the shortest path that visits all the nodes in the list |
| `centerPoint()` |   Finds the node that has the shortest distance to it's farthest node |
| `dijkDist()` |  returns all the shortest path from the given source and its distance |
| `theLightNextNodeNotVisited()` | returns the closest and lightest node from a given node |
| ` theLightNextNode()` | returns lightest node from a given node |
| `sumOfW()` | returns the weight of the givien list |
| `eccentricity()` |  returns list of the largest pathh |
| `plot_graph()` | Plots the graph |

### Algorithm used:
* dijkstra(self, src, dest) -> (float, list) :
This method based on Dijkstra's algorithm.
Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph.
In other words it finds the shortest paths between the source node and the destination node.
The method stored a distance dictionary represent each node weight, in the beginning initialized to infinity.
In each step the method update his current distance from the source node.
In addition it stored a dictionary represent each node "father", meaning the node through which we discovered this node.
Update the source node weight to be 0 and push him into a queue.
Pop the node with the minimum weight from the queue.
Visit each one of this nodes neighbors:
Check if his current weight is more then the distance between the node and the source node, if so, update his weight and updates his "father" to be the node's id from which he came to.
After going through all the neighbors of the node, If the current node that pop out from the queue is the destination node we finish.
Otherwise repeat these steps until the queue is empty.
If the dest node weight is infinity it means there is no path between src node and dest node, return infinity and empty list.
Otherwise returns the weight of the dest node that represent the distance between the two nodes, return the path between them and the distance.
Complexity: O((|V|+|E|)log|V|), |V|=number of nodes, |E|=number of edges.
## External info:
- More about graph : https://en.wikipedia.org/wiki/Directed_graph
- More about matplotlib : https://matplotlib.org   
