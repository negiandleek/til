# TODO: よくわかってない
import math
N = int(input())
R = [0]*N
C = [0]*N
for i in range(N):
    R[i], C[i] = map(int, input().split())

dp = [[math.inf]*N for i in range(N)]
for i in range(N):
    dp[i][i] = 0
for l in range(1, N):
    for i in range(N-l):
        a0 = R[i]
        c0 = C[i+l]
        dp[i][i+l] = min(a0*C[j]*c0 + dp[i][j] + dp[j+1][i+l] for j in range(i, i+l))
print(dp[0][N-1])

# わからないので後回し
# http://daily-tech.hatenablog.com/entry/2018/09/29/203935
n = int(input().rstrip())

def calcMatrix(N, P):
    matrix = [[None]*N for _ in range(N)]
    for i in range(N):
        matrix[i][i] = 0
        
    for l in range(1, N): #行列の数
        for i in range(N - l): #行列の先頭
            j = i + l #行列の後尾
            for k in range(i, j): #組み合わせの区切りの位置
                try:
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k+1][j] + P[i] + P[k] + P[j])   
                except:
                    print(i, j)
                    print(*matrix)
                

arr = []            
for _ in range(n):
    *A, = input().rstrip().split()
    arr.append(int(A[0] * int(A[1])))

# print(arr)
calcMatrix(n, arr)
