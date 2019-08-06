# 练习1：在屏幕上显示跑马灯文字

import os
import time

def lighting1():
    content = 'Welcome...   '
    while True:
        os.system('clear')  # 或cls
        print(content)
        time.sleep(0.1)
        content = content[1:] + content[0] # 最低位绕到最后

def lighting2():
    content = 'Welcome...   '
    while True:
        os.system('clear')
        time.sleep(0.2) # 就多了个字会闪的效果。。。
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

def main():
    lighting1()

if __name__ == '__main__':
    main()
