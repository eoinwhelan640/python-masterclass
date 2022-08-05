import sys


def game_v1():
    print('Enter two numbers to sum them')
    one = input('First number>: ')
    two = input('Second number>: ')
    try:
        print(f'Sum is {int(one) + int(two)}')
    except ValueError:
        print('One of the inputs is not a number')

def game_helper():
    number = None
    while number == None:
        try:
            number = int(input('Enter number>: '))
        except ValueError:
            print('That was not a number, choose again')
    return number

def game_v2():
    print('Enter two numbers to sum them')
    print('First Number')
    one = game_helper()
    print('\nSecond Number')
    two = game_helper()
    print(f'Sum is {one + two}')

#game_v2()

# His solution
def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            # He doesnt wait for loop to iterate and close via the clause
            # When has condition he wants, he ends the loop.
            # Don't surrender to the loop! dont let it push you around
            # break out when I have what I want
            return number
        except ValueError:
            print("Invalid number, try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("Finally clause always executes")

first_number = getint('Please enter the first number: ')
second_number = getint('Please enter the second number: ')
# Do a divisin instead of addition
try:
    print(f'{first_number}/{second_number} is {first_number/second_number}')
except ZeroDivisionError:
    print('Cannot divide by 0')
    sys.exit(2)
else:
    print("Division performed successfully"
          "+")
