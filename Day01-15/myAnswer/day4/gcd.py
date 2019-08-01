# 求最大公约数GCD，即(a,b)
# 算法：更相减损法，全程就是比较和减法，感觉效率比辗转相除法高点。

num1 = int(input('num1 = '))
num2 = int(input('num2 = '))

while num1 != num2:
    if num2 > num1:
        num1, num2 = num2, num1
    num1 = num1 - num2
print('gcd is', num1)
