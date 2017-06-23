class NameArray:

    def __init__(self, inNoOfVertices):
        self.noOfVertices = inNoOfVertices
        self.nameArray = [None] * inNoOfVertices

    def makeSet(self):
        for i in range(self.noOfVertices):
            self.nameArray[i] = i

    def find(self,inName):
        return self.nameArray[inName]

    def union(self, inName1, inName2):
        for name in range(self.noOfVertices):
            if self.nameArray[name] == inName1:
                self.nameArray[name] = inName2

class ParentArray:

    def __init__(self, inNoOfVertices):
        self.noOfVertices = inNoOfVertices
        self.parentArray = [None] * inNoOfVertices

    def makeSet(self):
        for i in range(self.noOfVertices):
            self.parentArray[i] = i

    def find(self, inNode):
        if self.parentArray[inNode] == inNode:
            return inNode
        return self.find(self.parentArray[inNode])

    def union(self, inNode1, inNode2):
        parentOfNode1 = self.find(inNode1)
        parentOfNode2 = self.find(inNode2)

        self.parentArray[parentOfNode1] = parentOfNode2

class ParentArrayMerge:

    def __init__(self, inNoOfVertices):
        self.noOfVertices = inNoOfVertices
        self.parentArray = [None] * inNoOfVertices
        self.rankArray = [None] * inNoOfVertices

    def makeSet(self):
        for i in range(self.noOfVertices):
            self.parentArray[i] = i
            self.rankArray[i] = 0

    def find(self, inNode):
        if self.parentArray[inNode] == inNode:
            return inNode
        return self.find(self.parentArray[inNode])

    def union(self,inNode1, inNode2):
        parentOfNode1 = self.find(inNode1)
        parentOfNode2 = self.find(inNode2)

        if self.rankArray[parentOfNode1] > self.rankArray[parentOfNode2]:
            self.parentArray[parentOfNode2] = parentOfNode1
        elif self.rankArray[parentOfNode2] > self.rankArray[parentOfNode1]:
            self.parentArray[parentOfNode1] = parentOfNode2
        else:
            self.parentArray[parentOfNode1] = parentOfNode2
            self.rankArray[parentOfNode2] += 1

class PathCompression:
    def __init__(self, inNoOfVertices):
        self.noOfVertices = inNoOfVertices
        self.parentArray = [None] * inNoOfVertices
        self.rankArray = [None] * inNoOfVertices

    def makeSet(self):
        for i in range(self.noOfVertices):
            self.parentArray[i] = i
            self.rankArray[i] = 0

    def find(self, inNode):
        if self.parentArray[inNode] == inNode:
            return inNode
        self.parentArray[inNode] = self.find(self.parentArray[inNode])
        return self.parentArray[inNode]

    def union(self, inNode1, inNode2):
        parentOfNode1 = self.find( inNode1)
        parentOfNode2 = self.find( inNode2)

        if self.rankArray[parentOfNode1] > self.rankArray[parentOfNode2]:
            self.parentArray[parentOfNode2] = parentOfNode1
        elif self.rankArray[parentOfNode2] > self.rankArray[parentOfNode1]:
            self.parentArray[parentOfNode1] = parentOfNode2
        else:
            self.parentArray[parentOfNode1] = parentOfNode2
            self.rankArray[parentOfNode2] += 1