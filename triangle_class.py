from triangle_func import IncorrectTriangleSides


class Triangle:
    
    def __init__(self, a, b, c):
        # Проверка типов: стороны должны быть числами
        for side in (a, b, c):
            if not isinstance(side, (int, float)):
                raise IncorrectTriangleSides(
                    "Стороны треугольника должны быть числами."
                )

        # Проверка положительности: стороны должны быть положительными
        if a <= 0 or b <= 0 or c <= 0:
            raise IncorrectTriangleSides(
                "Стороны треугольника должны быть положительными числами."
            )

        # Проверка неравенства треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise IncorrectTriangleSides(
                "Сумма двух сторон треугольника должна быть больше третьей стороны."
            )

        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        if self.a == self.b == self.c:
            return "equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "isosceles"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c
