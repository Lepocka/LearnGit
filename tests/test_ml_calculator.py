import unittest
from ml_calculator import MLCalculator
import math

class TestMLCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = MLCalculator()

    def test_calculate_mean(self):
        self.assertAlmostEqual(self.calculator.calculate_mean([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(self.calculator.calculate_mean([-1, 0, 1]), 0.0)
        self.assertAlmostEqual(self.calculator.calculate_mean([10]), 10.0)
        self.assertAlmostEqual(self.calculator.calculate_mean([999999999, 1000000001]), 1000000000.0)
        self.assertAlmostEqual(self.calculator.calculate_mean([-9, -4, -3, -1.3, -2]), -3.86)
        self.assertRaises(TypeError, self.calculator.calculate_mean, [1, 'a', 3])
        self.assertRaises(ValueError, self.calculator.calculate_mean, [])
    
    def test_calculate_variance(self):
        self.assertAlmostEqual(self.calculator.calculate_variance([1, 2, 3, 4, 5]), 2.0)
        self.assertAlmostEqual(self.calculator.calculate_variance([-1, 0, 1]), 2/3)
        self.assertAlmostEqual(self.calculator.calculate_variance([10]), 0.0)
        self.assertAlmostEqual(self.calculator.calculate_variance([999999999, 1000000001]), 1.0)
        self.assertAlmostEqual(self.calculator.calculate_variance([-9, -4, -3, -1.3, -2]), 7.4384)
        self.assertRaises(TypeError, self.calculator.calculate_mean, [1, 'a', 3])
        self.assertRaises(ValueError, self.calculator.calculate_variance, [])
    
    def test_calculate_standard_deviation(self):
        self.assertAlmostEqual(self.calculator.calculate_standard_deviation([1, 2, 3, 4, 5]), math.sqrt(2.0))
        self.assertAlmostEqual(self.calculator.calculate_standard_deviation([-1, 0, 1]), math.sqrt(2/3))
        self.assertAlmostEqual(self.calculator.calculate_standard_deviation([10]), 0.0)
        self.assertAlmostEqual(self.calculator.calculate_standard_deviation([999999999, 1000000001]), 1.0)
        self.assertAlmostEqual(self.calculator.calculate_standard_deviation([-9, -4, -3, -1.3, -2]), math.sqrt(7.4384))
        self.assertRaises(TypeError, self.calculator.calculate_standard_deviation, [1, 'a', 3])
        self.assertRaises(ValueError, self.calculator.calculate_standard_deviation, [])

    def test_calculate_dot_product(self):
        self.assertEqual(self.calculator.calculate_dot_product([1, 2, 3, 7], [4, 5, 6, 1]), 39)
        self.assertEqual(self.calculator.calculate_dot_product([-1, 2, 1], [1, 2, -1]), 2)
        self.assertEqual(self.calculator.calculate_dot_product([0], [1]), 0)
        self.assertEqual(self.calculator.calculate_dot_product([1.5, 2.5], [4.0, 5.0]), 18.5)
        self.assertEqual(self.calculator.calculate_dot_product([9999999999], [1]), 9999999999)
        self.assertRaises(TypeError, self.calculator.calculate_dot_product, [1, 'a'], [1, 2])
        self.assertRaises(TypeError, self.calculator.calculate_dot_product, [1, 2], [1, 'b'])
        self.assertRaises(ValueError, self.calculator.calculate_dot_product, [], [])
        self.assertRaises(ValueError, self.calculator.calculate_dot_product, [1, 2], [1, 2, 3])
    
    def test_calculate_euclidean_distance(self):
        self.assertAlmostEqual(self.calculator.calculate_euclidean_distance([1, 2, 6], [4, 6, 2]), math.sqrt(41))
        self.assertAlmostEqual(self.calculator.calculate_euclidean_distance([-1, -1], [1, 1]), math.sqrt(8))
        self.assertAlmostEqual(self.calculator.calculate_euclidean_distance([0], [0]), 0.0)
        self.assertAlmostEqual(self.calculator.calculate_euclidean_distance([1.5], [4.0]), math.sqrt(6.25))
        self.assertAlmostEqual(self.calculator.calculate_euclidean_distance([9999999999], [0]), 9999999999.0)
        self.assertRaises(TypeError, self.calculator.calculate_euclidean_distance, [1, 'a'], [1, 2])
        self.assertRaises(TypeError, self.calculator.calculate_euclidean_distance, [1, 2], [1, 'b'])
        self.assertRaises(ValueError, self.calculator.calculate_euclidean_distance, [], [])
        self.assertRaises(ValueError, self.calculator.calculate_euclidean_distance, [1, 2], [1, 2, 3])
    
if __name__ == '__main__':
    unittest.main()
