n = int(input().rstrip())
a = [None] + list(map(int, input().rstrip().split()))

def maxHeapify(A, i):
    l = i * 2
    r = i * 2 + 1
    largest = i
    
    if l <= n and A[l] > A[i]:
        largest = l
    
    if r <= n and A[r] > A[largest]:
        largest = r
        
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        maxHeapify(A, largest)
        
for i in reversed(range(1, (n // 2) + 1)):
    maxHeapify(a, i)

print("" , *a[1:])
