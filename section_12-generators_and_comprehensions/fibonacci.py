a = 2
b = 3
print(f"a is {a}, b is {b}")

# This works because rhs is evaluuated first & asisgned to other side
a, b = b, a
print(f"a is {a}, b is {b}")

# my attempt at a fib gen using yield
# def fibonacci(n):
#     now, last = 1, 0
#     run = 1
#     while run < n+1:
#         if run == 1:
#             yield now - 1
#             run += 1
#         elif run == 2:
#             yield now
#             run += 1
#         else:
#             run += 1
#             last, now = now, now + last
#             yield now
# def fibonacci(n):
#     now, last = 1, 0
#     result = None
#     if n < 2:
#         return n-1
#     for i in range(n-2):
#         result = now + last
#         last = now
#         now = result
#     return now
# for i in range(10):
#     print(f"index is {i+1}, fib is {fibonacci(i+1)}")
# val = fibonacci(10)
# for ind, i in enumerate(val):
#      print(f"index is {ind+1}, fib is {i}")

# His fibonacci
def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current

fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))


for i in range(10):
    print(next(fib))