"""
约瑟夫斯问题
总共m个人，每n个一杀（m>=n)
"""
def josephus1(m = 41, n = 3):
    alive = [index for index in range(1,m+1)]
    dead = []
    kill = 0
    step = 0
    while len(alive) - len(dead) > n - 1:
        if alive[kill] in dead:
            kill += 1
            if kill > 40:
                kill -= 41
        else:
            step += 1
            if step == n:
                dead.append(alive[kill])
                kill += 1
                if kill > 40:
                    kill -= 41
                step = 0
            else:
                kill += 1
                if kill > 40:
                    kill -= 41
    return list(set(alive) - set(dead))

def main():
    a = josephus1()
    print(a)

if __name__ == '__main__':
    main()
