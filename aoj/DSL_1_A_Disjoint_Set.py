# NOTE
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_A
n,m = map(int, input().rstrip().split())

class Forest:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [-1] * n
        self.root = [-1] * n
    def boss(self, index):
        if self.root[index] == -1:
            return index
        else:
            self.root[index] = self.boss(self.root[index])
            return self.root[index]
    def find(self, index):
        while self.root[index] != -1:
            index = self.root[index]
        return index
        
    def same(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        return True if rx == ry else False
        
    def unit(self, x, y):
        rx = self.boss(x)
        ry = self.boss(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.root[ry] = rx
            self.rank[rx] += self.rank[ry]
        else:
            self.root[rx] = ry
            self.rank[ry] += self.rank[rx]
        
forest = Forest(n)

for _ in range(m):
    q, x, y = map(int, input().rstrip().split())
    if q == 0:
        forest.unit(x, y)
    else:
        isSame = forest.same(x, y)
        print("1" if isSame == True else "0")
