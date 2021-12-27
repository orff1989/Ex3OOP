from src import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.Node import Node
import json, random
import matplotlib.pyplot as plt
import numpy as np
import GraphAlgo
import functools
import operator

class GraphAlgo(GraphAlgoInterface):

    def __init__(self):
       self.graph=DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        dict = {}
        gr = DiGraph()
        with open(file_name, "r+") as f:
            dict = json.load(f);

        edges={}
        nodes={}

        for t in dict["Nodes"]:
            if len(t.keys())!=1:
                pos = tuple(map(float, t["pos"].split(',')))
            else:
                pos = (random.randint(0,50),random.randint(0,50),0)

            edges[t["id"]]={}
            nodes[t["id"]] = Node(t["id"], pos)
        for t in dict["Edges"]:
            edges[t["src"]][t["dest"]]=t["w"]

        self.graph.Edges=edges
        self.graph.Nodes=nodes
        self.graph.mc=0
        return True

    def save_to_json(self, file_name: str) -> bool:  # need to work on
        Edges = []
        tup = {}
        for src, v in self.graph.Edges.items():
            for dest, w in v.items():
                tup["src"] = src
                tup["w"] = w
                tup["dest"] = dest
                Edges.append(tup)
                tup = {}

        Nodes = []
        tup = {}
        for id, n in self.graph.Nodes.items():
            tup["id"] = id
            tup["pos"] = ','.join(map(str, n.pos))

            Nodes.append(tup)
            tup = {}

        gr = {}
        gr["Edges"] = Edges
        gr["Nodes"] = Nodes
        with open(file_name, "w") as f:
            jsonStringEdges = json.dumps(gr)
            f.write(jsonStringEdges)
            return True
        return False

    def dijkDist(self, src) -> (list, list):
        visi = []
        distance = []
        mySet = []
        thePath = []

        for i in range(0, self.graph.v_size()):
            visi.append(False)
            distance.append(float('inf'))
            thePath.append([])

        distance[src] = 0
        thisNode = src

        while (1 == 1):
            visi[thisNode] = True

            for o in self.graph.Edges[thisNode]:
                if visi[o] == True:
                    continue

                mySet.append(o)
                tempLenghth = distance[thisNode] + self.graph.Edges[thisNode][o]
                if tempLenghth < distance[o]:
                    distance[o] = tempLenghth
                    thePath[o] = []
                    thePath[o] = thePath[thisNode].copy()
                    thePath[o].append(self.graph.Nodes[thisNode])

            if mySet.__contains__(thisNode):
                mySet.remove(thisNode)

            if len(mySet) == 0:
                break

            minimumDistance = float('inf')
            j = 0
            for i in mySet:
                if minimumDistance > distance[i]:
                    minimumDistance = distance[i]
                    j = i

            thisNode = j
        return distance, thePath

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 == id2:
            return 0, None

        distance, thePath = self.dijkDist(id1)

        if distance[id2] == -1 or distance[id2] == float('inf'):
            return -1, None

        finalPath = []
        for p in thePath:
            if len(p) != 0 and finalPath.__contains__(p[0].id) == False:
                finalPath.append(p[0].id)

        finalPath.append(id2)
        return distance[id2], finalPath

    def allVisited(self, node_lst, visi):
        for n in node_lst:
            if visi[n] == False:
                return False
        return True

    def theLightNextNodeNotVisited(self, curr, visi: dict) -> int:
        if curr == -1: return -1
        index = -1
        if len(self.graph.Edges[curr].keys()) == 0:
            return -1
        minW = float('inf')

        for key, v in self.graph.Edges[curr].items():
            if v < minW:
                if visi.get(key) == None or visi.get(key) == False:
                    minW = v
                    index = key

        return index

    def theLightNextNode(self, nodeId):
        if nodeId == -1: return -1
        index = -1
        if len(self.graph.Edges[nodeId]) == 0:
            return -1

        minW = float('inf')

        for key, v in self.graph.Edges[nodeId].items():
            if v < minW:
                minW = v
                index = key

        return index

    def sumOfW(self, thePath: list) -> float:
        sum = 0
        prev = thePath[0]
        for i in thePath:
            if i == prev:
                continue
            sum = sum + self.graph.Edges[prev][i]
            prev = i
        return sum

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        visi = {}
        thePath = []

        for i in node_lst:
            visi[i] = False

        srcIndex = 0
        nextNode = -1
        curr = srcIndex

        while (self.allVisited(node_lst, visi) == False):
            if srcIndex > self.graph.v_size():
                return None
            nextNode = self.theLightNextNodeNotVisited(curr, visi)

            if nextNode == -1:
                nextNode = self.theLightNextNode(curr)

            if nextNode == -1:
                thePath = []
                for i in node_lst:
                    visi[i] = False
                srcIndex = srcIndex + 1
                curr = srcIndex

            thePath.append(curr)
            visi[curr] = True
            curr = nextNode
        sumOfWw = self.sumOfW(thePath)
        return thePath, sumOfWw

    def eccentricity(self):
        ecc = []
        for k in range(self.graph.v_size()):
            ecc.append(float('-inf'))

        for i in self.graph.Nodes.keys():
            for j in self.graph.Nodes.keys():
                if i != j:
                    dist, thePath = self.shortest_path(i, j)
                    if dist > ecc[i] and dist != -1:
                        ecc[i] = dist
        return ecc

    def centerPoint(self) -> (int, float):
        dist1 = self.eccentricity()
        dist = {}
        for j in range(len(dist1)):
            if dist1[j] != float('-inf'):
                dist[j] = dist1[j]
        min = float('inf')

        index = 0
        for i in dist.keys():
            if dist[i] < min:
                min = dist[i]
                index = i

        return index, min

    def plot_graph(self) -> None:
        for src in self.graph.Nodes.values():
            x, y, z =src.pos
            plt.plot(x,y,markersize=10, marker="o", color="red")
            plt.text(x, y,  str(src.id), color="blue", fontsize=12)

            for dest in self.graph.Edges[src.id]:
                n_x, n_y , n_z= self.graph.Nodes[dest].pos
                plt.annotate("",xy=(x,y),xytext=(n_x,n_y),arrowprops=dict(arrowstyle="<-"))
        plt.show()