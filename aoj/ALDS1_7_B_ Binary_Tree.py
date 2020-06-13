# # coding: utf-8
# # Your code here!

n = int(input().rstrip())
nodes = [None] * n
root = -1

class Node:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right
        self.parent = -1
        self.sibling = -1
        left = 0 if left == -1 else 1
        right = 0 if right == -1 else 1
        self.degree = left + right
        self.depth = 0
        self.height = 0
        
    @property
    def type(self):
        if self.parent == -1:
            return "root"
        elif self.left == -1 and self.right == -1:
            return "leaf"
        else:
            return "internal node"
        
    def toString(self):
        print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}'.format(self.id, self.parent, self.sibling , self.degree, self.depth, self.height, self.type))

# input
for i in range(n):
    id, left, right = list(map(int, input().rstrip().split()))
    nodes[id] = Node(id, left, right)

# set parent and sibling
for i in range(n):
    if nodes[i].left != -1:
        nodes[nodes[i].left].parent = nodes[i].id
        if nodes[i].right != -1:
            nodes[nodes[i].left].sibling = nodes[i].right
        
    if nodes[i].right != -1:
        nodes[nodes[i].right].parent = nodes[i].id
        nodes[nodes[i].right].sibling = nodes[i].left
       
# root
for i in range(n):
    if nodes[i].parent == -1:
        root = i
        break;
        
# depth 
def depthCalc(index, depth):
    nodes[index].depth = depth
    
    if nodes[index].left != -1:
        depthCalc(nodes[index].left, depth + 1)
    if nodes[index].right != -1:
        depthCalc(nodes[index].right, depth + 1)

depthCalc(root, 0)

# height
def heightCalc(index):
    heightL = 0
    heightR = 0
    
    if nodes[index].left != -1:
        heightL = heightCalc(nodes[index].left) + 1
    if nodes[index].right != -1:
        heightR = heightCalc(nodes[index].right) + 1
    
    height = max(heightL, heightR)
    nodes[index].height = height
    return height
    
heightCalc(root)
    
for i in range(n):
    nodes[i].toString()
