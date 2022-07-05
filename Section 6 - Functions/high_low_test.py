LOW = 1
HIGH = 1000

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")
# function is reworked to output the number of guesses, not to just exit when we guess correctly
def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1

correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses,1
    elif number_of_guesses == max_guesses:
        correct_count += 1


print('I guessed without being told {} times. Max {} guesses'.format(correct_count, max_guesses))




# Fizz buzz
def fizz_buzz(n: int) -> str:
    '''
    Play fizz buzz game


    :param n: Integer to check
    :return: 'fizz' if number is divisible by 3
        'buzz' if number is divisble by 5
        'fizz buzz' if number is divisible by 3 AND 5
        The number as a string otherwise.
    '''
    if (n % 3 == 0) and (n % 5 == 0):
        return 'fizz buzz'
    elif (n % 3 == 0):
        return 'fizz'
    elif (n % 5 == 0):
        return 'buzz'
    return str(n)


for i in range(1,101):
    out = fizz_buzz(i)
    print(out)



# Create a loop to play the game agaisnt the computer
# print(80*'*')
# print('STARTING GAME')
# print(80*'*')
# for i in range(1,100):
#     if i ==1:
#         print('Starting at 1')
#     out = fizz_buzz(i)
#     if i %2 == 0:
#         print('Computer says: {}'.format(out))
#     else:
#         say = input('User: ')
#         if say != out:
#             print('WRONG - GAME OVER.')
#             print('ANSWER WAS: {}'.format(out))
#             break

# His way of doing it
print(80*'*')
print('STARTING GAME')
print(80*'*')

# In thsi was instead of douing one move at a time, within the loop we're doing computers turn and my turn
# less code and less for lops. Dont have to do the even/odd check to decide who goes too.

# input('Play fizz Buzz. Press Enter to start')
# print()
# next_number = 0
# while next_number< 99:
#     next_number+=1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_answer = fizz_buzz(next_number)
#     players_answer = input('Your turn: ')
#     if players_answer != correct_answer:
#         print('WRONG, the correct answer was {}'.format(correct_answer))
#         break
# else:
#     print('All Done!')


# Write a factorial function
import math
def factorial(n: int) -> int:
    '''
    Calculate factorial for a given n


    :param n: Integer for factorial calculation
    :return: n!
    '''
    start = 1
    for i in range(1,n):
        start *= i+1
    return start


for i in range(36):
    out = factorial(i)
    print('{} factorial is: {}'.format(i,out))

# His way
# def factorial(n: int) -> int:
#     """Return n! (0! is 1)."""
#     if n <= 1:
#         return 1
#
#     result = 2
#     for x in range(3, n + 1):
#         result *= x

# Using recursion his way, dont like this
# def factorial(n: int) -> int:
#     """
#     Return n! (0! is 1).
#
#     Valid for `n` in the range 0 to 998 (inclusive).
#     Larger values of `n` will cause a RecursionError.
#     """
#     if n <= 1:
#         return 1
#
#     return n * factorial(n - 1)
