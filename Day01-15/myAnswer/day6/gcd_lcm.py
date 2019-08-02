def gcd(x, y):
    while x != y:
        if y > x:
            x, y = y, x
        x = x - y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)
