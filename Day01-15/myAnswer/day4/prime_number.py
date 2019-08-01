# 输入一个正整数判断它是不是素数

num = int(input('num = '))
prime_list = []
prime_list.append(2)

for i in range(3,num+1):
    is_prime = False
    for j in prime_list:
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        prime_list.append(i)
list_length = len(prime_list)
if prime_list[list_length - 1] == num:
    print('%d is a prime number.' % num)
else:
    print('%d is NOT a prime number.' % num)
