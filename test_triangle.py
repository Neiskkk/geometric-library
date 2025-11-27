import unittest
from triangle import area
from triangle import perimeter 

class TriangleTestCase(unittest.TestCase):
    def test_area_normal_value(self):
       res = area(4, 5)
       self.assertEqual(res,  10)
       
    def test_area_zero(self):
       res = area(4, 0)
       self.assertEqual(res, 0)

    def test_perimeter_normal_value(self):
       res = perimeter(3, 4, 5)
       self.assertEqual(res, 12)

