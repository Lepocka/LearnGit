class input_validator:
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
    
    def get_correct_input_operator(self) -> str:
        input_value = self.input_value

        while not self.is_number(input_value) or not float(input_value) in [0, 1, 2, 3]:
            print('Incorrect input')
            input_value = input('Choose operator again: ')
        
        return input_value
    

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
        if float(self.operator) == 0:
            return self.addition()
        elif float(self.operator) == 1:
            return self.subtraction()
        elif float(self.operator) == 2:
            return self.multiplication()
        elif float(self.operator) == 3:
            return self.division()


class main:
    def __init__(self) -> None:
        pass

    def operator_instruction(self) -> None:
        print('0: +')
        print('1: -')
        print('2: *')
        print('3: /')

    def run(self) -> None:
        input_value_validator = input_validator()

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
    app = main()
    app.run()
