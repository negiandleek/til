# TODO
n, m = map(int, input().rstrip().split())
p = list(map(int, input().rstrip().split()))
c = list(map(int, input().rstrip().split()))
  
r = [None for _ in range(n)]
  
for i in range(n):
    a = c[p[i] - 1]
    r[i] = a
  
maximum = -1 * (10 ** 9) - 1
  
for i in range(n):
    next = p[i] - 1
    tMax = -1 * (10 ** 9) - 1
    total = 0
    
    for j in range(m):
        total = total + r[next]
        tMax = max(total, tMax)
        next = p[next] - 1
        
    maximum = max(maximum, tMax)
        
print(maximum)