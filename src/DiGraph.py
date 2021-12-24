from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.Nodes= {}
        self.Edges= {}
        self.mc = 0

    # def __init__(self, _Nodes, _Edges):
    #     self.Nodes=_Nodes
    #     self.Edegs=_Edges
    #     self.mc=0

    def v_size(self) -> int:
        return self.Nodes.__len__()

    def e_size(self) -> int:
        sum=0
        for key, v in self.Edges.items():
            sum = sum + len(v)
        return sum

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
         if id1 in self.Nodes.keys() and id2 in self.Nodes.keys():
            self.Edges[id1][id2]=weight
            self.mc = self.mc + 1
            return True
         else: return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
            self.Nodes[node_id]=Node(node_id,pos)
            self.Edges[node_id]={}
            self.mc=self.mc+1

    def remove_node(self, node_id: int) -> bool:
        if self.Nodes[node_id]!=None:
            self.Nodes.pop(node_id)
            self.mc = self.mc + 1
            return True
        else: return False


    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self.Nodes.keys() and node_id2 in self.Nodes.keys():
            self.Edges[node_id1][node_id2]=None
            self.mc = self.mc + 1
            return True
        else: return False

    def __str__(self):
        return f"Nodes:{self.Nodes}\nEdges:{self.Edges}"