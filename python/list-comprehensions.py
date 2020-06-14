# リスト内包表記 
# [式 for 任意の変数名 in 任意のシーケンス型 条件式]

print([char for char in "abc"])
# > ["a", "b", "c"]

a = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
b = [a[i] for i in range(len(a)) if  i % 2 == 0]
# > [0, 4, 16, 36, 64]
