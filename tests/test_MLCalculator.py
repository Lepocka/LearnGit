import unittest
from MLCalculator import MLCalculator

class TestMLCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = MLCalculator()

    def test_calculate_mean(self):
        self.assertAlmostEqual(self.calculator.calculate_mean([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(self.calculator.calculate_mean([-1, 0, 1]), 0.0)
        self.assertAlmostEqual(self.calculator.calculate_mean([10]), 10.0)
        self.assertEqual(self.calculator.calculate_mean([]), None)
    
    def test_calculate_variance(self):
        self.assertAlmostEqual(self.calculator.calculate_variance([1, 2, 3, 4, 5]), 2.0)
        self.assertAlmostEqual(self.calculator.calculate_variance([-1, 0, 1]), 2/3)
        self.assertAlmostEqual(self.calculator.calculate_variance([10]), 0.0)
        self.assertEqual(self.calculator.calculate_variance([]), None)
    
    def test_calculate_standard_deviation(self):
        self.assertAlmostEqual(self.calculator.calculate_standard_deviation([1, 2, 3, 4, 5]), 2.0 ** 0.5)
        self.assertAlmostEqual(self.calculator.calculate_standard_deviation([-1, 0, 1]), (2/3) ** 0.5)
        self.assertAlmostEqual(self.calculator.calculate_standard_deviation([10]), 0.0)
        self.assertEqual(self.calculator.calculate_standard_deviation([]), None)

    def test_calculate_dot_product(self):
        self.assertEqual(self.calculator.calculate_dot_product([1, 2, 3], [4, 5, 6]), 32)
        self.assertEqual(self.calculator.calculate_dot_product([-1, 2, 1], [1, 2, -1]), 2)
        self.assertEqual(self.calculator.calculate_dot_product([1, 2], [1, 2, 3]), None)
    
    def test_calculate_euclidean_distance(self):
        self.assertAlmostEqual(self.calculator.calculate_euclidean_distance([1, 2], [4, 6]), 5.0)
        self.assertAlmostEqual(self.calculator.calculate_euclidean_distance([-1, -1], [1, 1]), (8) ** 0.5)
        self.assertEqual(self.calculator.calculate_euclidean_distance([1, 2], [1, 2, 3]), None)
    
if __name__ == '__main__':
    unittest.main()