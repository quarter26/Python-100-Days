"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次摇色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
"""

from random import randint

money = 1000
while money > 0:
    print("You have $%d." % money)
    next_turn = False
    debt = int(input('Input your debt: $'))
    while debt > money or debt < 0:
        print('BAD input!')
        debt = int(input('Input your debt again: $'))
    first_play = randint(1, 6) + randint(1, 6)
    print('The first result is %d.' % first_play)
    if first_play == 7 or first_play == 11:
        print('Player win!')
        money += debt
    elif first_play == 2 or first_play == 3 or first_play == 12:
        print('Banker win!')
        money -= debt
    else:
        next_turn = True
        print('Go on the next turn.')
    while next_turn:
        second_play = randint(1, 6) + randint(1, 6)
        print('The second result is %d.' % second_play)
        if second_play == 7:
            print('Banker win!')
            money -= debt
            next_turn = False
        elif second_play == first_play:
            print('Player win!')
            money += debt
            next_turn = False
print('You are broken.  Game over.')
