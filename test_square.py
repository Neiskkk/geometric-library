import unittest
from square import area
from square import perimeter 

class SquareTestCase(unittest.TestCase):
   '''Проверяет фунцию нахождения площади для Square с валидным значением'''
   def test_area_normal_value(self):
       res = area(5)
       self.assertEqual(res,  25)
   
   '''Проверяет фунцию нахождения площади для Square с стороной равной 0'''
   def test_area_zero(self):
       res = area(0)
       self.assertEqual(res, 0)

   '''Проверяет фунцию нахождения периметра для Square с стороной равной 0'''
   def test_perimeter_zero(self):
       res = perimeter(0)
       self.assertEqual(res, 0)
       
   '''Проверяет фунцию нахождения периметра для Square с валидным значением'''
   def test_perimeter_normal_value(self):
       res = perimeter(5)
       self.assertEqual(res, 20)

