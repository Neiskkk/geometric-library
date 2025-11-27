import unittest
from rectangle import area
from rectangle import perimeter 

class RectangleTestCase(unittest.TestCase):
    def test_area_normal_value(self):
       res = area(3, 5)
       self.assertEqual(res,  15)
       
    def test_area_zero(self):
       res = area(3, 0)
       self.assertEqual(res, 0)
       
    def test_perimeter_normal_value(self):
       res = perimeter(3, 5)
       self.assertEqual(res, 16)

