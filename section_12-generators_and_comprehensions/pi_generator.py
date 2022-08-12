# first generator for odd numbers
def oddnumbers():
    n = 1
    while True:
        yield n
        n += 2

odds = oddnumbers()
#for i in range(100):
#    print(next(odds))

# my attempt
# def pi_series():
#     denom = odd()
#     next(denom)
#     n = 0
#     start = 4
#     while True:
#         val = 4*next(denom)**-1
#         if n % 2 == 0:
#             val *= -1
#         n += 1
#         start += val
#         yield start

# his effort
def pi_series():
    odds = oddnumbers()
    approx = 0
    while True:
        approx += (4 / next(odds))
        yield approx
        approx -= (4 / next(odds))
        yield approx



pi = pi_series()

for i in range(20000):
    print(next(pi))