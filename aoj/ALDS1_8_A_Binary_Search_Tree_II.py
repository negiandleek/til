# coding: utf-8
# Your code here!

n = int(input().rstrip())

class Node:
    __slots__ = ['key', 'left', 'right']
    def __init__(self, key):
        self.key = int(key)
        self.left = self.right = None


root = None

def insert(node):
    global root
    y, x = None, root
    
    while x != None:
        y = x
        if node.key < x.key:
            x = x.left
        else:
            x = x.right
    
    if y == None:
        root = node
    elif node.key < y.key:
        y.left = node
    else:
        y.right = node
        
        
def find(key):
    global root
    node = root
    num = int(key)
    while node != None and node.key != num:
        if num < node.key:
            node = node.left
        else:
            node = node.right
            
    return node
    
    
def inOrder(node):
    return inOrder(node.left) + " " + str(node.key) + inOrder(node.right) if node else ''
    
def preOrder(node):
    return  " " + str(node.key) + preOrder(node.left) + preOrder(node.right) if node else ''
    
for i in range(n):
    command = input().rstrip().split()
    if command[0] == "insert":
        insert(Node(command[1]))
    elif command[0] == "find":
        if find((command[1])) is None:
            print("no")
        else:
            print("yes")
    elif command[0] == "print":
        print(inOrder(root))
        print(preOrder(root))
