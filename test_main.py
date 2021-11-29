from figures import Triangle
from figures import Rectangle
from figures import Circle

def test_is_triangle_possible():
    result = Triangle(1, 2, 3)
    assert result.is_triangle(1, 2, 3)

def test_is_rectangle_possible():
    result = Rectangle(3,3)
    assert result.is_rectangle_possible(3, 3)

def test_is_circle_possible():
    result = Circle(1)
    assert result.is_circle_possible(1)
