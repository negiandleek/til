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
for i in range(N):
    nodes.append(Node(i))

def bfs(Graph, Nodes, index, count):
    stash = []
    for v in range(N):
        if Graph[index][v] == 1 and Nodes[v].depth == 0:
            Nodes[v].depth = count + 1
            stash.append(v)
            
    for v in range(len(stash)):
        bfs(Graph, Nodes, stash[v], count + 1)
        
    
    
for i in range(N):
    if nodes[i].depth == 0:
        bfs(graph, nodes, i, 0)
        
for i in range(len(nodes)):
    print(nodes[i].toString())
    
