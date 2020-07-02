# url -> https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/11/ALDS1_11_A
N = int(input().rstrip())

def generateGraph(N):
    graph = [[0]*N for _ in range(N)]
    for _ in range(N):
        U, A, *B = map(int, input().rstrip().split())
        
        for i in range(A):
            graph[U-1][B[i]-1] = 1
    
    return graph
        
result = generateGraph(N)
for i in range(len(result)):
    print(*result[i])
