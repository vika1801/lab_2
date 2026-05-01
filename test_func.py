import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestGetTriangleTypePositive(unittest.TestCase):
    #1
    def test_equilateral_integers(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")
    
    #2
    def test_equilateral_floats(self):
        self.assertEqual(get_triangle_type(1.5, 1.5, 1.5), "equilateral")

    #3
    def test_equilateral_minimal(self):
        self.assertEqual(get_triangle_type(1, 1, 1), "equilateral")

    #4
    def test_isosceles_ab_equal(self):
        self.assertEqual(get_triangle_type(5, 5, 3), "isosceles")

    #5
    def test_isosceles_bc_equal(self):
        self.assertEqual(get_triangle_type(4, 6, 6), "isosceles")

    #6
    def test_isosceles_ac_equal(self):
        self.assertEqual(get_triangle_type(7, 5, 7), "isosceles")

    #7
    def test_nonequilateral_integers(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")

    #8
    def test_nonequilateral_floats(self):
        self.assertEqual(get_triangle_type(1.2, 3.4, 4.1), "nonequilateral")


class TestGetTriangleTypeNegative(unittest.TestCase):

    #9
    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 3, 4)

    #10
    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 3, 4)

    #11
    def test_all_negative_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-3, -3, -3)

    #12
    def test_triangle_inequality_equal(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 2, 3)

    #13
    def test_triangle_inequality_greater(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 10)

    #14
    def test_string_argument(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("abc", 3, 4)

    #15
    def test_none_argument(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(None, 3, 4)

    #16
    def test_list_argument(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type([3], 3, 4)


if __name__ == "__main__":
    unittest.main()
