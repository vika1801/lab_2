class IncorrectTriangleSides(Exception):
    pass


def get_triangle_type(a, b, c):
    # Проверка: стороны должны быть числами
    for side in (a, b, c):
        if not isinstance(side, (int, float)):
            raise IncorrectTriangleSides(
                "Стороны треугольника должны быть числами."
            )

    # Проверка: стороны должны быть положительными
    if a <= 0 or b <= 0 or c <= 0:
        raise IncorrectTriangleSides(
            "Стороны треугольника должны быть положительными числами."
        )

    # Проверка неравенства треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        raise IncorrectTriangleSides(
            "Сумма двух сторон треугольника должна быть больше третьей стороны."
        )

    # Определение типа треугольника
    if a == b == c:
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    else:
        return "nonequilateral"
