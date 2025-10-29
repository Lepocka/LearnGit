from enum import Enum

class Operator(Enum):
    ADDITION = '+'
    SUBTRACTION = "-"
    MULTIPLICATION = '*'
    DIVISION = "/"

class InputValidator:
    def __init__(self, input_value: str = '') -> None:
        self.input_value = input_value
    
    def set_input_value(self, input_value) -> None:
        self.input_value = input_value

    def is_number(self, input_number) -> bool:
        try:
            float(input_number)
            return True
        except ValueError:
            return False

    def get_correct_input_number(self) -> str:
        input_value = self.input_value
        
        while not (self.is_number(input_value)):
            print('Incorrect input')
            input_value = input('Input number again: ')

        return input_value
    
    def get_correct_input_operator(self) -> Operator:
        input_value = self.input_value

        while not input_value in [op.value for op in Operator]:
            print('Incorrect input')
            input_value = input('Choose operator again: ')
        
        return Operator(input_value)
    

class Calculator:
    def __init__(self, operator, first_num, second_num):
        self.operator = operator
        self.first_num = first_num
        self.second_num = second_num
    
    def addition(self) -> float:
        return float(self.first_num) + float(self.second_num)
    
    def subtraction(self) -> float:
        return float(self.first_num) - float(self.second_num)
    
    def multiplication(self) -> float:
        return float(self.first_num) * float(self.second_num)
    
    def division(self) -> float:
        try:
            return float(self.first_num) / float(self.second_num)
        except ZeroDivisionError:
            return None
    
    def calculating(self) -> float:
        if self.operator == Operator.ADDITION:
            return self.addition()
        elif self.operator == Operator.SUBTRACTION:
            return self.subtraction()
        elif self.operator == Operator.MULTIPLICATION:
            return self.multiplication()
        elif self.operator == Operator.DIVISION:
            return self.division()


class Main:
    def __init__(self) -> None:
        pass

    def operator_instruction(self) -> None:
        print(f'Addition:       {Operator.ADDITION.value}')
        print(f'Substraction:   {Operator.SUBTRACTION.value}')
        print(f'Multiplication: {Operator.MULTIPLICATION.value}')
        print(f'Division:       {Operator.DIVISION.value}')

    def run(self) -> None:
        input_value_validator = InputValidator()

        input_value_validator.set_input_value(input('Input first number: '))

        first_number = input_value_validator.get_correct_input_number()

        input_value_validator.set_input_value(input('Input second number: '))

        second_number = input_value_validator.get_correct_input_number()

        self.operator_instruction()

        input_value_validator.set_input_value(input('Choose operator: '))

        input_operator = input_value_validator.get_correct_input_operator()

        calculator = Calculator(input_operator, first_number, second_number)

        result = calculator.calculating()

        if result == None:
            print('Error: Division by zero')
            print('Try again')
            self.run()
        else:
            print(f'Result: {result}')


if __name__ == '__main__':
    app = Main()
    app.run()
