# 求最大公约数GCD，即(a,b)
# 算法：扩展欧几里得算法，还可以求出类似 xa + yb = gcd(a,b) = d 中(x,y)的结果。

num1 = int(input('num1 = '))
num2 = int(input('num2 = '))

def egcd(a, b):
    if b > a:
        a, b = b, a
    if a % b == 0:
        return (b, 0, 1)
    else:
        for q in range(0, a // b + 1):
            r = a - b * q
            if r > b:
                continue
            else:
                break
        d, x, y = egcd(b, r)
        return (d, y, x - y * q)

gcd = egcd(num1, num2)
print('gcd is',gcd[0])
