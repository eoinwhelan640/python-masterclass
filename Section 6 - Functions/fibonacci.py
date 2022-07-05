def fibonacci(n):
    """
    Create nth sequence of fibonnacci numbers

    :param n: Number of fibonacci numbers to return
    :return: List of fibonacci numbers
    """
    fib = [0,1]
    # -2 cos we start off with first two
    for i in range(n-2):
        fib.append(fib[i] + fib[i+1])
    return fib


result =  fibonacci(20)
print(len(result))


## Work was done on functions.py page




