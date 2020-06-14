# coding: utf-8
# Your code here!

n = int(input().rstrip())
nodes = [None] * n

for i in range(n):
    index, left, right = list(map(int, input().rstrip().split()))
    nodes[index] = [left, right, -1]
    
for i in range(n):
    left, right, _ = nodes[i]
    nodes[left][2] = i
    nodes[right][2] = i

root = 0
for i in range(n):
    if nodes[i][2] == -1:
        root = i
        break

preNodes = []
inOrderNodes = []
postOrderNodes = []

def preOrder(index):
    global preNodes
    
    left, right, _ = nodes[index]
    preNodes.append(str(index))
    if left != -1:
        preOrder(left)
    if right != -1:
        preOrder(right)
        
def InOrder(index):
    global inOrderNodes
    left, right, _ = nodes[index]
    if left != -1:
        InOrder(left)
    inOrderNodes.append(str(index))
    if right != -1:
        InOrder(right)

def PostOrder(index):
    global postOrderNodes
    left, right, _ = nodes[index]
    if left != -1:
        PostOrder(left)
    if right != -1:
        PostOrder(right)
    postOrderNodes.append(str(index))
        
preOrder(root)
InOrder(root)
PostOrder(root)
    
print("Preorder")
print(" " + " ".join(preNodes))
print("Inorder")
print(" " + " ".join(inOrderNodes))
print("Postorder")
print(" " + " ".join(postOrderNodes))
    
