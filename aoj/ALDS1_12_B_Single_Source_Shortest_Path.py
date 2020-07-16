# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/12/ALDS1_12_B
import math

n = int(input().rstrip())
m = []
G = [[math.inf for _ in range(n)] for _ in range(n)]
s = 0

for i in range(n):
    a,b,*c, = map(int, input().rstrip().split())
    m.append(a)
    if a == 0:
        s = i
    for j in range(b):
        G[i][c[j * 2]] = c[j * 2 + 1]
    
def dijkstra(index, G):
    # 初期化
    # 状態
    color = ['WHITE'] * n
    # コスト
    d = [math.inf] * n
    # 親
    p = [None] * n
    
    # 初期値
    d[index] = 0
    p[index] = -1
    u = -1
    
    while True:
        mincost = math.inf
        for i in range(n):
            if color[i] != "BLACK" and d[i] < mincost:
                u = i
                mincost = d[i]
        
        if mincost == math.inf:
            break;
        
        color[u] = "BLACK"
        
        for v in range(n):
            if d[u] + G[u][v] < d[v]:
                d[v] = d[u] + G[u][v]
                p[v] = u
                color[v] = 'GRAY'
               
    return d
    
costs = dijkstra(s, G)

for i in range(n):
    print(str(m[i]) + " " + str(costs[m[i]]))
