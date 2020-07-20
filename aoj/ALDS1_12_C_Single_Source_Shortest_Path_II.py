# TODO
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/12/ALDS1_12_C
import math
n = int(input().rstrip())
g = [[] for _ in range(n)]
que = [None]

for _ in range(n):
    a,b,*c = map(int,input().rstrip().split())
    for i in range(b):
        g[a].append([c[i*2], c[i*2+1]])

def insert(key, cost):
    global que
    if len(que) == 1:
        que.append([key, cost])
        return True
    
    que.append([key, cost])
    i = len(que) - 1
    while i > 1 and que[i // 2][1] < que[i][1]:
        temp = que[i]
        que[i] = que[i // 2]
        que[i // 2] = temp
        i = i // 2
        
def sort(index):
    global que
    largest = index
    l = index*2
    r = index*2+1
    if l < len(que) and que[index][1] < que[l][1]:
        largest = l
        
    if r < len(que) and que[largest][1]< que[r][1]:
        largest = r
    
    if largest != index:
        temp = que[index]
        que[index] = que[largest]
        que[largest] = temp
        sort(largest)
        
def extract():
    global que
    if len(que) == 2:
        return que.pop()
    result = que[1]
    que[1]=que[-1]
    que = que[0:-1]
    sort(1)
    return result
    
def dijkstra(index):
    d = [math.inf for _ in range(n)]
    color = ["WHITE" for _ in range(n)]
    d[index] = 0
    insert(index,0)
    
    while len(que) > 1:
        u,_ = extract()
        color[u] = "BLACK"
        
        for i in range(len(g[index])):
            key,cost = g[index][i]
            if color[key] != "BLACK":
                if d[u] + cost < d[key]:
                    d[key] = d[u] + cost
                    color[key] = "GRAY"
                    insert(key, d[key])
    
    return d
print(dijkstra(0))
