import unittest
import numpy as np
from week1.numpy_basics import NumpyBasics


class TestNumpyBasics(unittest.TestCase):

    def setUp(self):
        self.nb = NumpyBasics()
        np.random.seed(42) 

    # ==================== ARRAY CREATION TESTS ====================

    def test_create_arrays_from_lists_1d(self):
        arrays = self.nb.create_arrays_from_lists()
        arr = arrays['array_1d']

        self.assertIsInstance(arr, np.ndarray)
        self.assertEqual(arr.shape, (5,))
        np.testing.assert_array_equal(arr, [1, 2, 3, 4, 5])

    def test_create_arrays_from_lists_2d(self):
        arrays = self.nb.create_arrays_from_lists()
        arr = arrays['array_2d']

        self.assertEqual(arr.shape, (2, 3))
        np.testing.assert_array_equal(arr, [[1, 2, 3], [4, 5, 6]])

    def test_create_arrays_from_lists_3d(self):
        arrays = self.nb.create_arrays_from_lists()
        arr = arrays['array_3d']

        self.assertEqual(arr.shape, (2, 2, 2))
        self.assertEqual(arr.ndim, 3)

    def test_create_special_arrays_zeros(self):
        arrays = self.nb.create_special_arrays()
        zeros = arrays['zeros']

        self.assertEqual(zeros.shape, (3, 3))
        self.assertEqual(zeros.dtype, np.int64)
        np.testing.assert_array_equal(zeros, np.zeros((3, 3)))

    def test_create_special_arrays_ones(self):
        arrays = self.nb.create_special_arrays()
        ones = arrays['ones']

        self.assertEqual(ones.shape, (2, 4))
        self.assertEqual(ones.dtype, np.float64)
        np.testing.assert_array_equal(ones, np.ones((2, 4)))

    def test_create_special_arrays_identity(self):
        arrays = self.nb.create_special_arrays()
        identity = arrays['identity']

        self.assertEqual(identity.shape, (4, 4))
        np.testing.assert_array_equal(identity, np.eye(4))

    def test_create_special_arrays_arange(self):
        arrays = self.nb.create_special_arrays()
        arange_arr = arrays['arange']

        expected = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
        np.testing.assert_array_equal(arange_arr, expected)

    def test_create_special_arrays_linspace(self):
        arrays = self.nb.create_special_arrays()
        linspace_arr = arrays['linspace']

        self.assertEqual(len(linspace_arr), 10)
        self.assertAlmostEqual(linspace_arr[0], 0.0)
        self.assertAlmostEqual(linspace_arr[-1], 1.0)

    def test_create_special_arrays_random_shape(self):
        arrays = self.nb.create_special_arrays()

        self.assertEqual(arrays['random_uniform'].shape, (5, 5))
        self.assertEqual(arrays['random_normal'].shape, (3, 3))

    def test_create_special_arrays_full(self):
        arrays = self.nb.create_special_arrays()
        full_arr = arrays['full']

        self.assertEqual(full_arr.shape, (2, 2))
        np.testing.assert_array_equal(full_arr, np.full((2, 2), 7))

    # ==================== ARRAY ATTRIBUTES TESTS ====================

    def test_analyze_array_attributes_shape(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        attrs = self.nb.analyze_array_attributes(arr)

        self.assertEqual(attrs['shape'], (2, 3))

    def test_analyze_array_attributes_ndim(self):
        arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        attrs = self.nb.analyze_array_attributes(arr)

        self.assertEqual(attrs['ndim'], 3)

    def test_analyze_array_attributes_size(self):
        arr = np.array([[1, 2, 3], [4, 5, 6]])
        attrs = self.nb.analyze_array_attributes(arr)

        self.assertEqual(attrs['size'], 6)

    def test_analyze_array_attributes_dtype(self):
        arr = np.array([1.5, 2.5, 3.5])
        attrs = self.nb.analyze_array_attributes(arr)

        self.assertEqual(attrs['dtype'], np.float64)

    # ==================== ARITHMETIC OPERATIONS TESTS ====================

    def test_arithmetic_operations_addition(self):
        ops = self.nb.arithmetic_operations()
        expected = np.array([6, 8, 10, 12])
        np.testing.assert_array_equal(ops['addition'], expected)

    def test_arithmetic_operations_multiplication(self):
        ops = self.nb.arithmetic_operations()
        expected = np.array([5, 12, 21, 32])
        np.testing.assert_array_equal(ops['multiplication'], expected)

    def test_arithmetic_operations_power(self):
        ops = self.nb.arithmetic_operations()
        expected = np.array([1, 4, 9, 16])
        np.testing.assert_array_equal(ops['power'], expected)

    def test_arithmetic_operations_scalar_mult(self):
        ops = self.nb.arithmetic_operations()
        expected = np.array([10, 20, 30, 40])
        np.testing.assert_array_equal(ops['scalar_mult'], expected)

    def test_arithmetic_operations_sqrt(self):
        ops = self.nb.arithmetic_operations()
        expected = np.array([1, np.sqrt(2), np.sqrt(3), 2])
        np.testing.assert_array_almost_equal(ops['sqrt'], expected)

    # ==================== COMPARISON OPERATIONS TESTS ====================

    def test_comparison_operations_greater(self):
        ops = self.nb.comparison_operations()
        expected = np.array([False, False, False, True, True])
        np.testing.assert_array_equal(ops['greater'], expected)

    def test_comparison_operations_equal(self):
        ops = self.nb.comparison_operations()
        expected = np.array([False, False, True, False, False])
        np.testing.assert_array_equal(ops['equal'], expected)

    def test_comparison_operations_indices(self):
        ops = self.nb.comparison_operations()
        expected = np.array([3, 4])
        np.testing.assert_array_equal(ops['indices_gt_3'], expected)

    def test_comparison_operations_mask(self):
        ops = self.nb.comparison_operations()
        expected = np.array([False, False, True, True, True])
        np.testing.assert_array_equal(ops['mask_gt_2'], expected)

    # ==================== RESHAPING TESTS ====================

    def test_reshaping_original(self):
        ops = self.nb.reshaping_operations()
        expected = np.arange(24)
        np.testing.assert_array_equal(ops['original'], expected)

    def test_reshaping_2_12(self):
        ops = self.nb.reshaping_operations()
        self.assertEqual(ops['reshape_2_12'].shape, (2, 12))

    def test_reshaping_4_6(self):
        ops = self.nb.reshaping_operations()
        self.assertEqual(ops['reshape_4_6'].shape, (4, 6))

    def test_reshaping_2_3_4(self):
        ops = self.nb.reshaping_operations()
        self.assertEqual(ops['reshape_2_3_4'].shape, (2, 3, 4))

    def test_reshaping_flatten(self):
        ops = self.nb.reshaping_operations()
        self.assertEqual(ops['flatten'].shape, (24,))
        self.assertEqual(ops['flatten'].ndim, 1)

    def test_reshaping_transpose(self):
        ops = self.nb.reshaping_operations()
        self.assertEqual(ops['transpose'].shape, (4, 6))

    # ==================== AGGREGATION TESTS ====================

    def test_aggregation_sum_shape(self):
        ops = self.nb.aggregation_operations()

        self.assertIsInstance(ops['sum_all'], (int, np.integer, float, np.floating))
        self.assertEqual(ops['sum_rows'].shape, (4,))
        self.assertEqual(ops['sum_cols'].shape, (5,))

    def test_aggregation_mean_in_range(self):
        ops = self.nb.aggregation_operations()

        self.assertGreater(ops['mean'], 0)
        self.assertLess(ops['mean'], 101)

    def test_aggregation_min_max(self):
        ops = self.nb.aggregation_operations()

        self.assertLessEqual(ops['min'], ops['max'])
        self.assertGreaterEqual(ops['min'], 1)
        self.assertLessEqual(ops['max'], 100)

    def test_aggregation_argmin_argmax(self):
        ops = self.nb.aggregation_operations()
        arr = ops['array'].flatten()

        self.assertEqual(arr[ops['argmin']], ops['min'])
        self.assertEqual(arr[ops['argmax']], ops['max'])

    def test_aggregation_cumsum_shape(self):
        ops = self.nb.aggregation_operations()

        self.assertEqual(ops['cumsum'].shape, (20,))  

    # ==================== UNIVERSAL FUNCTIONS TESTS ====================

    def test_ufuncs_abs(self):
        ops = self.nb.universal_functions_demo()

        self.assertTrue(np.all(ops['abs'] >= 0))

    def test_ufuncs_sign(self):
        ops = self.nb.universal_functions_demo()

        self.assertTrue(np.all(np.isin(ops['sign'], [-1, 0, 1])))

    def test_ufuncs_clip(self):
        ops = self.nb.universal_functions_demo()

        self.assertTrue(np.all(ops['clip'] >= 0))
        self.assertTrue(np.all(ops['clip'] <= 3))

    def test_ufuncs_where(self):
        ops = self.nb.universal_functions_demo()

        self.assertTrue(np.all(ops['where'] >= 0))


if __name__ == '__main__':
    unittest.main(verbosity=2)