# 找出1~9999之间的所有完美数
# 完美数是除自身外其他所有因子的和正好等于这个数本身的数
# 例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

perfect_number = []
perfect_number.append(1)

for num in range(1, 10000):
    number_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            number_sum += i
    if number_sum == num:
        perfect_number.append(num)
print(perfect_number)
