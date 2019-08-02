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
