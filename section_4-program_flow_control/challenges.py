# Similar to guessing game played before, but instead of only having two guesses or 3 etc, we want to
# guess until we get right -> so no repeated ifs
import random


# # my way
# guess = int(input("Please guess a number: "))
# correct = random.randint(1,10)
# print('Correct answer is {}'.format(correct)) # TODO: Remove after tests
# guess_number = 0
# while guess != correct:
#     guess_number += 1
#     if guess == 0:
#         print('Exiting game...')
#         break
#     elif guess > correct:
#         print('Too high, guess lower')
#     else:
#         print('Too low, guess lower')
#     guess = int(input("Please guess again "))
#
# if guess==correct:
#     print('You guessed correctly! It took you {} tries'.format(guess_number))


# His code
answer = random.randint(1,1000)
#print(answer)
guess = 0
guess_number = 0
# while guess != answer:
#     guess = int(input('Pick a number '))
#     guess_number += 1
#     if guess == 0:
#         print('Exiting....')
#         break
#     if guess == answer:
#         print('You guessed correctly, it took you {} tries'.format(guess_number))
#     elif guess > answer:
#         print('Too high, guess lower')
#     else:
#         print('Too low, guess higher')


# Binary chop - let computer guess a number
# Doing it my way

# high = 1000
# low = 1
# print("Please think of a number between {1} and {0}".format(high,low))
# input("Press Enter to start: ") # Just so we can hang proc until inputs
# guess_number = 0
# answer = 468
# while True:
#     guess = low + (high -low) // 2 # midpoint
#     guess_number += 1
#     direction = input('Should cpu go higher or lower? The guess is {}: '.format(guess)).casefold()
#     if direction == 'higher':
#        low = guess
#     if direction == 'lower':
#         high = guess
#     if guess == answer:
#         print('The machine guessed it, it took {} attempts'.format(guess_number))
#         break


# low = 1
# high = 1000
# print('Please think of a number between {} and {}'.format(low,high))
# input('Press enter to start: ')
# guesses = 0
# while True:
#     print('\tGuessing in the range of {} to {}'.format(low,high))
#     guess = low +(high-low) //2
#     high_low = input('My guess is {}. '
#                      'Should I go higher or lower or am I correct '.format(guess)).casefold()
#     guesses += 1
#     # This is how pass would be used if we wrote the actual logic later on
#     # if high_low == 'higher':
#     #     # Guess higher - the low end of range becomes 1 greater than guess
#     #     pass
#     if high_low == 'higher':
#         # Guess higher - the low end of range becomes 1 greater than guess
#         low = guess + 1
#     elif high_low =='lower':
#         # Guess lower - the high end of the range becomes 1 less than guess
#         high = guess - 1
#     elif high_low == 'correct':
#         print('Correct! I got it in {} guesses'.format(guesses))
#         break
#     else:
#         print('Choices are only higher,lower or correct')


## Augmented assignment - literally just using +=. It's binary operation combined with assignment
# So +,-,*,/ all binary: (x+y)

x = 'Good '
x+= 'Morning'
print(x)


# exercise
number = 7
multiplier = 3
answer = 0

# add your loop after this comment
for n in range(multiplier):
    answer += number

print(answer)
print("*"*80)

# use else in a loop - actually has another purpose
# v contrived example

numbers= [1,45,32,12,60]
# Here the else only fires on a successful loop through all elements, if break happens at all we wont see the else
#  clause
for num in numbers:
    if number % 8 == 0:
        #reject the list
        print('The numbers are unacceptable,even one will break it')
        break
else:
    print('These numbers are ok')



# Using this version of else in high low game. Will only work with some numbers where convergence is possible, ie 72
# but not 73

