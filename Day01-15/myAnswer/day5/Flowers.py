# 找出100~999之间的所有水仙花数
# 水仙花数是各位立方和等于这个数本身的数
# 如: 153 = 1**3 + 5**3 + 3**3

for n in range(100, 1000):
    ge = n % 10
    shi = n % 100 // 10
    bai = n // 100
    if n == ge**3 + shi**3 + bai**3:
        print(n)
