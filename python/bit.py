# 0未満を 0にするビット演算子
x & ~(x >> 31))

# さらに、1より大きい数を1にするビット演算子
1 & ((x & ~(x >> 31)) > 0)

# これと同じ
min(1, max(0, x))