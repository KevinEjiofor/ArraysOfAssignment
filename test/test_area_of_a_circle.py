import unittest
from  area_of_a_circle import circle
from math import pi

class  TestAreaFunction(unittest.TestCase):
    def test_area_test_function(self):
        self.assertAlmostEqual(circle(1), pi)
        self.assertAlmostEqual(circle(0),0)
        self.assertAlmostEqual(circle(2), pi * 2 **2)

    def test_values(self):
        self.assertRaises(ValueError, circle, -1)
        self.assertRaises(ValueError, circle, -5)

    def test_radius_type(self):
        self.assertRaises(TypeError, circle, True)
        self.assertRaises(TypeError,circle, 2 + 5j)

