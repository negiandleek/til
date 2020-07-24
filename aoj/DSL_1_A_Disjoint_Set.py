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
        
def same(x, y):
    rx = find(x)
    ry = find(y)
    return True if rx.key == ry.key else False
        
# FIXME
# forestのpresentativeを合併する
def unit(x, y):
    isSame = same(x,y)
    if isSame == True:
        return
    if x.rank < y.rank:
        y.parent = x
        root = x if x.root == -1 else x.root
        y.root = root
        root.rank += y.rank != 0 if y.rank else 1
    else:
        x.parent = y
        root = y if y.root == -1 else y.root
        x.root = root
        root.rank += x.rank != 0 if x.rank else 1

for _ in range(m):
    q, x, y = map(int, input().rstrip().split())
    if q == 0:
        unit(nodes[x], nodes[y])
    else:
        isSame = same(nodes[x], nodes[y])
        print("1" if isSame == True else "0" )
