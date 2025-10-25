def is_number(input_number):
    try:
        float(input_number)
        return True
    except ValueError:
        return False

def number_validation(input_number):
    number = input_number

    while not (is_number(number)):
        print('Incorrect input')
        number = input('Input again: ')

    return number

def operator_instruction():
    print('0: +')
    print('1: -')
    print('2: *')
    print('3: /')


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
        return float(self.first_num) / float(self.second_num)
    
    def calculating(self) -> float:
        if float(self.operator) == 0:
            return self.addition()
        elif float(self.operator) == 1:
            return self.subtraction()
        elif float(self.operator) == 2:
            return self.multiplication()
        elif float(self.operator) == 3:
            return self.division()
        else:
            print('Incorrect input')
            operator_instruction()
            new_operator = input('Choose operator again: ')
            new_operator = number_validation(new_operator)
            self.operator = new_operator
            return self.calculating()

first_number = input('Input first number: ')

first_number = number_validation(first_number)

second_number = input('Input second number: ')

second_number = number_validation(second_number)

operator_instruction()

input_operator = input("Choose operator: ")

input_operator = number_validation(input_operator)

calculator = Calculator(input_operator, first_number, second_number)

result = calculator.calculating()

print(f'Result: {result}')
