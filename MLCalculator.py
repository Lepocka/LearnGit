class MLCalculator:
    def __init__(self):
        pass
    
    # Середнє арифметичне
    def calculate_mean(self, numbers: list[float]) -> float:
        if len(numbers) == 0:
            return None
        return sum(numbers) / len(numbers)
    
    # Дисперсія
    def calculate_variance(self, numbers: list[float]) -> float:
        if len(numbers) == 0:
            return None
        
        mean = self.calculate_mean(numbers)
        variance = 0

        for num in numbers:
            variance += (num - mean) ** 2
        variance /= len(numbers)
        return variance

    # Стандартне відхилення
    def calculate_standard_deviation(self, numbers: list[float]) -> float:
        variance = self.calculate_variance(numbers)
        if variance is None:
            return None
        return variance ** 0.5
    
    # Скалярний добуток векторів
    def calculate_dot_product(self, vector1: list[float], vector2: list[float]) -> float:
        if len(vector1) != len(vector2):
            print("Vectors must be of the same length")
            return None
        
        dot_product = 0

        for i in range(len(vector1)):
            dot_product += vector1[i] * vector2[i]
            
        return dot_product

    # Евклідова відстань між двома точками
    def calculate_euclidean_distance(self, point1: list[float], point2: list[float]) -> float:
        if len(point1) != len(point2):
            print("Points must be of the same dimension")
            return None
        
        distance = 0
        for i in range(len(point1)):
            distance += (point1[i] - point2[i]) ** 2

        distance **= 0.5
        return distance
    