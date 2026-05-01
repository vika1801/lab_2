import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides


# Тест №1: Равносторонний
def test_equilateral_int():
    t = Triangle(3, 3, 3)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 9


# Тест №2: Равносторонний (дробные)
def test_equilateral_float():
    t = Triangle(1.5, 1.5, 1.5)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == pytest.approx(4.5)


# Тест №3: Равносторонний минимальный
def test_equilateral_minimal():
    t = Triangle(1, 1, 1)
    assert t.triangle_type() == "equilateral"
    assert t.perimeter() == 3


# Тест №4: Равнобедренный (a == b)
def test_isosceles_ab():
    t = Triangle(5, 5, 3)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 13


# Тест №5: Равнобедренный (b == c)
def test_isosceles_bc():
    t = Triangle(4, 6, 6)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 16


# Тест №6: Равнобедренный (a == c)
def test_isosceles_ac():
    t = Triangle(7, 5, 7)
    assert t.triangle_type() == "isosceles"
    assert t.perimeter() == 19


# Тест №7: Разносторонний (целые)
def test_nonequilateral_int():
    t = Triangle(3, 4, 5)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == 12


# Тест №8: Разносторонний (дробные)
def test_nonequilateral_float():
    t = Triangle(1.2, 3.4, 4.1)
    assert t.triangle_type() == "nonequilateral"
    assert t.perimeter() == pytest.approx(8.7)


# Тест №9: Нулевая сторона
def test_zero_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 3, 4)


# Тест №10: Отрицательная сторона
def test_negative_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-1, 3, 4)


# Тест №11: Все отрицательные
def test_all_negative_sides():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(-3, -3, -3)


# Тест №12: Нарушение неравенства (сумма равна третьей)
def test_triangle_inequality_equal():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 2, 3)


# Тест №13: Нарушение неравенства (сумма меньше третьей)
def test_triangle_inequality_greater():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(1, 1, 100)


# Тест №14: Строка вместо числа
def test_string_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle("x", 3, 4)


# Тест №15: None вместо числа
def test_none_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle(None, 3, 4)


# Тест №16: Список вместо числа
def test_list_side():
    with pytest.raises(IncorrectTriangleSides):
        Triangle([3], 3, 4)
