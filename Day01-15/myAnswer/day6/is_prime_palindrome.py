def is_palindrome(num):
    temp = num
    reverse = 0
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10

def is_prime(num):
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
    return prime_list[list_length - 1] == num

if __name__ == '__main__':
    num = int(input('>>>'))
    if is_palindrome(num) and is_prime(num):
        print('num is both palindrome and prime')
    else:
        print('num is not both palindrome and prime')
