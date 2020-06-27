# TODO:
n = int(input().rstrip())

def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [ [0 for j in range(m)] for i in range(n) ]
    maxL = 0
    print(c)
    for i in range(1, m):
        for j in range(1, n):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
            
            maxL = max(maxL, c[i][j])
            
    return maxL
    
for i in range(n):
    a = input().rstrip()
    b = input().rstrip()
    print(lcs(a, b))
