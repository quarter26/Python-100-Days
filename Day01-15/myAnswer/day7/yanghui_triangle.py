# 练习6：打印杨辉三角

def yanghui_triangle(n = 7):
    yh = [[]] * n
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1) # 元素为空的列表，占坑用
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

def main():
    yanghui_triangle()

if __name__ == '__main__':
    main()
