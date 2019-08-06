# 案例1：双色球选号
# 一般摇出来红球6个，黄球1个

from random import sample

def select_balls(red = 6, yellow = 1):
    selected_balls = []
    red_balls = [x for x in range(1,34)]
    selected_red = sample(red_balls, red)
    selected_red.sort()
    yellow_balls = [x for x in range(1,17)]
    selected_yellow = sample(yellow_balls, yellow)
    selected_yellow.sort()
    selected_balls = selected_red + selected_yellow
    return selected_balls

def show_result(balls, bonus = 1):
    for index, ball in enumerate(balls):
        if index == len(balls) - bonus:
            print('|', end = ' ')
        print('%02d' % ball, end = ' ')
    print()

def main():
    n = int(input('Times of play: '))
    for _ in range(n):
        show_result(select_balls(10,3),3)

if __name__ == '__main__':
    main()
    
