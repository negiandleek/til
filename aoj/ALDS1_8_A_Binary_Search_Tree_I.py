# coding: utf-8
# Your code here!

n = int(input().rstrip())

class Node:
    __slots__ = ['key', 'left', 'right']
    def __init__(self,key):
        self.key = int(key)
        self.left = self.right = None
        
root = None

def insert(z):
    global root
    x, y = root, -1
    
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
            
    if y == -1:
        root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def inorder(node):
    return inorder(node.left) + f' {node.key}' + inorder(node.right) if node else ''
    
def preorder(node):
    return f' {node.key}' + preorder(node.left) + preorder(node.right) if node else ''
        
for i in range(n):
    temp = input().rstrip().split()
    if temp[0] == "insert":
        insert(Node(temp[1]))
    else:
        print(inorder(root))
        print(preorder(root))
        
        
