import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        while True:
            self.per = a + b + c
            if a <=(c+b):
                print("taki trojkat nie istnieje")
                quit()
            else: return self.per

    def area(self):
        self.ar = (a*h)/2
        return self.ar


class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def perimeter(self):
        self.per = (2*a)+(2*b)
        return self.per

    def area(self):
        self.ar = a*b
        return self.ar


class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        self.ar = math.pi*(r*r)
        return self.ar

    def perimeter(self):
        self.per = 2*(math.pi)*r
        return self.per


while True:
    figure = str(input("Jakia figure chcesz obliczac?: prostokat,kwadrat,trojkat,kolo"))
    if str(figure) not in ["prostokat","kwadrat","kolo","trojkat","1","2","3","4",]:
        print("Nie poprawna nazwa!")
        continue
    else: break

if figure == "trojkat" or figure=="4": ##############TRIANGLE
    while True:
        try:
            a = int(input("Podaj podstawe: "))
            b = int(input("Podaj drugi bok: "))
            c = int(input("Podaj trzeci bok: "))
            h = int(input("Podaj wysokosc opadajaca na podstawe: "))
            break
        except ValueError: print("Podaj poprawna wartosc!")
    type_of = Triangle(a, b, c)

if figure == "prostokat" or figure=="kwadrat" or figure in ["1","2"]: ##############RECTANGLE
    while True:
        try:
            a = int(input("Podaj pierwszy bok: "))
            b = int(input("Podaj drugi bok: "))
            break
        except ValueError: print("Podaj poprawna wartosc!")
    type_of = Rectangle(a, b)

if figure == "kolo" or figure== "3": ##############CIRCLE
    while True:
        try:
            r = float(input("Podaj promien kola: "))
            break
        except ValueError: print("Podaj poprawna wartosc!")
    type_of = Circle(r)

print("Pole wynosi:",type_of.area())
print("Obwod wynosi:",type_of.perimeter())
waiting = input("press enter to end")