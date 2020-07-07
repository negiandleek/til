# TODO:
n, m = map(int, input().rstrip().split())

friends = [[0 for i in range(n)] for i in range(n)]
for _ in range(m):
    a,b = map(int, input().rstrip().split())
    friends[a][b] = 1

ids = [None] * n

def dfs(index, id):
    global ids
    ids[index] = id
    node = friends[index]
    
    for i in range(n):
        if ids[i] == None and friends[index][i] == 1:
            dfs(i, id)
            
for i in range(n):
    if ids[i] == None:
        dfs(i, i + 1)
        
q = int(input().rstrip())
print(ids)
for _ in range(q):
    a,b = map(int,input().rstrip().split())
    if ids[a] == ids[b]:
        print("yes")
    else:
        print("no")
