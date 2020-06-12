# # coding: utf-8
# # Your code here!

n = int(input().rstrip())
nodes = {}
root = -1

class Node:
    def __init__(self, id, degree, children):
        self.id = id
        self.degree = degree
        self.children = children
        self.parent = -1
        self.depth = 0
        self.type = "root"
    def setParent(self, id):
        self.parent = id
    def setType(self, type):
        self.type = type
    def setDepth(self, depth):
        self.depth = depth
    def toString(self):
        print("node " + str(self.id) + ": parent = " + str(self.parent) + ", depth = " + str(self.depth) + ", " + str(self.type) + ", " + str(self.children))

for i in range(n):
    a = list(map(int, input().rstrip().split()))
    nodes[a[0]] = (Node(a[0],a[1],a[2:]))
    
for i in range(n):
    node = nodes[i]
    children = node.children
        
    for j in range(len(children)):
        nodes[children[j]].setParent(node.id)
        
def dfs(index, depth):
    nodes[index].setDepth(depth)
    for i in range(len(nodes[index].children)):
        dfs(nodes[index].children[i], depth + 1)
        
r = -1
for i in range(n):
    if nodes[i].parent == -1:
        r = i
        break;
dfs(r, 0)
    
for i in range(len(nodes)):
    node = nodes[i]
    if node.parent == -1:
        node.setType('root')
    elif not node.children:
        node.setType('leaf')
    else:
        node.setType('internal node')
        
for i in range(n):
    nodes[i].toString()
