def multiply(x: float,y: float = 300) -> float:
    result = x*y
    return result


# def check_palindrome(x):
#     if x == x[::-1]:
#         return True
#     else:
#         return False

# better way
# def is_palindrome(string):
#     backwards = string[::-1]
#     return backwards == string

# better again
def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string.casefold() == string[::-1].casefold()
#
#
# # Doing it with a simple lambda
# test = lambda x: True if x == x[::-1] else False
#
#
# val1 = is_palindrome("abcddcba")
# val2 = test("abcddcba")
#
# print(val1)
# print(val2)

# while True:
#     word = input("Please input your word: ").casefold()
#     if word == 'stop':
#         break
#     if is_palindrome(word) == True:
#         print("{} is a palindrome".format(word))
#     else:
#         print("{} is not a palindrome - try again".format(word))

# create a palindrome sentence checker
# Only use alphanumeric
# remove the punctuation
#ss='Was it a car, or a cat, I saw?'
# def check_pal(x):
#     letters = ''.join(x.casefold().split())
#     output = []
#     for letter in letters:
#         if letter.isalnum():
#             output.append(letter)
#     result = ''.join(output)
#     return result==result[::-1]
#
# print(check_pal('Was it a car, or a cat, I saw?'))


# Much better code for palindrome
# Create an empty string instead of making a list we have to keep collpasing. Can just use '+' to combine strings
# def sentence_palindrome(sentence):
#     string=""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     return string==string[::-1]

# Do it using the other function
def sentence_palindrome(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
        punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string=""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)

print(sentence_palindrome('Was it a car, or a cat, I saw?'))

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

# my way
# Sum even or odd numbers in a range
# if t is e then sum all even numbers <n
# if t is o then its all off numbers
# give -1 if t is neither of these
# def sum_eo(n,t):
#     """
#     Sum the even or odd numbers in a given range based
#
#     :param n: Integer range we will use for sum
#     :param t: String to determine if we sum even or odd numbers in range
#     :return: Sum of even/odd numbers in range
#     """
#     if not t in ['e','o']:
#         print('Invalid choice, Exiting...')
#         return -1
#     numbers = [i for i in range(0,n,2)]
#     if t == 'o':
#         for i in range(len(numbers)):
#             numbers[i] += 1
#     return sum([i for i in numbers if i<n])
#
# #
# print(sum_eo(10,'e'))
# print(sum_eo(7,'o'))
# print(sum_eo(11,'spam'))


# better way of doing it
# def sum_eo(n,t):
#     """
#     Sum the even or odd numbers in a given range
#
#     :param n: Integer range we will use for sum
#     :param t: String to determine if we sum even or odd numbers in range
#     :return: Sum of even/odd numbers in range
#     """
#     if t =='e':
#         start = 2
#     elif t =='o':
#         start = 1
#     else:
#         return -1
#     return sum(range(start,n,2))
# #
#  print(sum_eo(10,'e'))
# # print(sum_eo(7,'o'))
# # print(sum_eo(11,'spam'))

# def fibonacci(n):
#     """
#     Create nth sequence of fibonnacci numbers
#
#     :param n: Number of fibonacci numbers to return
#     :return: List of fibonacci numbers
#     """
#     fib = [0,1]
#     # -2 cos we start off with first two
#     for i in range(n-2):
#         fib.append(fib[i] + fib[i+1])
#     return fib

# His way of doing fibonacci
# Doesnt use list or indexes, just creates placeholder values to update each time
def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`"""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1,0
    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


# result = fibonacci(20)
# print(len(result))
for i in range(36):
    print(i,fibonacci(i))

p = sentence_palindrome(10)