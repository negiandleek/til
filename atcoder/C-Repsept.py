# https://atcoder.jp/contests/abc174/tasks/abc174_c
n = int(input().rstrip())
  
def calc(target):
    result = 0
    count = 0
    if target % 2 == 0:
        print(-1)
        return
        
    for i in range(n):
        result = (result * 10 + 7) % target
        count += 1
        if result == 0:
            print(count)
            return
    
    print(-1)
    
calc(n)