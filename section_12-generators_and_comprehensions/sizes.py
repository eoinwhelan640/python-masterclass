import sys

def my_range(n: int):
    start = 0
    while start < n:
        yield start
        start += 1


big_range = my_range(100)
print(f"big_range is {sys.getsizeof(big_range)} bytes")


# create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

print(f"big_list is {sys.getsizeof(big_list)} bytes")
print(big_range)
print(big_list)


print(next(big_range))
print(f"big_range is {sys.getsizeof(big_range)} bytes")