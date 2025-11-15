import unittest
import math

import circle
import square
import rectangle
import triangle


class CircleTest(unittest.TestCase):
    """Тесты для модуля circle.py - проверка функций работы с кругом"""
    
    def test_circle_area_positive_radius(self):
        """Проверяет вычисление площади круга с положительным радиусом"""
        # Площадь круга: π * r² = π * 2² = 4π ≈ 12.566
        self.assertAlmostEqual(circle.area(2), math.pi * 4, places=5)
    
    def test_circle_area_zero_radius(self):
        """Проверяет вычисление площади круга с нулевым радиусом"""
        # Площадь круга с радиусом 0 должна быть 0
        self.assertEqual(circle.area(0), 0)
    
    def test_circle_area_large_radius(self):
        """Проверяет вычисление площади круга с большим радиусом"""
        # Площадь круга: π * 10² = 100π ≈ 314.159
        self.assertAlmostEqual(circle.area(10), math.pi * 100, places=5)
    
    def test_circle_area_float_radius(self):
        """Проверяет вычисление площади круга с дробным радиусом"""
        # Площадь круга: π * 1.5² = 2.25π ≈ 7.069
        self.assertAlmostEqual(circle.area(1.5), math.pi * 2.25, places=5)
    
    def test_circle_perimeter_positive_radius(self):
        """Проверяет вычисление периметра (длины окружности) с положительным радиусом"""
        # Периметр окружности: 2 * π * r = 2 * π * 2 = 4π ≈ 12.566
        self.assertAlmostEqual(circle.perimeter(2), 2 * math.pi * 2, places=5)
    
    def test_circle_perimeter_zero_radius(self):
        """Проверяет вычисление периметра окружности с нулевым радиусом"""
        # Периметр окружности с радиусом 0 должен быть 0
        self.assertEqual(circle.perimeter(0), 0)
    
    def test_circle_perimeter_large_radius(self):
        """Проверяет вычисление периметра окружности с большим радиусом"""
        # Периметр окружности: 2 * π * 10 = 20π ≈ 62.832
        self.assertAlmostEqual(circle.perimeter(10), 2 * math.pi * 10, places=5)
    
    def test_circle_perimeter_float_radius(self):
        """Проверяет вычисление периметра окружности с дробным радиусом"""
        # Периметр окружности: 2 * π * 1.5 = 3π ≈ 9.425
        self.assertAlmostEqual(circle.perimeter(1.5), 2 * math.pi * 1.5, places=5)

class SquareTest(unittest.TestCase):
    """Тесты для модуля square.py - проверка функций работы с квадратом"""
    
    def test_square_area_positive_side(self):
        """Проверяет вычисление площади квадрата с положительной стороной"""
        # Площадь квадрата: a² = 5² = 25
        self.assertEqual(square.area(5), 25)
    
    def test_square_area_zero_side(self):
        """Проверяет вычисление площади квадрата с нулевой стороной"""
        # Площадь квадрата со стороной 0 должна быть 0
        self.assertEqual(square.area(0), 0)
    
    def test_square_area_one_side(self):
        """Проверяет вычисление площади квадрата со стороной 1"""
        # Площадь квадрата: 1² = 1
        self.assertEqual(square.area(1), 1)
    
    def test_square_area_large_side(self):
        """Проверяет вычисление площади квадрата с большой стороной"""
        # Площадь квадрата: 10² = 100
        self.assertEqual(square.area(10), 100)
    
    def test_square_perimeter_positive_side(self):
        """Проверяет вычисление периметра квадрата с положительной стороной"""
        # Периметр квадрата: 4 * a = 4 * 5 = 20
        self.assertEqual(square.perimeter(5), 20)
    
    def test_square_perimeter_zero_side(self):
        """Проверяет вычисление периметра квадрата с нулевой стороной"""
        # Периметр квадрата со стороной 0 должен быть 0
        self.assertEqual(square.perimeter(0), 0)
    
    def test_square_perimeter_one_side(self):
        """Проверяет вычисление периметра квадрата со стороной 1"""
        # Периметр квадрата: 4 * 1 = 4
        self.assertEqual(square.perimeter(1), 4)
    
    def test_square_perimeter_large_side(self):
        """Проверяет вычисление периметра квадрата с большой стороной"""
        # Периметр квадрата: 4 * 10 = 40
        self.assertEqual(square.perimeter(10), 40)


