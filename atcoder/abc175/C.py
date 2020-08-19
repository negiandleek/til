a,b,c = map(int, input().rstrip().split())
a = abs(a)
  
if a > b * c:
    print(abs(a - b*c))
else:
    n = a // c
    surplus = a % c
    m = b - n
    if m % 2 == 0:
        print(surplus)
    else:
        print(abs(min(surplus + c, surplus - c)))