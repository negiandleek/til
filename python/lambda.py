# lambda 引数: 式

add = lambda x,y: x + y
add(1,2) # > 3

addCurry = lambda x: lambda y : x + y
addCurry(10)(20) # > 30
