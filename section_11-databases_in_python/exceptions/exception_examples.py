def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

# try:
#     print(factorial(1000))
# except (RecursionError, ZeroDivisionError):
#     print("Number is too large")


try:
    print(factorial(1000/0))
except RecursionError:
    print("Can't calculate factorials that large")
except ZeroDivisionError:
    print("zero division")

print("Program terminating")