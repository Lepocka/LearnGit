class input_validator:
    def __init__(self, input_value: str = ''):
        self.input_value = input_value
    
    def set_input_value(self, input_value):
        self.input_value = input_value

    def is_number(self, input_number):
        try:
            float(input_number)
            return True
        except ValueError:
            return False

    def get_correct_input_number(self):
        input_value = self.input_value
        
        while not (self.is_number(input_value)):
            print('Incorrect input')
            input_value = input('Input number again: ')

        return input_value
    
    def get_correct_input_operator(self):
        input_value = self.input_value

        while not self.is_number(input_value) or not float(input_value) in [0, 1, 2, 3]:
            print('Incorrect input')
            input_value = input('Choose operator again: ')
        
        return input_value
    
def operator_instruction():
    print('0: +')
    print('1: -')
    print('2: *')
    print('3: /')

def calculating(operator, first_num, second_num):
    while True:
        if float(operator) == 0:
            return float(first_num) + float(second_num)
        elif float(operator) == 1:
            return float(first_num) - float(second_num)
        elif float(operator) == 2:
            return float(first_num) * float(second_num)
        elif float(operator) == 3:
            return float(first_num) / float(second_num)

input_value_validator = input_validator()

input_value_validator.set_input_value(input('Input first number: '))

first_number = input_value_validator.get_correct_input_number()

input_value_validator.set_input_value(input('Input second number: '))

second_number = input_value_validator.get_correct_input_number()

operator_instruction()

input_value_validator.set_input_value(input('Choose operator: '))

input_operator = input_value_validator.get_correct_input_operator()

result = calculating(input_operator, first_number, second_number)

print(f'Result: {result}')
