N = int(input().rstrip())

class Node:
    __slots__ = ["key", "discovery", "finish"]
    def __init__(self, key):
        self.key = key
        self.discovery = 0
        self.finish = 0
        
    def toString(self):
        return "" + str(self.key + 1) + " " + str(self.discovery) + " " + str(self.finish)
        
def generateGraph(N):
    graph = [[0]*N for _ in range(N)]
    for _ in range(N):
        U, A, *B = map(int, input().rstrip().split())
        
        for i in range(A):
            graph[U-1][B[i]-1] = 1
    
    return graph
        
Graph = generateGraph(N)
Nodes = []
count = 0
for i in range(N):
    Nodes.append(Node(i))

# Stackを使うやり方
def depth(G, N, U):
    global count
    Stack = []
    count += 1
    N[U].discovery = count
    Stack.append(N[U])
    
    while Stack != []:
        node = Stack[len(Stack) - 1]
        v = next(node)
        count += 1
        if v != None:
            N[v].discovery = count
            Stack.append(N[v])
        else:
            a = Stack.pop()
            a.finish = count
            
def next(N):
    key = N.key
    result = None
    for i in range(len(Graph[key])):
        if Graph[key][i] == 1 and Nodes[i].discovery == 0:
            result = i
            break
        
    return result
  
for i in range(N):
    if Nodes[i].discovery == 0:
        depth(Graph, Nodes, i)

# 再起を使うやり方
def dfs(graph, nodes, index):
    global count
    count += 1
    nodes[index].discovery = count
    
    for v in range(N):
        if graph[index][v] and nodes[v].discovery == 0:
            dfs(graph, nodes, v)
    
    count += 1
    nodes[index].finish = count

# print
for i in range(len(Nodes)):
    print(Nodes[i].toString())
