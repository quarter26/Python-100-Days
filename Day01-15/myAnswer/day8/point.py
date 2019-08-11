from math import sqrt

class Point(object):

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return(sqrt(dx ** 2 + dy ** 2))

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    point_a = Point(4, 3)
    point_o = Point()
    print(point_a)
    print(point_o)
    point_a.move_to(3, 4)
    print(point_a)
    point_a.move_by(1, -1)
    print(point_a)
    print(point_a.distance_to(point_o))

if __name__ == '__main__':
    main()
