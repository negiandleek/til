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

def unit(x, y):
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

# FIXME
def same(x, y):
    rx = x if x.root == -1 else x.root
    ry = y if y.root == -1 else y.root
    if rx.key == ry.key:
        print("1")
    else:
        print("0")

for _ in range(m):
    q, x, y = map(int, input().rstrip().split())
    if q == 0:
        unit(nodes[x], nodes[y])
    else:
        same(nodes[x], nodes[y])
