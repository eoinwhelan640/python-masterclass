def factorial(n):
    """Calculate n! iterably"""
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
        return result


# for i in range(130):
#     print(f"{i}: {factorial(i)}")


def recursive_factorial(n):
    """Calculate n! recursively"""
    # n! = (n)(n-1)!
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n-1)
# print(recursive_factorial(1))
# print(recursive_factorial(2))
# print(recursive_factorial(3))


# fibonacci recursive
# my attempt
# consider the sequence as [1,1,2,3]
def fib_recursion(n):
    if n <= 2:
        return 1
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)


# his version
# he considers the sequence as [0, 1,1,2,3]
def fib(n):
    "F(n) = F(n - 1) + F(n - 2)"
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# Also his way, doing it iterably
def fibonacci(n):
    if n==0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus_1 = 1
        n_minus_2 = 0
        for f in range(1, n):
            result = n_minus_2 + n_minus_1
            n_minus_2 = n_minus_1
            n_minus_1 = result
    return result

for i in range(36):
    print(i, fib(i),fibonacci(i) ,sep='\t')


