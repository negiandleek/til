# coding: utf-8
# Your code here!

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
    if node is None:
        return 
    
    # 削除するnodeが子を持たない
    if node.left == None and node.right == None:
        if node.parent == None:
            root = None
        else:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
    
    elif node.left != None and node.right != None:
        print("")
    else:
        child = node.left if node.left != None else node.right
        parent = node.parent
        if parent.left == node:
            parent.left = child
            child.parent = parent
        else:
            parent.right = a
            child.parent = parent
    
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
