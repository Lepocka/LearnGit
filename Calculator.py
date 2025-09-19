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
        else:
            print('Incorrect input')
            operator_instruction()
            operator = input('Choose operator again: ')

first_number = input('Input first number: ')

first_number = number_validation(first_number)

second_number = input('Input second number: ')

second_number = number_validation(second_number)

operator_instruction()

input_operator = input("Choose operator: ")

input_operator = number_validation(input_operator)

result = calculating(input_operator, first_number, second_number)

print(f'Result: {result}')
