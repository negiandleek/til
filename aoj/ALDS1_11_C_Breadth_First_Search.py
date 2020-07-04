N = int(input().rstrip())

class Node:
    __slots__ = ["key", "depth"]
    def __init__(self, key):
        self.key = key
        self.depth = 0
        
    def toString(self):
        return "" + str(self.key + 1) + " " + str(self.depth)

def generate(n):
    result = [[0]*n for _ in range(n)]
    for _ in range(n):
        u, a, *b = map(int, input().rstrip().split())
        
        for i in range(a):
            result[u-1][b[i]-1] = 1
    return result
    
graph = generate(N)
nodes = []
count = 0
for i in range(N):
    nodes.append(Node(i))

def bfs(Graph, Nodes, U):
    ...
    
for i in range(N):
    if nodes[i].discovery == 0:
        depth(graph, nodes, i)
