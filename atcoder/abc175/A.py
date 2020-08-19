n = input().rstrip()
count = 0
max = 0
for i in range(len(n)):
    if n[i] == "R":
        count += 1
        if max < count:
            max = count
    else:
        count = 0
  
print(max)