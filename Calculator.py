first_num = input('Input first number: ')

while not (str.isdigit(first_num)):
    print('This is not a number')
    first_num = input('Input first number again: ')

second_number = input('Input second number: ')

while not (str.isdigit(second_number)):
    print('This is not a number')
    second_number = input('Input second number again: ')

result = int(first_num) + int(second_number)

print(f'Result: {result}')
