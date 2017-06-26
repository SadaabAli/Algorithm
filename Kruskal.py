import sys
from Find_Union import NameArray, ParentArray, ParentArrayMerge, PathCompression
from heap import Heap

class Kruskal:

  # constructor template for Kruskal:
  # kruskal = Kruskal(5,10)
  # Interpretation:
  # inNoOfVertices represents the number of vertices in the tree
  # iNoOfEdges represents the number of edges in the tree which correspond to
  # the number of elements in the heap.
  def __init__(self, inNoOfVertices, iNoOfEdges):
    self.noOfVertices = inNoOfVertices
    self.tree = Heap(iNoOfEdges)

  # Input : the edges of the tree read from the file
  # Output : A min heap data stucture inside tree
  def makeTree(self, inEdges):
    for edge in inEdges:
      edge = edge.split()
      src = edge[0]
      dest = edge[1]
      weight = int(edge[2])
      self.tree.insert(((src, dest), weight))

  # Input : Mode used to find the Minimum spanning tree:
  #   If mode == a -> using name Array
  #   If mode == b -> using parent Array
  #   If mode == c -> using parent array and weighted merge
  #   If mode == d -> using parent array, weighted merge and path compression
  # Output : The edges of the minimum spanning tree.
  def GetMST(self,iNoOfEdges,inMode):
    mst = []
    if inMode == "a":
      parentInfo = NameArray()
    elif inMode == "b":
      parentInfo = ParentArray()
    elif inMode == "c":
      parentInfo = ParentArrayMerge()
    else:
      parentInfo = PathCompression()

    parentInfo.makeSet(iNoOfEdges)

    while len(mst) < self.noOfVertices - 1:
      edge, weight = self.tree.pop()
      node1 = edge[0]
      node2 = edge[1]

      nameOfTree1 = parentInfo.find(node1)
      nameOfTree2 = parentInfo.find(node2)

      if nameOfTree1 != nameOfTree2:
        mst.append(edge)
        parentInfo.union(nameOfTree1, nameOfTree2)

    return mst

# Input : Filename and mode used to form the MST
# Output : prints the edges of the minimum spanning tree
def run(inFileName, inMode):
  f = open(inFileName, "r")
  lines = f.readlines()
  lines = [x.strip() for x in lines]
  ver = lines.pop(0).strip()
  graph = Kruskal(int(ver), len(lines))
  graph.makeTree(lines)
  mst = graph.GetMST(lines,inMode)
  printPath(mst,inMode)

# Input : edges of the minimum spanning tree
# Output : prints the edges of the minimum spanning tree
def printPath(inOutput,inMode):
  print "The edges in the minimum spanning tree "
  if inMode == "a":
    print "using name array are:"
  elif inMode == "b":
    print "using parent array:"
  elif inMode == "c":
    print "using parent and weighted merge array:"
  else:
    print "using path compression are:"
  for i in range(0, len(inOutput)):
    edge = inOutput[i]
    print str(edge[0]) + "-" + str(edge[1])

# Input : Filename and mode used to form MST
# Output : Runs the Kruskal algorithm to form MST
run(sys.argv[1],sys.argv[2])