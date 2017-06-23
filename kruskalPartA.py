import sys
from heap import Heap

class KruskalMST:

    def __init__(self, inNoOfVertices, iNoOfEdges):
        self.noOfVertices = inNoOfVertices
        self.tree = Heap(iNoOfEdges)

    def makeTree(self, inEdges):
        for edge in inEdges:
            edge = edge.split()
            src = int(edge[0])
            dest = int(edge[1])
            weight = int(edge[2])
            self.tree.insert(((src, dest), weight))

    def union(self, inNameArray, inName1, inName2):
        for name in range(len(inNameArray)):
            if inNameArray[name] == inName1:
                inNameArray[name] = inName2

    def GetMST(self):
        mst = {}
        nameArray = [None] * self.noOfVertices

        for node in range(self.noOfVertices):
            nameArray[node] = node

        while len(mst.keys()) < self.noOfVertices - 1:
            edge, weight = self.tree.pop()
            node1 = edge[0]
            node2 = edge[1]

            nameOfTree1 = nameArray[node1]
            nameOfTree2 = nameArray[node2]

            if nameOfTree1 != nameOfTree2:
                mst[edge] = weight
                self.union(nameArray, nameOfTree1, nameOfTree2)

        return mst

f = open(sys.argv[1], "r")
lines = f.readlines()
lines = [x.strip() for x in lines]
ver = lines.pop(0)[0]
graph = KruskalMST(int(ver),len(lines))

graph.makeTree(lines)
mst = graph.GetMST()

print mst