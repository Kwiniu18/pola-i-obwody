import math
import click


class Triangle:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if (
            self.a > self.b + self.c
            and self.b > self.a + self.c
            and self.c > self.b + self.a
        ):
            print("\n")
            print("nie ma takiego trojkata, pomiary moga byc bledne!")
        return (self.a * self.h) / 2

    def is_triangle(self, a, b, c):
        return a < b + c


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (2 * self.a) + (2 * self.b)

    def area(self):
        return self.a * self.b

    def is_rectangle_possible(self, a, b):
        return (a * b) > 0


class Circle:
    def __init__(self, r):

        self.r = r

    def area(self):
        return math.pi * (r * r)

    def perimeter(self):
        return 2 * (math.pi) * r

    def is_circle_possible(self, r):
        return (2 * (math.pi) * r) > 0
