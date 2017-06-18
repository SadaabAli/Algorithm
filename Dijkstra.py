import sys
from heap import Heap

# The required inputs i.e filename , source and destination can be given by
# command line arguments.
# The following command can be used from the terminal to read file Graph.txt
# and given the shorted path form node 0 and 3:
# python Djikstra.py Graph.txt 0 3

# Given: name of the file where graph is stored, source and destination
# Example: run("Graph.txt", "0", "4") will run the dijktra's algorithm.
def run(filename, src, dest):
  graph = generate_graph(filename)
  dijkstra(graph, src, dest)

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
    source = line[0]
    destination = line[1]
    weight = int(line[2])

    if source not in graph:
      graph[source] = [(destination, weight)]
    else:
      graph[source].append([destination, weight])
    if destination not in graph:
      graph[destination] = []
  return graph

# Given: the dictionary with parents stored , source, and the destination.
# Example:
#  parent: {'1': '0', '3': '2', '2': '1', '5': '6', '4': '5', '7': '0', '6': '7', '8': '7'}
#  printPath(parent, "0", "4") =>
#  The shortest path from 0 to 4 is:
#  0 7 6 5 4
def printPath(parent, src, dest):
  output = []
  print "The shortest path from " + src + " to " + dest + " is:"
  while src != dest:
    output.append(dest)
    dest = parent[dest]
  output.append(src)
  for i in range(len(output),0,-1):
    print output[i-1],

# Given: graph for which we have to find shotest path from source to
#  destination.
# Example: dijkstra(graph, "0", "4") => shortest path from 0 to 4 is prined
#  in the given graph.
def dijkstra(graph, src, dest):
  vertices = graph.keys()
  Q = Heap(len(vertices))
  parent = {}

  for vertex in vertices:
    if vertex == src:
      Q.insert((vertex, 0))
    else:
      Q.insert((vertex,float('inf')))

  while not Q.isEmpty():
    u, wt_u = Q.pop()
    if u == dest:
      printPath(parent, src, dest)
      break
    else:
      lst = graph[u]
      for tup_v in lst:
        v, wt_v = tup_v
        if v not in Q.minHeap_pos:
          continue
        ind_v = Q.minHeap_pos[v]
        current_wt = Q.minHeap[ind_v][1]
        if wt_u + wt_v < current_wt:
          new_wt = wt_u + wt_v
          parent[v] = u
          Q.decreaseKey(ind_v, v, new_wt)

run(sys.argv[1], sys.argv[2], sys.argv[3])