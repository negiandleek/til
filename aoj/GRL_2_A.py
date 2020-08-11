# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
# TODO:
import math

n,m = map(int, input().rstrip().split())

nodes = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))
    
def minimum():
    d = [math.inf for _ in range(n)]
    b = [0 for _ in range(n)]
    
    d[0] = 0
    
    count = 0
    while True:
        cost = math.inf
        u = -1
        
        for i in range(n):
            if d[i] < cost and b[i] == 0:
                cost = d[i]
                u = i
                
        if cost == math.inf:
            break;
            
        b[u] = 1
        
        for j in nodes[u]:
            if d[j[0]] > j[1]:
                d[j[0]] = j[1]
        
        count += 1
        
    return d
        
result = minimum()
answer = 0
for value in result:
    answer += value
    
print(answer)
