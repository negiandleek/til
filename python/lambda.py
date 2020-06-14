# lambda 引数: 式

add = lambda x,y: x + y
add(1,2) # > 3

addCurry = lambda x: lambda y : x + y
addCurry(10)(20) # > 30

list(map(lambda x: x*x, range(10)))
# > [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
