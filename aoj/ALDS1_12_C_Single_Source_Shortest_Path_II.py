# WIP
# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/12/ALDS1_12_C
from heapq import heappush, heappop

inf = float('inf')
n = int(input())
g = []
for i in range(n):
    line = list(map(int, input().split()[2:]))
    g.append(zip(line[0::2], line[1::2]))
    
d = [inf] * n
d[0] = 0
heap = [(0, 0)]

while heap:
    cost, current = heappop(heap)
    
    if d[current] < cost:
        continue
    
    for v, c in g[current]:
        currentCost = d[current] + c
        if currentCost < d[v]:
            d[v] = currentCost
            heappush(heap, (currentCost, v))
                
for i in range(n):
    print(i, d[i])
