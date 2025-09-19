def is_number(input_number):
    try:
        float(input_number)
        return True
    except ValueError:
        return False

def number_validation(input_number):
    number = input_number

    while not (is_number(number)):
        print('This is not a number')
        number = input('Input number again: ')

    return number 

first_number = input('Input first number: ')

first_number = number_validation(first_number)

second_number = input('Input second number: ')

second_number = number_validation(second_number)

result = float(first_number) + float(second_number)

print(f'Result: {result}')


