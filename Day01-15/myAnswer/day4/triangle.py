# 打印各种三角形

row = int(input('row = '))
for i in range(row):
    for j in range(i + 1):
        print('*', end = '')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i -1:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()

for i in range(row+1):
    print(' ' * (row - i), end = '')
    print('*' * (2 * i - 1))
