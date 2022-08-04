panagram = "The quick brown fox jumps over the lazy dog"

words = panagram.split(", ")
#print(words)

print("".join(panagram))




# Code challenge
numbers = ['9','223','372','036','854','775','807']

# for ind,num in enumerate(numbers):
#     numbers[ind] = int(num)
#
# print(numbers)

# his way to do it, values in place
for ind in range(len(numbers)):
    numbers[ind] = int(numbers[ind])

# his way to create a new list and append integers to it
new=[]
for ind in range(len(numbers)):
    new.append(int(numbers[ind]))
print(new)




# program to add three numbers
numbers = input("Please enter 3 comma separated numbers: ")
tokens=numbers.split(',')

for ind in range(len(tokens)):
    tokens[ind] = int(tokens[ind])
a,b,c = tokens
result = a+b-c
print(result)d

# other way
# out=0
# for val in tokens:
#     out += int(val)
# else:
#     print(out)