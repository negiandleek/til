heap = [None] + [-1] * 2000000
H = 1

def maxHeap(i):
    global heap
    left = i * 2
    right = i * 2 + 1
    largest = i
    if left < H and heap[largest] < heap[left]:
        largest = left
    if right < H and heap[largest] < heap[right]:
        largest = right
    
    if largest != i:
        temp = heap[i]
        heap[i] = heap[largest]
        heap[largest] = temp
        maxHeap(largest)
    
def insert(key):
    global H
    global heap
    i = H
    if key < heap[i]:
        return False
        
    heap[i] = key
    while i > 1:
        parent = (i // 2)
        if heap[i] > heap[parent]:
            temp = heap[parent]
            heap[parent] = heap[i]
            heap[i] = temp
            i = parent
        else:
            break;
    H += 1
            
def extract():
    global H
    global heap
    if len(heap) < 1:
        return False
    
    max = heap[1]
    heap[1] = heap[H - 1]
    heap[H - 1] = -1
    maxHeap(1)
    H-=1
    
    print(max)

while True:
    *A, = map(str, input().split())
    if A[0] == "insert":
        insert(int(A[1]))
    elif A[0] == "extract":
        extract()
    else:
        break

# but this code is Run Time Error.
# A better way to write, 

from heapq import *
import sys
q=[]
while True:
	a=sys.stdin.readline().split()
	if a[0]=='end': break
	if a[0]=='insert':
	    # min-heapなので-1 * int(x)
		heappush(q,-int(a[1]))
	else:
		print(-heappop(q))
