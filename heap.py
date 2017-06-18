class Heap:
  # constructor template for Heap:
  # h = Heap(size)
  # Interpretation:
  # size is the size of the heap
  def __init__(self, size):
    self.minHeap = [(None,None)] * (size+1)
    self.minHeap_pos = {}
    self.pos = 1

  # Given: position of element in the heap
  # Returns: position of element's parent in the heap
  # Example: h.parent(2) => 1
  def parent(self, pos):
    return pos / 2

  # Given: position of element in the heap
  # Returns: position of element's left child in the heap
  # Example: h.leftChild(2) => 4
  def leftChild(self, pos):
    return pos * 2

  # Given: position of element in the heap
  # Returns: position of element's right child in the heap
  # Example: h.rightChild(2) => 5
  def rightChild(self, pos):
    return pos * 2 + 1

  # Given: position of two elements that needs to be swapped in the heap
  # Example: h.swap(2,4) => element's at these positions will be swapped in the
  #  heap
  def swap(self, pos1, pos2):
    temp = self.minHeap[pos1]
    self.minHeap[pos1] = self.minHeap[pos2]
    self.minHeap[pos2] = temp

  # Given: position of two elements that needs to be swapped
  # Example: h.swapPos(2,4) => position of elements will be swapped in the
  # dictionary
  def swapPos(self, pos1, pos2):
    self.minHeap_pos[self.minHeap[pos1][0]] = pos1
    self.minHeap_pos[self.minHeap[pos2][0]] = pos2

  # Given: position of element in the heap from which it needs
  #  to be moved up in the tree until parent element is smaller than
  #  the current element.
  #  If position is not given then the element is moved up in the
  #  tree from the last inserted position.
  # Examples: If current position is 6 in the heap.
  #  h.bubbleUp() => element at position 6 will be moved up.
  #  h.bubbleUp(4) => element at position 4 will be moved up.
  def bubbleUp(self, pos=-1):
    if pos == -1:
      pos = self.pos - 1
    while pos > 0 and self.minHeap[self.parent(pos)][1] > self.minHeap[pos][1]:
      self.swap(pos, self.parent(pos))
      self.swapPos(pos, self.parent(pos))
      pos = self.parent(pos)

  # Given: position of element in the heap from which it needs
  #  to be moved down in the tree until it is greater than its child
  #  elements.
  # Example: h.sinkDown(1) => element at position 1 will be moved down.
  def sinkDown(self, parent):
    # least represents the index of smallest element among parent, left child
    # and right child
    least = parent
    # if left child is smaller than the parent
    if self.leftChild(parent) < self.pos and \
            self.minHeap[parent][1] > self.minHeap[self.leftChild(parent)][1]:
      least = self.leftChild(parent)
    # if right child is smaller than the parent or left child
    if self.rightChild(parent) < self.pos and \
            self.minHeap[least][1] > self.minHeap[self.rightChild(parent)][1]:
      least = self.rightChild(parent)
    if least != parent:
      self.swap(parent, least)
      self.swapPos(parent, least)
      self.sinkDown(least)

  # Given: element that needs to be inserted in the heap
  # Example: h.insert(('3',5)) => ('3',5) will be inserted at the leaf and then
  #  will be moved up with bubbleUp() operation.
  def insert(self, element):
    self.minHeap[self.pos] = element
    self.minHeap_pos[element[0]] = self.pos
    self.pos += 1
    self.bubbleUp()

  # Given: the key(vertex) and the value(weight) which needs to be updated in
  #  the tree and then move up in the tree with bubbleUp() operation.
  # Example: h.decreaseKey('3', 2) will update the tuple ('3', 5) with
  #  ('3', 2) and then it will be moved up in the tree.
  def decreaseKey(self, index, key, value):
      self.minHeap[index] = (key, value)
      self.bubbleUp(index)

  # Returns: the element at the root. (which is the elementwith smallest weight)
  # Example: h.pop() => tuple with lowest weight in the heap.
  def pop(self):
    # root element is popped out which is at index 1
    element = self.minHeap[1]
    pos = self.pos
    # replace the root element with the leaf
    leaf_elem = self.minHeap[pos-1]
    self.minHeap[1] = leaf_elem
    self.minHeap.pop()
    self.pos -= 1
    # change the position in dictionary
    vertex = leaf_elem[0]
    self.minHeap_pos[vertex] = 1
    self.minHeap_pos.pop(element[0])
    # perform sink down operation starting from root
    self.sinkDown(1)
    return element

  # Returns: true iff the heap is empty
  # Example: h.isEmpty() => returns true if heap is empty.
  def isEmpty(self):
    return self.pos == 1