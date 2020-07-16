class Node:
    __slots__ = ("key", "parent", "left", "right")
    def __init__(self, key, parent, left, right):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


n = int(input().rstrip())
keys = list(input().rstrip().split())
heap = [None]

for i in range(1, n + 1):
    parent = i // 2
    left = i * 2
    right = i * 2 + 1
    heap.append(Node(keys[i-1], parent, left, right))
    
for i in range(1, n + 1):
    result = "node " + str(i) + ": key = " + str(heap[i].key) + ", "
    if heap[heap[i].parent] != None:
        result += "parent key = " + str(heap[heap[i].parent].key) + ", "
        
    if heap[i].left < len(heap):
        result += "left key = " + str(heap[heap[i].left].key) + ", "
    
    if heap[i].right < len(heap):
        result += "right key = " + str(heap[heap[i].right].key) + ", "
    
    print(result)
    
    
    
