''' checks answer and writes coloured message '''
from termcolor import colored

def check_answer(my_value, expected_value = ''):
    ''' Prints the answer and compares with the expected solution '''
    print(my_value)
    if expected_value != '':
        if my_value == expected_value:
            print(colored('CORRECT! Your answer is good', 'green'))
        else:
            print(colored(f'INCORRECT! The expected answer is: {expected_value}', 'red'))
