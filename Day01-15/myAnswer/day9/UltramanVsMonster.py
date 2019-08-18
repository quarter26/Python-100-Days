from random import randint, randrange
from abc import ABCMeta, abstractmethod


class Fighters(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp', '_at', '_df')

    def __init__(self, name, hp, at, df):
        self._name = name
        self._hp = hp
        self._at = at
        self._df = df

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def at(self):
        return self._at

    @at.setter
    def at(self, at=0):
        self._at = at if at >= 0 else 0

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, df=0):
        self._df = df if df >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass


'''
    @abstractmethod
    def avoid(self):
        pass
'''


class Ultraman(Fighters):
    __slots__ = ('_name', '_hp', '_mp', '_at', '_df', '_cr')

    def __init__(self, name, hp, mp, at, df, cr):
        super().__init__(name, hp, at, df)
        self._mp = mp
        self._cr = cr if 0 <= cr <= 100 else 0

    def attack(self, other):
        if self._cr < randint(0, 100):
            if self._at > other.df:
                other.hp -= self._at - other.df
            else:
                other.hp -= 1
        else:
            if self._at * (100 + self._cr) / 100 > other.df:
                other.hp -= int(self._at * (100 + self._cr) / 100) - other.df
            else:
                other.hp -= 1

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for i in others:
                if i.alive > 0:
                    i.hp -= int(self._at * 0.2)
        else:
            return False

    def resume(self):
        incr_mp = randint(5, 10)
        self._mp += incr_mp
        incr_hp = randint(10, 20)
        self._hp += incr_hp
        return '恢复了%d点HP，%d点MP' % (incr_hp, incr_mp)

    def __str__(self):
        return '---%s奥特曼---\n' % self._name + 'HP: %d\n' % self._hp + 'MP: %d\n' % self._mp


class Monster(Fighters):
    __slots__ = ('_name', '_hp', '_at', '_df')

    def attack(self, other):
        if self._at > other.df:
            other.hp -= self._at
        else:
            other.hp -= 1

    def __str__(self):
        return '---%s小怪兽---\n' % self._name + 'HP: %d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster


def select_monster(monsters):
    monster_len = len(monsters)
    for i, monster in enumerate(monsters):
        print(i + 1, monster)
    selected_index = int(input('选择怪兽：'))
    while selected_index > monster_len:
        selected_index = int(input('WRONG INPUT! RETRY: '))
    selected_result = monsters[selected_index - 1]
    if selected_result.alive > 0:
        return selected_result


def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster, end='')


def main():
    # Ultraman (self, name, hp, mp, at, df, cr):
    u = Ultraman('迪迦', 1000, 100, 100, 30, 15)
    # Monster     __slots__ = ('_name', '_hp', '_at', '_df')
    m1 = Monster('哥斯拉', 200, 10, 10)
    m2 = Monster('金刚', 500, 50, 5)
    m3 = Monster('小鸡', 2000, 5, 20)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('=====第%02d回合=====' % fight_round)
        action = int(input('1. 攻击\n2. 使用技能\n3. 恢复\n'))
        if action == 1:
            target = select_monster(ms)
            print('%s使用普通攻击打了%s！' % (u.name, target.name))
            u.attack(target)
            if target.alive > 0:
                print('%s回击了%s！' % (target.name, u.name))
        elif action == 2:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击！' % u.name)
            else:
                print('%不行啊蓝不够！魔法攻击失败！')
        elif action == 3:
            u.resume()
        else:
            print('BAD INPUT! DO NOTHING!')
        for m in ms:
            if m.alive > 0:
                print('%s攻击了%s！' % (m.name, u.name))
                m.attack(u)
        display_info(u, ms)
        fight_round += 1
    if u.alive > 0:
        print('%s奥特曼 胜！' % u.name)
    else:
        print('小怪兽 胜！')


if __name__ == '__main__':
    main()
