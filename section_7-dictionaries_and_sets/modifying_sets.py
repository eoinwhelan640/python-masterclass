#numbers = {}
# this creates an empty set, but dont do this its hard to read. ^ creates an empty dict
# this works because we can use * to unpack a sequence or iterable.
# unpacking an empty sequence produces no values, so it initialises an empty set within braces
# Dont do this, its retarded
#numbers = {*""}
# Might also see this as
#numbers = {*{}}
#print(type(numbers))


numbers = set()
numbers.add(1)
print(numbers)

# get 4 numbers from a user
# while len(numbers) < 5:
#     next_value = int(input("Give me a number >: "))
#     numbers.add(next_value)
# else:
#     print(numbers)


data = ['blue','red','blue','green','red','blue','white']

# unique_data = sorted(set(data))
# print(unique_data)

# create a list of unique colours in the order they appeared
unique_data = list(dict.fromkeys(data))
print(unique_data)