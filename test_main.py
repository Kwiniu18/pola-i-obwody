from figures import Triangle
from figures import Rectangle
from figures import Circle


def test_is_triangle_possible():
    result = Triangle(1, 2, 3, 4)
    assert result.is_triangle(3, 4, 5)


def test_is_rectangle_possible():
    result = Rectangle(1, 2)
    assert result.is_rectangle_possible(3, 3)


def test_is_circle_possible():
    result = Circle(1)
    assert result.is_circle_possible(1)


# RECTANGLE TESITNG
def test_rectangle_area_calculations():
    result = Rectangle(4, 4)
    out = result.area()
    assert out == 16


def test_rectangle_perimeter_calculations():
    result = Rectangle(4, 4)
    out = result.perimeter()
    assert out == 16


# TRIANGLE TESTING
def test_triangle_perimeter_calculations():
    result = Triangle(5, 5, 5, 0)
    out = result.perimeter()
    assert out == 15


def test_triangle_area_calculations():
    result = Triangle(6, 0, 0, 2)
    out = result.area()
    assert out == 6


##CIRCLE TESTING
def test_circle_area_calculations():
    result = Circle(1)
    out = result.area(2)
    assert out == 12.566370614359172


def test_circle_perimeter_calculations():
    result = Circle(1)
    out = result.perimeter(2)
    assert out == 12.566370614359172
