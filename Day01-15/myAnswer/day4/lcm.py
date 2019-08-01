# 求最小公倍数LCM，即[a,b]
# 原理： a * b = (a, b) * [a, b]
# 未来可以把gcd写成函数调用，目前还不会

num1 = int(input('num1 = '))
num2 = int(input('num2 = '))
ji = num1 * num2

while num1 != num2:
    if num2 > num1:
        num1, num2 = num2, num1
    num1 = num1 - num2
gcd = num1
lcm = int(ji / gcd)
print('lcm is', lcm)
