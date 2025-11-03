import math

class MLCalculator:
    def __init__(self):
        pass
    
    # Середнє арифметичне
    def calculate_mean(self, numbers: list[float]) -> float:
        '''
        Calculates the mean of a list of numbers.

        Parameters
        ----------
            numbers : list[float]
                A list of numerical values
        Returns
        -------
            float
                The mean of the input numbers
        Raises
        ------
            ValueError
                If the input list is empty
        Examples
        --------
            >>> calculate_mean([1, 2, 3, 4, 5])
            3.0
        '''
        if len(numbers) == 0:
            raise ValueError("The list must be not empty")
        try:
            return sum(numbers) / len(numbers)
        except TypeError:
            raise TypeError("The list must contain only numerical values")
    
    # Дисперсія
    def calculate_variance(self, numbers: list[float]) -> float:
        '''
        Calculates the variance of a list of numbers.

        Parameters
        ----------
            numbers : list[float]
                A list of numerical values
        Returns
        -------
            float
                The variance of the input numbers
        Raises
        ------
            ValueError
                If the input list is empty
        Examples
        --------
            >>> calculate_variance([1, 2, 3, 4, 5, 6, 7])
            4.0
        '''
        mean = self.calculate_mean(numbers)

        return sum((num - mean) ** 2 for num in numbers) / len(numbers)

    # Стандартне відхилення
    def calculate_standard_deviation(self, numbers: list[float]) -> float:
        '''
        Calculates the standard deviation of a list of numbers.

        Parameters
        ----------
            numbers : list[float]
                A list of numerical values
        Returns
        -------
            float
                The standard deviation of the input numbers
        Raises
        ------
            ValueError
                If the input list is empty
        Examples
        --------
            >>> calculate_standard_deviation([1, 2, 3, 4, 5, 6, 7])
            2.0
        '''
        variance = self.calculate_variance(numbers)
        return math.sqrt(variance)
    
    # Скалярний добуток векторів
    def calculate_dot_product(self, vector1: list[float], vector2: list[float]) -> float:
        '''
        Calculates the standard deviation of a list of numbers.

        Parameters
        ----------
            vector1 : list[float]
                A list of numerical values. First vector coordinates
            vector2 : list[float]
                A list of numerical values. Second vector coordinates
        Returns
        -------
            float
                The dot product of the input vectors
        Raises
        ------
            ValueError
                If the input lists are of different lengths
        Examples
        --------
            >>> calculate_dot_product([1, 2, 3], [4, 5, 6])
            32
        '''
        if len(vector1) != len(vector2):
            raise ValueError("Vectors must be of the same length")
        
        if len(vector1) == 0 or len(vector2) == 0:
            raise ValueError("Vectors must be not empty")
        try:
            return sum(a * b for a, b in zip(vector1, vector2))
        except TypeError:
            raise TypeError("The lists must contain only numerical values")
    # Евклідова відстань між двома точками
    def calculate_euclidean_distance(self, point1: list[float], point2: list[float]) -> float:
        '''
        Calculates the standard deviation of a list of numbers.

        Parameters
        ----------
            point1 : list[float]
                A list of numerical values. First point coordinates
            point2 : list[float]
                A list of numerical values. Second point coordinates
        Returns
        -------
            float
                The euclidean_distance of the input points
        Raises
        ------
            ValueError
                If the input lists are of different lengths
        Examples
        --------
            >>> calculate_euclidean_distance([1, 2], [4, 6])
            5.0            
        '''
        if len(point1) != len(point2):
            raise ValueError("Points must be of the same dimension")
        if len(point1) == 0 or len(point2) == 0:
            raise ValueError("Points must be not empty")
        try:
            return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
        except TypeError:
            raise TypeError("The lists must contain only numerical values")
        