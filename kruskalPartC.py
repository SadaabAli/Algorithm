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

    def findParent(self, inParent, inNode):
        if inParent[inNode] == inNode:
            return inNode
        return self.findParent(inParent, inParent[inNode])

    def union(self, inParent, inRank, inNode1, inNode2):
        parentOfNode1 = self.findParent(inParent, inNode1)
        parentOfNode2 = self.findParent(inParent, inNode2)

        if inRank[parentOfNode1] > inRank[parentOfNode2]:
            inParent[parentOfNode2] = parentOfNode1
        elif inRank[parentOfNode2] > inRank[parentOfNode1]:
            inParent[parentOfNode1] = parentOfNode2
        else:
            inParent[parentOfNode1] = parentOfNode2
            inRank[parentOfNode2] += 1

    def GetMST(self):
        mst = {}
        parent = {}
        rank = {}

        for node in range(self.noOfVertices):
            parent[node] = node
            rank[node] = 0

        while len(mst.keys()) < self.noOfVertices - 1:
            edge, weight = self.tree.pop()
            node1 = edge[0]
            node2 = edge[1]

            parentOfNode1 = self.findParent(parent, node1)
            parentOfNode2 = self.findParent(parent, node2)

            if parentOfNode1 != parentOfNode2:
                mst[edge] = weight
                self.union(parent, rank, node1, node2)

        return mst

f = open(sys.argv[1], "r")
lines = f.readlines()
lines = [x.strip() for x in lines]
ver = lines.pop(0)[0]
graph = KruskalMST(int(ver),len(lines))

graph.makeTree(lines)
mst = graph.GetMST()

print mst