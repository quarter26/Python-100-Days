# 打印斐波那契数列 Fibonacci sequence

num = int(input('num = '))
a = 0
b = 1
for i in range(num):
    a, b = b, a + b
    print(a, end= ' ')
