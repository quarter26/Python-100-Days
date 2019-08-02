def is_palindrome(num):
    temp = num
    reverse = 0
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp //= 10
#        print('reverse =', reverse)
#        print('temp =', temp)
    return reverse == num
