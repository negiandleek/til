n = int(input().rstrip())

def fib(count):
    if count == 0 or count == 1:
        return 1
    else:
        return fib(count - 1) + fib(count - 2)

result = [1, 1] + [None]*(n-1)

def fibByMemo(count):
    global result
    if count == 0 or count == 1:
        return result[count]
    if result[count] != None:
        return result[count]
        
    result[count] = fibByMemo(count - 1) + fibByMemo(count - 2)
    return result[count]

result2 = [1,1] + [None]*(n-1)
def findByDynamic(count):
    global result2
    for i in range(2, count+1):
        result2[i] = result2[i-1] + result2[i-2]
        
print(fib(2))
fibByMemo(n)
print(*result)
findByDynamic(n)
print(*result2)
