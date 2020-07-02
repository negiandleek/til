# TODO:
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/11/ALDS1_11_B
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
for i in range(N):
    Nodes.append(Node(i))


def nextGraph(N):
    key = N.key
    result = None
    for i in range(len(Graph[key])):
        if Graph[key][i] == 1 and Nodes[i].discovery == 0:
            result = i
            break
        
    return result
            
    

def depth(G, N):
    Stack = []
    count = 1
    N[0].discovery = count
    Stack.append(N[0])
    
    while Stack != []:
        node = Stack[len(Stack) - 1]
        v = nextGraph(node)
        count += 1
        if v != None:
            N[v].discovery = count
            Stack.append(N[v])
        else:
            a = Stack.pop()
            a.finish = count
            
depth(Graph, Nodes)

for i in range(len(Nodes)):
    print(Nodes[i].toString())
