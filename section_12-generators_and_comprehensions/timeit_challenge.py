# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.

import timeit

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(timeit.timeit("x = fact(100)", globals=globals(), number=10000))
    print(timeit.timeit("x = factorial(100)", setup="from __main__ import factorial", number=10000))


# run_1 = """\
# fact(100)
# """
#
# run_2 = """\
# factorial(100)
# """
#
# result = []
# for func in [run_1, run_2]:
#     result.append(timeit.timeit(func, globals=globals(), number=10000))
# print(result)
#
#
# # Print the other methods
# print(80*"*")
# test1 = """\
# def fact(n):
#     result = 1
#     if n > 1:
#         for f in range(2, n + 1):
#             result *= f
#     return result
#
# x = fact(100)
# """
#
# test2="""\
# def factorial(n):
#     # n! can also be defined as n * (n-1)!
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# y = factorial(100)
# """
#
# score = []
# for test in [test1, test2]:
#     score.append(timeit.timeit(test, number=10000))
# print(score)



