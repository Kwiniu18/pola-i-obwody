import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return a + b + c

    def area(self):
        return (a * h) / 2

    def is_triangle(self, a, b, c):
        return a < b + c


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (2 * a) + (2 * b)

    def area(self):
        return a * b

    def is_rectangle_possible(self, a, b):
        return (a * b) > 0


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (r * r)

    def perimeter(self):
        return 2 * (math.pi) * r

    def is_circle_possible(self,r):
        return (2 * (math.pi) * r) > 0
