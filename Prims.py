import sys
from heap import Heap

# The required inputs i.e filename can be given by command line arguments.
# The following command can be used from the terminal to read file Graph.txt

# python Prims.py Graph.txt

# Given: name of the file where graph is stored
# Example: run("Graph.txt") will run the prim's algorithm.
def run(filename):
  graph = generate_graph(filename)
  prims(graph)

# Given: name of the file where graph is stored
# Returns: the graph as a dictionary with key as a source vertex and value as a
#  list of tuples of destination vertex and its respective weights. This graph
#  stores the source vertex and all the adjascent vertices from the source
#  vertex.
# Example: suppose the file has graph like:
#  3
#  1  2  4
#  2  3  1
#  1  3  3
# Then the graph dictionary will store the value as:
# {'1': [('2', 4), ('3', 3)], '2': [('3', 1)], '3': []}
def generate_graph(filename):
  f = open(filename, "r")
  lines = f.readlines()
  lines = [x.strip() for x in lines]
  lines.pop(0)
  graph = {}
  for line in lines:
    line = line.split()
    point1 = line[0]
    point2 = line[1]
    weight = int(line[2])

    if point1 not in graph:
      graph[point1] = [(point2, weight)]
    else:
      graph[point1].append([point2, weight])

    if point2 not in graph:
      graph[point2] = [(point1, weight)]
    else:
      graph[point2].append([point1, weight])
  return graph

# Given: the result in the dictionary
# Example: result in dictionary 'output':
#  [['0', '1'], ['3', '0'], ['2', '3']]
#  printPath(output) =>
#  The edges in the minimum spanning tree are:
#  0-1
#  3-0
#  2-3
def printPath(output):
  print "The edges in the minimum spanning tree are:"
  for i in range(0, len(output)):
    print output[i][0] + "-" + output[i][1]

# Given: graph for which we have to find Minimum Spanning Tree.
# Example: prims(graph) => edges of Minimum Spanning Tree are printed for the
#   given graph.
def prims(graph):
  vertices = graph.keys()
  Q = Heap(len(vertices))
  parent = {}
  src = vertices[0]
  output = []

  for vertex in vertices:
    if vertex == src:
      Q.insert((vertex, 0))
    else:
      Q.insert((vertex,float('inf')))
    parent[vertex] = None

  while not Q.isEmpty():
    u, weight = Q.pop()
    if parent[u] != None:
      output.append([u, parent[u]])
    edges = graph[u]
    for edge in edges:
      v, wt_v = edge
      if v not in Q.minHeap_pos:
        continue
      ind_v = Q.minHeap_pos[v]
      if wt_v < Q.minHeap[ind_v][1]:
        parent[v] = u
        Q.decreaseKey(ind_v, v, wt_v)
  printPath(output)

run(sys.argv[1])