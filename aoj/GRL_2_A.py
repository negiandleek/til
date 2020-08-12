# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
# TODO:import math

n,m = map(int, input().rstrip().split())

edges = [None for _ in range(m)]
nodes = [None for _ in range(n)]

class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost
    def toString(self):
        print("" + str(self.start) + " " + str(self.end) + " " + str(self.cost))
        
class Node:
    def __init__(self, key):
        self.height = 1
        self.key = key
        self.root = -1
        self.children = -1
    def toString(self):
        return "" + str(self.key) + " " + str(self.root)
        
for i in range(m):
    a,b,c = map(int, input().rstrip().split())
    edges[i] = Edge(a,b,c)
    
edges = sorted(edges, key=lambda value: value.cost)

for i in range(n):
    nodes[i] = Node(i)
    
def root(n):
    if nodes[n].root == -1:
        return n
    nodes[n].root = root(nodes[n].root)
    return nodes[n].root
    
def find(n):
    if nodes[n].root == -1:
        return n
        
    return root(nodes[n].root)
    
def some(a, b):
    return root(a) == root(b)
    

def unit(a, b):
    ra = root(a)
    rb = root(b)
    
    if ra == rb:
        return
    
    if nodes[a].height >= nodes[b].height:
        nodes[b].root = ra
        nodes[a].children = b
        nodes[a].height += nodes[b].height
    else:
        nodes[a].root = rb
        nodes[b].children = a
        nodes[b].height += nodes[a].height

def minimum():
    global edges
    d = 0
    while edges:
        edge = edges[0]
        if some(edge.start, edge.end) == False:
            unit(edge.start, edge.end)
            d += edge.cost
        edges = edges[1:]
    
    return d

print(minimum())