# low = 1
# high = 1000
# print('Please think of a number between {} and {}'.format(low,high))
# input('Press enter to start: ')
# guesses = 0
# while low != high:
#     #print('\tGuessing in the range of {} to {}'.format(low,high))
#     guess = low +(high-low) //2
#     high_low = input('My guess is {}. '
#                      'Should I go higher or lower or am I correct '.format(guess)).casefold()
#     guesses += 1
#     # This is how pass would be used if we wrote the actual logic later on
#     # if high_low == 'higher':
#     #     # Guess higher - the low end of range becomes 1 greater than guess
#     #     pass
#     if high_low == 'higher':
#         # Guess higher - the low end of range becomes 1 greater than guess
#         low = guess + 1
#     elif high_low =='lower':
#         # Guess lower - the high end of the range becomes 1 less than guess
#         high = guess - 1
#     elif high_low == 'correct':
#         print('You got it! ')
#         print('I got it in {} guesses'.format(guesses))
#         break
#     else:
#         print('Choices are only higher,lower or correct')
# else:
#     print('You thought of the number {}'.format(low))
#     print('I got it in {} guesses'.format(guesses))

# Use else with the loop the same way you do with for loops
# available_exits = ['west','east','south','north']
# chosen_exit = " "
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() =='quit':
#         print('You gave up')
#         break
# else:
#     print("You escaped")


# print('Hello my name\t is Eoin. What are\n you doing\n today')

# Ending challenges
#print('-'*80)
#options = {1:'Hello ',2:'Fuck off', 3:'20:10', 4:'-.-',5:'quit'}
# while True:
#     print('[1] Say hello\n[2] Be rude\n[3] Display time\n[4] Smile\n[5] Quit')
#     choice = options[int(input('Choose an option: '))]
#     if choice=='quit':
#         print('Exiting...')
#         break
#     else:
#         print(choice)


# My attempt at it
# choice = None
# valid_options = [0,1,2,3,4,5]
# while choice != 0:
#     options_msg = '[1] Learn Python\n[2] learn Java\n[3] ' \
#                   'Learn KDB\n[4] ' \
#                   'Have Dinner\n[5] Go to Bed\n[0] Exit\n Please choose your options from the list above: '
#     choice = int(input(options_msg))
#     while not choice in valid_options:
#         print('Invalid choice, please choose again')
#         # Could argue this is not necessary, diff between loop til you pick a valid option vs just printing the
#         # message again. Think behaviour resolves to same so maybe secondary loop not necessary and could do
#         # as below ?
#         choice = int(input(options_msg))
#     if choice>0:
#         print('You chose option {}'.format(choice))
#     else:
#         print('Exiting...')
#         break


# His go at it
# print('Please choose options from list below: ')
# print('1:\tLearn Python')
# print('2:\tLearn Java')
# print('3:\tLearn KDB')
# print('4:\tEat Dinner')
# print('5:\tExit')
# choice= "-"
# while True:
#     if choice == '0':
#         break
#     elif choice in "12345":
#         print('You chose {}'.format(choice))
#     else:
#         print('Please choose options from list below: ')
#         print('1:\tLearn Python')
#         print('2:\tLearn Java')
#         print('3:\tLearn KDB')
#         print('4:\tEat Dinner')
#         print('5:\tExit')
#     choice = input()
#
#

# while choice != 0:
#     if choice in "12345":
#         print('You chose {}'.format(choice))
#     else:
#         print('Please choose options from list below: ')
#         print('1:\tLearn Python')
#         print('2:\tLearn Java')
#         print('3:\tLearn KDB')
#         print('4:\tEat Dinner')
#         print('5:\tExit')
#     choice = input()


import nltk
from itertools import product
from nltk.corpus import reuters
corpus = [w.casefold() for w in reuters.words() if len(w)== 5]

alphabet = "abcdefghijklmnopqrstuvwxyz"
one = 's'
two = alphabet
three = alphabet
four = ''.join([l for l in alphabet if not l in "pnle"])
five = 'd'


loop=0
# Wordle
print('Have letters [s][][][][d]')
print("-"*80)
for a,b,c,d,e in product (one, two, three, four, five):
    loop += 1
    word = a+b+c+d+e
    if word in corpus:
        print(a+b+c+d+e)
    if loop % 2000 == 0:
        print('{} letter combinations checked'.format(loop))


