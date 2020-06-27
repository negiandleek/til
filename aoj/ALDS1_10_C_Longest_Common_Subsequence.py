# TLE 
# 参考にする -> https://onlinejudge.u-aizu.ac.jp/solutions/problem/ALDS1_10_C/review/3456820/kichi941/Python3
n = int(input().rstrip())

def lcs(x, y):
    m = len(x) + 1
    n = len(y) + 1
    c = [ [0 for j in range(n)] for i in range(m) ]
    maxL = 0
    
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
