# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

import random

def generate_code(code_len = 4):
    all_chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1 # 上面把所有可能的字符都写进去了
    code = ''
    for _ in range(0, code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code

# 第二种每次循环调用了两次randint，感觉效率不如上面的
# 但是不用存一个字符串了
def generate_code2(code_len = 4):
    code = ''
    for _ in range(0, code_len):
        char_type = random.randint(0,2) # 确认数字、小写或是大写字母
        if char_type == 0:
            code += chr(random.randint(48,57)) # ASCII码转换
        elif char_type == 1:
            code += chr(random.randint(65,90))
        else:
            code += chr(random.randint(97,122))
    return code


def main():
    print(generate_code())
    print(generate_code2())

if __name__ == '__main__':
    main()
