import math


class addComplex:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%i+%sj)' % (self.x, self.y)

    def __add__(self, next):
        new_x = self.x + next.x
        new_y = self.y + next.y
        return addComplex(new_x, new_y)

    def __mul__(self, next):
        new_x = self.x * next.x - self.y * next.y
        new_y = self.y * next.x + self.x * next.y
        return addComplex(new_x, new_y)


z1 = addComplex(1, 2)
z2 = addComplex(2, 3)

print(f"{z1} + {z2} = ", z1 + z2)
print(f"{z1} * {z2} = ", z1 * z2)
