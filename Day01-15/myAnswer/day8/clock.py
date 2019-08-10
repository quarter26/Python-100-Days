from time import sleep
from os import system

class Clock(object):
    def __init__(self, hour = 0, minute = 0, second = 0):
        self._second = second
        self._minute = minute
        self._hour = hour

    def work(self):
        while(True):
            sleep(1)
            system('clear')
            self._second += 1
            if self._second == 60:
                self._second = 0
                self._minute += 1
                if self._minute == 60:
                    self._minute = 0
                    self._hour += 1
                    if self._hour == 24:
                        self._hour = 0
            print('%02d:%02d:%02d' % (self._hour, self._minute, self._second))

def main():
    clock = Clock(23, 59 ,57)
    clock.work()

if __name__ == '__main__':
    main()