class RectangleTest(unittest.TestCase):
    """Тесты для модуля rectangle.py - проверка функций работы с прямоугольником"""
    
    def test_rectangle_area_positive_side(self):
        """Проверяет вычисление площади прямоугольника с положительной стороной"""
        # Площадь: a² = 4² = 16 (примечание: функция принимает один параметр)
        self.assertEqual(rectangle.area(4), 16)
    
    def test_rectangle_area_zero_side(self):
        """Проверяет вычисление площади прямоугольника с нулевой стороной"""
        # Площадь со стороной 0 должна быть 0
        self.assertEqual(rectangle.area(0), 0)
    
    def test_rectangle_area_one_side(self):
        """Проверяет вычисление площади прямоугольника со стороной 1"""
        # Площадь: 1² = 1
        self.assertEqual(rectangle.area(1), 1)
    
    def test_rectangle_area_large_side(self):
        """Проверяет вычисление площади прямоугольника с большой стороной"""
        # Площадь: 7² = 49
        self.assertEqual(rectangle.area(7), 49)
    
    def test_rectangle_perimeter_positive_side(self):
        """Проверяет вычисление периметра прямоугольника с положительной стороной"""
        # Периметр: 4 * a = 4 * 4 = 16 (примечание: функция принимает один параметр)
        self.assertEqual(rectangle.perimeter(4), 16)
    
    def test_rectangle_perimeter_zero_side(self):
        """Проверяет вычисление периметра прямоугольника с нулевой стороной"""
        # Периметр со стороной 0 должен быть 0
        self.assertEqual(rectangle.perimeter(0), 0)
    
    def test_rectangle_perimeter_one_side(self):
        """Проверяет вычисление периметра прямоугольника со стороной 1"""
        # Периметр: 4 * 1 = 4
        self.assertEqual(rectangle.perimeter(1), 4)
    
    def test_rectangle_perimeter_large_side(self):
        """Проверяет вычисление периметра прямоугольника с большой стороной"""
        # Периметр: 4 * 7 = 28
        self.assertEqual(rectangle.perimeter(7), 28)


class TriangleTest(unittest.TestCase):
    """Тесты для модуля triangle.py - проверка функций работы с треугольником"""
    
    def test_triangle_area_positive_values(self):
        """Проверяет вычисление площади треугольника с положительными значениями"""
        # Площадь треугольника: (a * h) / 2 = (6 * 4) / 2 = 12
        self.assertEqual(triangle.area(6, 4), 12)
    
    def test_triangle_area_zero_base(self):
        """Проверяет вычисление площади треугольника с нулевым основанием"""
        # Площадь треугольника с основанием 0 должна быть 0
        self.assertEqual(triangle.area(0, 5), 0)
    
    def test_triangle_area_zero_height(self):
        """Проверяет вычисление площади треугольника с нулевой высотой"""
        # Площадь треугольника с высотой 0 должна быть 0
        self.assertEqual(triangle.area(5, 0), 0)
    
    def test_triangle_area_one_values(self):
        """Проверяет вычисление площади треугольника со сторонами 1"""
        # Площадь треугольника: (1 * 1) / 2 = 0.5
        self.assertEqual(triangle.area(1, 1), 0.5)
    
    def test_triangle_area_large_values(self):
        """Проверяет вычисление площади треугольника с большими значениями"""
        # Площадь треугольника: (10 * 8) / 2 = 40
        self.assertEqual(triangle.area(10, 8), 40)
    
    def test_triangle_area_float_values(self):
        """Проверяет вычисление площади треугольника с дробными значениями"""
        # Площадь треугольника: (5.5 * 3.0) / 2 = 8.25
        self.assertEqual(triangle.area(5.5, 3.0), 8.25)
    
    def test_triangle_perimeter_positive_sides(self):
        """Проверяет вычисление периметра треугольника с положительными сторонами"""
        # Периметр треугольника: a + b + c = 3 + 4 + 5 = 12
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
    
    def test_triangle_perimeter_zero_sides(self):
        """Проверяет вычисление периметра треугольника с нулевыми сторонами"""
        # Периметр треугольника: 0 + 0 + 0 = 0
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
    
    def test_triangle_perimeter_one_side_zero(self):
        """Проверяет вычисление периметра треугольника с одной нулевой стороной"""
        # Периметр треугольника: 5 + 0 + 3 = 8
        self.assertEqual(triangle.perimeter(5, 0, 3), 8)
    
    def test_triangle_perimeter_equal_sides(self):
        """Проверяет вычисление периметра равностороннего треугольника"""
        # Периметр равностороннего треугольника: 5 + 5 + 5 = 15
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)
    
    def test_triangle_perimeter_large_sides(self):
        """Проверяет вычисление периметра треугольника с большими сторонами"""
        # Периметр треугольника: 10 + 12 + 15 = 37
        self.assertEqual(triangle.perimeter(10, 12, 15), 37)
    
    def test_triangle_perimeter_float_sides(self):
        """Проверяет вычисление периметра треугольника с дробными сторонами"""
        # Периметр треугольника: 2.5 + 3.5 + 4.0 = 10.0
        self.assertEqual(triangle.perimeter(2.5, 3.5, 4.0), 10.0)


if __name__ == '__main__':
    unittest.main()
