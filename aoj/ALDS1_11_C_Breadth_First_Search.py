N = int(input().rstrip())

class Node:
    __slots__ = ["key", "depth"]
    def __init__(self, key):
        self.key = key
        self.depth = -1
        
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

def bfs(Graph, Nodes):
    depth = 0
    Nodes[0].depth = depth
    que = [Nodes[0]]
    while que != []:
        deque = que[0]
        que = que[1:]
        for v in range(N):
            if Graph[deque.key][v] == 1 and Nodes[v].depth == -1:
                Nodes[v].depth = deque.depth + 1
                que.append(Nodes[v])
            
    
for i in range(len(nodes)):
    if nodes[i].key == 0:
        nodes[i].depth = 0
        bfs(graph, nodes)
        break;
        
for i in range(len(nodes)):
    print(nodes[i].toString())
    
