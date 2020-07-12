n, m = map(int, input().rstrip().split())

edges = [[] for i in range(n)]
for _ in range(m):
    a,b = map(int, input().rstrip().split())
    edges[a].append(b)
    if a not in edges[b]:
        edges[b].append(a)

group = [None] * n
cnt = 0

for i in range(n):
    if group[i] == None:
        group[i] = cnt
        stack = [i]
        while stack:
            v = stack.pop()
            for c in edges[v]:
                if group[c] == None:
                    group[c] = cnt
                    stack.append(c)
        cnt += 1

q = int(input().rstrip())
for _ in range(q):
    a,b = map(int,input().rstrip().split())
    if group[a] == group[b]:
        print("yes")
    else:
        print("no")
