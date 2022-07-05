# Start looking at for loops

# The set of values for a for loop must come from an iterable or some sequence
#anything we can iterate over (eg string which is sequence) - is an iterable
parrot = 'Norwegian Blue'
for char in parrot:
    print(char)
print('-'*80)


# Long winded way of stripping out numbers
number = "9,223;372:036 854,775;807"
separators = number[1::4]
#print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print('-'*80)
# Do it another way with for loop
# Get the separators quickly
# Why do we initialise this ? - because we're going to add to this using +=
separators = ""
for char in number:
    if not char.isnumeric():
        separators += char
print(separators)



# # Now do amethod which takes user input
# number = input('Please enter a large number separated by any separators: ')
# separators =""
# for char in number:
#     if not char.isnumeric():
#         separators += char
# #print(separators)
# values = "".join(char if char not in separators else " " for char in number).split()
# print(sum([int(val) for val in values]))
print("*"*80)
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
caps=""
for l in quote:
    if l.isupper():
       caps+= l
print(caps)

# For range it's up to but NOT including the last value - cos index starts at 0.
for i in range(20):
    print("i is now {}".format(i))
print("-"*80)

# Can give step value - when doing this wee need to give start value
for i in range(2,10,3):
    print("i is {}".format(i))
print('-'*80)

# Interesting you can step backwards
for i in range(10,2,-2):
    print("i is {}".format(i))
# range also works with "in"as boolean test
age = 20
if age in range(40):
    print("Age is in the range")


## Nested for loops
# Do a times times tables
for i in range(1,12+1):
    for j in range(1,12+1):
        print("{} times {} is {}".format(i,j,i*j))
    print("#"*80)



# Look at lists and their use for for loops - specifically continue & break
shopping = ['milk','pasta','eggs','spam','bread','rice']
# one way to print our list avoiding spam
for item in shopping:
    if item != "spam":
        print("Buy "+ item)
print("*"*80)

# better way to avoid spam item in list using continue
for item in shopping:
    if item =="spam":
        continue
    print("Buy " + item)
print("*"*80)

## break - terminates the loop
for item in shopping:
    if item =="spam":
        break
    print("Buy " + item)
print("*"*80)

# new problem, find an item in a list
item_to_find = "spam"
found_at = None

for index in range(len(shopping)):
    if shopping[index] == item_to_find:
        # We initialised found_at, so if we never found it we would print something instead of variable not found error
        found_at = index
        break
print("Item found at position {}".format(found_at))

# for i,item in enumerate(shopping):
#     if item == item_to_find:
#         found_at = i
#         break
# print('found item at index {}'.format(found_at))

## Of course a much simpler way of doing all of this is
print("*"*80)
found_at= None
if item_to_find in shopping:
    found_at = shopping.index(item_to_find)
if found_at is not None:
    print("Item found at index {}".format(found_at))
else:
    print("item not found")

#########################################
# While loops - loop while some condition is true and stop when its false
print("*"*80)
print("*"*80)
##########################
# for i in range(10):
#     print("i is now {}".format(i))
i= 0
while i<10:
    print("i is now {}".format(i))
    i+=1



## Adventure game for getting out of maze
available_exits =['North','South','East','West']
# have to initialse it because of the way we created the list
# chosen_exit = " "
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
# print("You escaped")


# Improving game with break
# chosen_exit = " "
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() =='quit':
#         print('You gave up')
#         break
# print("You escaped")

for i in range(0, 100, 7):
    print(i)
    if i>0 and i%11==0:
        break

# numbers that arent divisble by 3 or 5