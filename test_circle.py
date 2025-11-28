import unittest
import math
from circle import area
from circle import perimeter 

class CircleTestCase(unittest.TestCase):
   '''Проверяет фунцию нахождения площади для Circle с валидным значением'''
   def test_area_normal_value(self):
       res = area(5)
       self.assertEqual(res, 5 * 5 * math.pi)
       
   '''Проверяет фунцию нахождения площади для Circle с радиусом равным 0'''
   def test_area_zero(self):
       res = area(0)
       self.assertEqual(res, 0)

   '''Проверяет фунцию нахождения периметра для Circle с радиусом равным 0'''
   def test_perimeter_zero(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       
   '''Проверяет фунцию нахождения площади для Circle с валидным значением'''
   def test_perimeter_normal_value(self):
       res = perimeter(5)
       self.assertEqual(res, 10 * math.pi)


