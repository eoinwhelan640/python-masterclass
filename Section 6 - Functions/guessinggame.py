import random

# Two approaches. 1 is to terminate if the function gets nonsense, ie set the value to 0
# Second approach is to loop until we get a valid number
# def get_integer():
#     while True:
#         guess = input('Please guess a number between 1 and {}: '.format(highest))
#         if guess.isnumeric():
#             break
#         else:
#             print('Thats not a number')
#     return int(guess)

# really interesting way to make the else part implicit, we dont need to actually write it
# because the else wont run if we return, so can leave it out entirely
# ie on run through where we guess a strng, it prints but on correct run it hits the return and doesnyt
def get_integer():
    while True:
        guess = input('Please guess a number between 1 and {}: '.format(highest))
        if guess.isnumeric():
            return int(guess)
        print('Thats not a number')



highest = 1000
answer = random.randint(1,highest)
guess=0
#print('Please guess a number between 1 and {}'.format(highest))


# My attempt
# while guess != answer:
#     guess = get_integer()
#     if guess == 0:
#         break
#     if guess == answer:
#         print('Congrats you guessed it')
#         break
#     else:
#         if guess < answer:
#             print('Please guess higher')
#         else:
#             print('Please guess lower')
#
#


#original
# while guess != answer:
#     guess = int(input('Please guess a number between 1 and {}: '.format(highest)))
#     if guess == 0:
#         break
#     if guess == answer:
#         print('Congrats you guessed it')
#         break
#     else:
#         if guess < answer:
#             print('Please guess higher')
#         else:
#             print('Please guess lower')



# the way he does it
def get_integer(prompt):
    """
    Get an integer from standard input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that the user will see, when
        they're prompted to enter the value
    :return: The integer that the user enters
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            # because we're using return here explicitly, we don't need to use break to end the loop
            return int(temp)

print(input.__doc__)
print('*'*80)
print(get_integer.__doc__)

while guess != answer:
    guess = get_integer('Choose a number: ')
    if guess == 0:
        break
    if guess == answer:
        print('Congrats you guessed it')
        break
    else:
        if guess < answer:
            print('Please guess higher')
        else:
            print('Please guess lower')
