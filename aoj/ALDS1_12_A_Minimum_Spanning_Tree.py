# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/12/ALDS1_12_A

import math
n = int(input().rstrip())

def generateGraph():
    a = [[] for _ in range(n)]
    for i in range(n):
        b = list(map(int, input().lstrip().split()))
        for j in range(n):
            a[i].append(b[j])
    return a
    
def prims(graph):
    # 初期化
    color = ['WHITE' for _ in range(n)]
    # Tに属する頂点とV-Tに属する頂点をつなぐ辺の中の最小の重み
    d = [math.inf for _ in range(n)]
    d[0] = 0
    #  MSTにおける頂点vの親
    p = [None for _ in range(n)]
    p[0] = -1
    # VとV-Tを繋ぐ辺の最小の重みになる頂点
    u = -1
    
    while True:
        mincost = math.inf
        # VとV-Tから最小のコストを持つエッジを選択
        for i in range(n):
            if color[i] != 'BLACK' and d[i] < mincost:
                mincost = d[i]
                u = i
        
        if mincost == math.inf:
            break;
            
        color[u] = 'BLACK'
        # V-Tの
        for v in range(n):
            if color[v] != 'BLACK' and graph[u][v] != -1:
                if graph[u][v] < d[v]:
                    d[v] = graph[u][v]
                    # p[v] = u
                    # color[v] = 'GRAY'
    return sum(d)

graph = generateGraph()
result = prims(graph)
print(result)
