class NameArray:

    # constructor template for NameArray:
    # nameArray = NameArray(5)
    # Interpretation:
    # We initialize an dictionary nameArray where vertex is the key and value is the name label
    def __init__(self):
        self.nameArray = {}

    # Assigns name label to every vertex(element) in the nameArray
    # Name of every vertex is itself at the start
    def makeSet(self,inEdges):
        for edge in inEdges:
            edge = edge.split()
            src = edge[0]
            dest = edge[1]
            if src not in self.nameArray:
                self.nameArray[src] = src
            if dest not in self.nameArray:
                self.nameArray[dest] = dest

    # Input : a vertex
    # Output :  the name label associated with the input vertex in the nameArray
    def find(self,inName):
        return self.nameArray[inName]

    # Input : two names inName1 and inName2
    # Output : Changes names of vertex with inName1 to inName2
    def union(self, inName1, inName2):
        for vertex in self.nameArray:
            if self.nameArray[vertex] == inName1:
                self.nameArray[vertex] = inName2

class ParentArray:

    # constructor template for ParentArray:
    # parentArray = ParentArray(5)
    # Interpretation:
    # We initialize an dictionary nameArray where vertex is the key and value is the name label
    def __init__(self):
        self.parentArray = {}

    # Assigns parent to every vertex(element) in the parentArray
    # Parent of every vertex is itself at the start
    def makeSet(self,inEdges):
        for edge in inEdges:
            edge = edge.split()
            src = edge[0]
            dest = edge[1]
            if src not in self.parentArray:
                self.parentArray[src] = src
            if dest not in self.parentArray:
                self.parentArray[dest] = dest

    # Input : a vertex
    # Output :  the parent associated with the input vertex in the parentArray
    def find(self, inNode):
        while (inNode != self.parentArray[inNode]):
            inNode = self.parentArray[inNode]
        return inNode

    # Input : two nodes inNode1 and inNode2
    # Output : parentArray with parent of node1 changes to parent of node 2
    def union(self, inNode1, inNode2):
        self.parentArray[inNode1] = inNode2

class ParentArrayMerge:

    # constructor template for ParentArrayMerge:
    # parentArrayMerge = ParentArrayMerge(5)
    # Interpretation:
    # We initialize an dictionary nameArray where vertex is the key and value is the name label
    # and dictionary rankArray which has rank of every vertex
    def __init__(self):
        self.parentArray = {}
        self.rankArray = {}

    # Assigns parent and rank to every vertex(element) in the parentArray and rankArray
    # Parent of every vertex is itself at the start and rank is zero
    def makeSet(self,inEdges):
        for edge in inEdges:
            edge = edge.split()
            src = edge[0]
            dest = edge[1]
            if src not in self.parentArray:
                self.parentArray[src] = src
            if dest not in self.parentArray:
                self.parentArray[dest] = dest
            if src not in self.rankArray:
                self.rankArray[src] = 0
            if dest not in self.rankArray:
                self.rankArray[dest] = 0

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
# We initialize an dictionary nameArray where vertex is the key and value is the name label
# and dictionary rankArray which has rank of every vertex
class PathCompression:
    def __init__(self):
        self.parentArray = {}
        self.rankArray = {}

    # Assigns parent and rank to every vertex(element) in the parentArray and rankArray
    # Parent of every vertex is itself at the start and rank is zero
    def makeSet(self,inEdges):
        for edge in inEdges:
            edge = edge.split()
            src = edge[0]
            dest = edge[1]
            if src not in self.parentArray:
                self.parentArray[src] = src
            if dest not in self.parentArray:
                self.parentArray[dest] = dest
            if src not in self.rankArray:
                self.rankArray[src] = 0
            if dest not in self.rankArray:
                self.rankArray[dest] = 0

    # Input : a vertex
    # Output :  the parent associated with the input vertex in the parentArray
    # If the parent of a node is not itself, we perform path compression by pointing the
    # element to its grandparent.
    def find(self, inNode):
        while (inNode != self.parentArray[inNode]):
            self.parentArray[inNode] = self.find(self.parentArray[inNode])
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