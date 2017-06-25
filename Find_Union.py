class NameArray:

    # constructor template for NameArray:
    # nameArray = NameArray(5)
    # Interpretation:
    # inNoOfVertices represents the size of the nameArray
    def __init__(self, inNoOfVertices):
        self.noOfVertices = inNoOfVertices
        self.nameArray = [None] * inNoOfVertices

    # Assigns name label to every vertex(element) in the nameArray
    # Name of every vertex is itself at the start
    def makeSet(self):
        for i in range(self.noOfVertices):
            self.nameArray[i] = i

    # Input : a vertex
    # Output :  the name label associated with the input vertex in the nameArray
    def find(self,inName):
        return self.nameArray[inName]

    # Input : two names inName1 and inName2
    # Output : Changes names of vertex with inName1 to inName2
    def union(self, inName1, inName2):
        for name in range(self.noOfVertices):
            if self.nameArray[name] == inName1:
                self.nameArray[name] = inName2

class ParentArray:

    # constructor template for ParentArray:
    # parentArray = ParentArray(5)
    # Interpretation:
    # inNoOfVertices represents the size of the parentArray
    def __init__(self, inNoOfVertices):
        self.noOfVertices = inNoOfVertices
        self.parentArray = [None] * inNoOfVertices

    # Assigns parent to every vertex(element) in the parentArray
    # Parent of every vertex is itself at the start
    def makeSet(self):
        for i in range(self.noOfVertices):
            self.parentArray[i] = i

    # Input : a vertex
    # Output :  the parent associated with the input vertex in the parentArray
    def find(self, inNode):
        while (inNode != self.parentArray[inNode]):
            inNode = self.parentArray[inNode]
        return inNode

    # Input : two nodes inNode1 and inNode2
    # Output : parentArray with parent of node1 changes to parent of node 2
    def union(self, inNode1, inNode2):
        # parentOfNode1 = self.find(inNode1)
        # parentOfNode2 = self.find(inNode2)

        self.parentArray[inNode1] = inNode2

class ParentArrayMerge:

    # constructor template for ParentArrayMerge:
    # parentArrayMerge = ParentArrayMerge(5)
    # Interpretation:
    # inNoOfVertices represents the size of the parentArray
    def __init__(self, inNoOfVertices):
        self.noOfVertices = inNoOfVertices
        self.parentArray = [None] * inNoOfVertices
        self.rankArray = [None] * inNoOfVertices

    # Assigns parent and rank to every vertex(element) in the parentArray and rankArray
    # Parent of every vertex is itself at the start and rank is zero
    def makeSet(self):
        for i in range(self.noOfVertices):
            self.parentArray[i] = i
            self.rankArray[i] = 0

    # Input : a vertex
    # Output :  the parent associated with the input vertex in the parentArray
    def find(self, inNode):
        while (inNode != self.parentArray[inNode]):
            inNode = self.parentArray[inNode]
        return inNode

    # Input : two nodes inNode1 and inNode2
    # Output : parentArray with parent of either node1 and node2 modified based on the rank of
    # parents
    def union(self,inNode1, inNode2):
        if self.rankArray[inNode1] > self.rankArray[inNode2]:
            self.parentArray[inNode2] = inNode1
        elif self.rankArray[inNode2] > self.rankArray[inNode1]:
            self.parentArray[inNode1] = inNode2
        else:
            self.parentArray[inNode1] = inNode2
            self.rankArray[inNode2] += 1

# constructor template for PathCompression:
# pathCompression = PathCompression(5)
# Interpretation:
# inNoOfVertices represents the size of the parentArray
class PathCompression:
    def __init__(self, inNoOfVertices):
        self.noOfVertices = inNoOfVertices
        self.parentArray = [None] * inNoOfVertices
        self.rankArray = [None] * inNoOfVertices

    # Assigns parent and rank to every vertex(element) in the parentArray and rankArray
    # Parent of every vertex is itself at the start and rank is zero
    def makeSet(self):
        for i in range(self.noOfVertices):
            self.parentArray[i] = i
            self.rankArray[i] = 0

    # Input : a vertex
    # Output :  the parent associated with the input vertex in the parentArray
    # If the parent of a node is not itself, we perform path compression by pointing the
    # element to its grandparent.
    def find(self, inNode):
        while (inNode != self.parentArray[inNode]):
            self.parentArray[inNode] = self.parentArray[self.parentArray[inNode]]
            inNode = self.parentArray[inNode]
        return inNode

    # Input : two nodes inNode1 and inNode2
    # Output : parentArray with parent of either node1 and node2 modified based on the rank of
    # parent
    def union(self, inNode1, inNode2):
        if self.rankArray[inNode1] > self.rankArray[inNode2]:
            self.parentArray[inNode2] = inNode1
        elif self.rankArray[inNode2] > self.rankArray[inNode1]:
            self.parentArray[inNode1] = inNode2
        else:
            self.parentArray[inNode1] = inNode2
            self.rankArray[inNode2] += 1