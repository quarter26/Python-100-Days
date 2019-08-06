# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index] # 遍历整个列表
        elif x[index] > m2:
            m2 = x[index] # 如果列表里出现两个最大值就完蛋
    return m1, m2

def max2_2(x):
    setx = set(x)
    m1 = max(setx) # 用集合剔除重复的元素，找出最大的
    setx.discard(m1) # 把刚刚找到的最大值删掉，再找就是第二大的了
    m2 = max(setx)
    return m1, m2

def main():
    list1 = [0,1,2,2,3,3,3,4,4,4,4]
    print(max2(list1))
    print(max2_2(list1))

if __name__ == '__main__':
    main()
