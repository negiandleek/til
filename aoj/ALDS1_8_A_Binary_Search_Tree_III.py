# coding: utf-8
# Your code here!
# TODO

n = int(input().rstrip())

class Node:
    __slots__ = ['key', 'left', 'right', 'parent']
    def __init__(self, key):
        self.key = int(key)
        self.left = self.right = self.parent = None


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
        node.parent = y
        y.left = node
    else:
        node.parent = y
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
    
def delete(key):
    global root
    node = find(key)
    y = x = None
    if node is None:
        return 
    
    if node.left == None or node.right == None:
        y = node
    else:
        y = getSuccessor(node)
    
    # 子の操作
    if y.left != None:
        x = y.left
    else:
        x = y.right
        
    if x != None:
        x.parent = y.parent
        
    if y.parent == None:
        root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
        
    if y != node:
        node.key = y.key      
        
def getSuccessor(node):
    if node.right != None:
        return getMinimum(node)
    
    y = node.parent
    while y != None and node == y.right:
        node = y
        y = y.parent

    return y
    
def getMinimum(node):
    while node.left != None:
        node = node.left
    return node
    
def inOrder(node):
    return inOrder(node.left) + " " + str(node.key) + inOrder(node.right) if node else ''
    
def preOrder(node):
    return  " " + str(node.key) + preOrder(node.left) + preOrder(node.right) if node else ''
    
for i in range(n):
    command = input().rstrip().split()
    if command[0] == "insert":
        insert(Node(command[1]))
    elif command[0] == "delete":
        delete(command[1])
    elif command[0] == "find":
        if find((command[1])) is None:
            print("no")
        else:
            print("yes")
    elif command[0] == "print":
        print(inOrder(root))
        print(preOrder(root))
