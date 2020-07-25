# NOTE
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A
n,m = map(int, input().rstrip().split())

class Node:
    def __init__(self, key):
        self.key = key
        self.root = -1
        self.rank = 0
        self.parent = -1
    def toString(self):
        return str(self.key) + ": rank: " + str(self.rank) + ": root:" + str(self.key if self.root == -1 else self.root.key)

nodes = [Node(i) for i in range(n)]

def find(node):
    while node.root != -1:
        node = node.root
    return node
    
def same(x, y):
    rx = find(x)
    ry = find(y)
    return True if rx.key == ry.key else False
        
def unit(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    if rx.rank < ry.rank:
        ry.parent = rx
        root = rx if rx.root == -1 else rx.root
        ry.root = root
        root.rank += ry.rank != 0 if ry.rank else 1
    else:
        rx.parent = ry
        root = ry if ry.root == -1 else ry.root
        rx.root = root
        root.rank += rx.rank != 0 if rx.rank else 1

for _ in range(m):
    q, x, y = map(int, input().rstrip().split())
    if q == 0:
        unit(nodes[x], nodes[y])
    else:
        isSame = same(nodes[x], nodes[y])
        print("1" if isSame == True else "0" )
