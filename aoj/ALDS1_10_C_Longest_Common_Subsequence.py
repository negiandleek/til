# TLE 
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

# 最適化したやつ

def optLcs(x, y):
    X = ' ' + x
    Y = ' ' + y
    m = len(X)
    n = len(Y)
    maxL = 0
    c = [ [0 for j in range(n)] for i in range(m) ]
    
    pre_row = c[0]
    for i in range(1, m):
        row = c[i]
        XX = X[i]
        for j, YY in enumerate(Y):
            if XX == YY:
                pre = pre_row[j - 1]
                row[j] = pre + 1
                if row[j] > maxL:
                    maxL = row[j]
            else:
                pre = pre_row[j]
                column = row[j-1]
                if pre >= column:
                    row[j] = pre
                else:
                    row[j] = column
        pre_row = row
    return maxL

# x = abc
# y = bacd
# i = row, j = column
# [0, 0, 0, 0, 0] 
# [0, 0, 1, 1, 1] 
# [0, 1, 1, 1, 1]
# [0, 1, 1, 2, 2]
# [0, 1, 1, 1] 
# [0, 1, 1, 2]
# -> 2
 
