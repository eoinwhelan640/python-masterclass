# # Start with if statements
# name =input("Enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
#
#
# # if age >= 18:
# #     print("You are old enough to vote at {}".format(age))
# #     print("Please put an X in the box")
# # else:
# #     print("Please come back in {} years".format(18-age))
#
# # Elif
# # Set a breakpoint by clicking in the margin and getting the red dot
# if age<18:
#     print("Please come back in {} years".format(18-age))
# elif age== 900:
#     print("Sorry Yoda you died in Return of the Jedi")
# else:
#     print('You are old enough to vote')
#     print("Please put an X in the box")

# HUUUUGE feature, multi line comment out - do ctrl + slash on highlighted block to comment out it all


# # Guessing game
# answer = 5
#
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
# if guess < answer:
#     print("Please guess higher")
# elif guess > answer:
#     print("Please guess lower")
# else:
#     print('You guessed correctly')


#################
# print("Please guess a number between 1 and 10: ")
# answer = 5
# # Add a second guess
# guess = int(input())
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input('Please guess again: '))
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print('Wrong again ')
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input('Please guess again: '))
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print('Wrong again')
# else:
#     print('You guessed correctly')

# Change it to be simplified
# answer = 5
# guess = int(input("Please guess a number between 1 and 10: "))
#
# if guess != answer:
#     if guess < answer:
#         print('Please guess higher: ')
#     else:
#         print('Please guess lower: ')
#     guess = int(input('You must guess again: '))
#     if guess == answer:
#         print('Well done you got it')
#     else:
#         print('Sorry you guessed wrong again')
# else:
#     print('Congrats you guessed correctly first time')
#
#


#
# answer = 5
#
# guess = int(input("Please guess a number between 1 and 10: "))
#
# if guess == answer:
#     print('Congrats you guessed correctly first time')
# else:
#     if guess < answer:
#         print('Please guess higher: ')
#     else:
#         print('Please guess lower: ')
#     guess = int(input('You must guess again: '))
#     if guess == answer:
#         print('Well done you got it')
#     else:
#         print('Sorry you guessed wrong again')
#
#





## More complex clauses - And vs Or
# age = int(input('How old are you? '))
# # if 16 <= age <= 65:
# #     print('Have a good day at work')
# # else:
# #     print('No work today')
# if age<=16 or age>=65:
#     print('Enjoy the time off')
# else:
#     print('Get to work')
# print('-'*80)

day = 'Saturday'
temp = 30
raining = False

# if (day == 'Saturday' and temp>27) or not raining:
#     print('Go Swimming')
# else:
#     print("Learn Python")


# # Truthy values
# if 0:
#     print('True')
# else:
#     print('False')
#
# name = input('Input your name: ')
# if name:
#     print('Hello {}'.format(name))
# # Pressing enter so no name comes in, gives '', so we get False boolean value
# else:
#     print('Horse with no name')

# Better to do
# if name !="":
#     print('Hello {}'.format(name))
# # Pressing enter so no name comes in, gives '', so we get False boolean value
# else:
#     print('You are a horse with no name')

# in and not in used with sequences and set
# parrot = 'Norweigian Blue'
# letter = input('Enter a char: ')
#
# if letter in parrot:
#     print('{} is in {}'.format(letter,parrot))
# else:
#     print("I don't need that letter")

# activity = input('What would you like to do today? ')
#
# if "cinema" not in activity:
#     print('But I want to go to the cinema')

name = input('What is your name ? ')
age = int(input('What age are you? '))

if 18 <= age < 31:
    print('Come on in {}!'.format(name))
else:
    print('You are the wrong age, come back in {} years'.format(18 - age))


