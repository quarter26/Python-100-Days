# 练习3：设计一个函数返回给定文件名的后缀名。

def get_file_xts(filename, has_dot = False): # 把带不带点儿都考虑到了，可以
    pos = filename.rfind('.') # 这题看答案了，不知道 str.rfind 这个函数
    # str.rfind 返回匹配想要字符串的最高位索引，可以在字符串后加搜索的切片区间
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

def main():
    print(get_file_xts('hello.txt.py'))

if __name__ == '__main__':
    main()
