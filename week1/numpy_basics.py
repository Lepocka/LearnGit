import numpy as np
from typing import Tuple, List


class NumpyBasics:
    # ==================== ARRAY CREATION ====================

    @staticmethod
    def create_arrays_from_lists() -> dict:
        array_1d = np.array([1,2,3,4,5])
        array_2d = np.array([[1,2,3],[4,5,6]])
        arrray_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
        return {
            'array_3d': arrray_3d,
            'array_2d': array_2d,
            'array_1d': array_1d
        }

    @staticmethod
    def create_special_arrays() -> dict:
        zeros = np.zeros((3,3), dtype=int)
        ones = np.ones((2,4), dtype=float)
        identity = np.eye(4)
        arange_arr = np.arange(0,20,2)
        linspace_arr = np.linspace(0,1,10)
        random_uniform = np.random.rand(5,5)
        random_normal = np.random.randn(3,3)
        full_arr = np.full((2,2),7)

        return {
            'zeros': zeros,
            'ones': ones,
            'identity': identity,
            'arange': arange_arr,
            'linspace': linspace_arr,
            'random_uniform': random_uniform,
            'random_normal': random_normal,
            'full': full_arr
        }

    # ==================== ARRAY ATTRIBUTES ====================

    @staticmethod
    def analyze_array_attributes(arr: np.ndarray) -> dict:
        return {
            'shape': arr.shape,
            'ndim': arr.ndim,
            'size': arr.size,
            'dtype': arr.dtype,
            'itemsize': arr.itemsize,
            'nbytes': arr.nbytes
        }

    # ==================== BASIC OPERATIONS ====================

    @staticmethod
    def arithmetic_operations() -> dict:
        a = np.array([1, 2, 3, 4])
        b = np.array([5, 6, 7, 8])

        return {
            'addition': a + b,
            'subtraction': a - b,
            'multiplication': a * b,
            'division': a / b,
            'power': a ** 2,
            'scalar_mult': a * 10,
            'sqrt': np.sqrt(a),
            'exp': np.exp(a),
            'log': np.log(a + 1)
        }

    @staticmethod
    def comparison_operations() -> dict:
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([3, 3, 3, 3, 3])

        return {
            'greater': a > b,
            'equal': a == b,
            'greater_equal': a >= b,
            'indices_gt_3': np.where(a > 3)[0],
            'mask_gt_2': a > 2
        }

    # ==================== RESHAPING ====================

    @staticmethod
    def reshaping_operations() -> dict:
        arr = np.arange(24)

        return {
            'original': arr,
            'reshape_2_12': arr.reshape(2, 12),
            'reshape_4_6': arr.reshape(4, 6),
            'reshape_2_3_4': arr.reshape(2, 3, 4),
            'flatten': arr.reshape(2, 3, 4).flatten(),
            'transpose': arr.reshape(6, 4).T,
            'expand_dims': np.expand_dims(arr, axis=0),
            'squeeze': np.squeeze(np.expand_dims(arr, axis=0))
        }

    # ==================== AGGREGATION OPERATIONS ====================

    @staticmethod
    def aggregation_operations() -> dict:
        np.random.seed(42)
        arr = np.random.randint(1, 101, size=(4, 5))

        return {
            'array': arr,
            'sum_all': np.sum(arr),
            'sum_rows': np.sum(arr, axis=1),
            'sum_cols': np.sum(arr, axis=0),
            'mean': np.mean(arr),
            'median': np.median(arr),
            'std': np.std(arr),
            'var': np.var(arr),
            'min': np.min(arr),
            'max': np.max(arr),
            'argmin': np.argmin(arr),
            'argmax': np.argmax(arr),
            'cumsum': np.cumsum(arr)
        }

    # ==================== UNIVERSAL FUNCTIONS ====================

    @staticmethod
    def universal_functions_demo() -> dict:
        arr = np.linspace(-5, 5, 11)  # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

        return {
            'original': arr,
            'abs': np.abs(arr),
            'sign': np.sign(arr),
            'ceil': np.ceil(arr),
            'floor': np.floor(arr),
            'round': np.round(arr),
            'clip': np.clip(arr, 0, 3),
            'where': np.where(arr > 0, arr, 0) 
        }


# ==================== MAIN DEMO ====================

def main():
    nb = NumpyBasics()

    print("=" * 80)
    print("NUMPY BASICS DEMO")
    print("=" * 80)

    # 1. Array Creation
    print("\n1. ARRAY CREATION FROM LISTS")
    arrays = nb.create_arrays_from_lists()
    print(f"1D array: {arrays['array_1d']}")
    print(f"2D array:\n{arrays['array_2d']}")
    print(f"3D array shape: {arrays['array_3d'].shape}")

    # 2. Special Arrays
    print("\n2. SPECIAL ARRAYS")
    special = nb.create_special_arrays()
    print(f"Zeros:\n{special['zeros']}")
    print(f"Identity:\n{special['identity']}")
    print(f"Arange: {special['arange']}")
    print(f"Linspace: {special['linspace']}")

    # 3. Array Attributes
    print("\n3. ARRAY ATTRIBUTES")
    test_array = np.random.rand(3, 4, 5)
    attrs = nb.analyze_array_attributes(test_array)
    for key, value in attrs.items():
        print(f"{key}: {value}")

    # 4. Arithmetic Operations
    print("\n4. ARITHMETIC OPERATIONS")
    arith = nb.arithmetic_operations()
    print(f"Addition: {arith['addition']}")
    print(f"Power: {arith['power']}")
    print(f"Sqrt: {arith['sqrt']}")

    # 5. Comparison Operations
    print("\n5. COMPARISON OPERATIONS")
    comp = nb.comparison_operations()
    print(f"Greater: {comp['greater']}")
    print(f"Indices where > 3: {comp['indices_gt_3']}")

    # 6. Reshaping
    print("\n6. RESHAPING OPERATIONS")
    reshape = nb.reshaping_operations()
    print(f"Original shape: {reshape['original'].shape}")
    print(f"Reshaped (2, 3, 4): {reshape['reshape_2_3_4'].shape}")
    print(f"Flattened: {reshape['flatten'].shape}")

    # 7. Aggregation
    print("\n7. AGGREGATION OPERATIONS")
    agg = nb.aggregation_operations()
    print(f"Array:\n{agg['array']}")
    print(f"Sum: {agg['sum_all']}")
    print(f"Mean: {agg['mean']:.2f}")
    print(f"Std: {agg['std']:.2f}")
    print(f"Sum by rows: {agg['sum_rows']}")
    print(f"Sum by cols: {agg['sum_cols']}")

    # 8. Universal Functions
    print("\n8. UNIVERSAL FUNCTIONS")
    ufuncs = nb.universal_functions_demo()
    print(f"Original: {ufuncs['original']}")
    print(f"Absolute: {ufuncs['abs']}")
    print(f"Sign: {ufuncs['sign']}")
    print(f"Clipped (0, 3): {ufuncs['clip']}")

    print("\n" + "=" * 80)
    print("DEMO COMPLETED!")
    print("=" * 80)


if __name__ == '__main__':
    main()
