print('Today is a good day to learn Python')
print("Python is fun")
# Always end with the type of quote you started with that
print("Python's strings are easy to use")
# Can embed quotes using this method
print('We can even include "quotes" in strings')

print( 'hello ' + "world")

greeting = 'hello '
#name = input("Please enter a name: ")
name = 'Eoin'
# if we want to space, add that too
print(greeting + " " + name)


# Escape chars
splitString = "This string has been \nsplit over \nseveral \nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting"')
# Or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\"")
# OR
print(""" The pet shop owner said "No, no, 'e's uh,...he's resting """)

anotherSplitString = """This string has been \
split over \
several \
lines"""

print(anotherSplitString)
print('Number 1\tThe Larch\n Number 2\tThe Horse Chestnut')

# If want the actual / char in the quote
#print("C:\users\eoin\file.txt")
# Interpreting \f as char, and backslash is ruining it, need to get around it
print("C:\\users\\eoin\\file.txt")
# use raw string by prefixing the text with a r
print(r"C:\users\eoin\file.txt")

age=26
print(type(greeting))
print(type(age))

# Python is strong typed & dynamic typed
age = 24
print(age)

age='24 years'
print(age)
print(type(age))

### Indexing
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])

# Negative indexing
print(parrot[-1])

# Slicing
print(parrot[0:6]) # Up to but NOT including 6
print(parrot[3:5]) # print 3 up to but NOT including 5
print(parrot[0:9])
print(parrot[:9])

print(parrot[10:])

# Negative slicing
print(parrot[-1])
print(parrot[:-1])
print(parrot[-1:])

print(parrot[-4:-2])
print(parrot[-4:12])

# Step
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])

# Sample application of step slicing
number = "9,223;372:036 854,775;807"
print(number[1::4])
separators = number[1::4]
print(separators)

values= "".join(char if char not in separators else " " for char in number).split()
print("".join(char if char not in separators else " " for char in number))
print(values)
print([int(val) for val in values])

# Negative slicing
letters="abcdefghijklmnopqrstuvwxyz"
# When using a negative step. our stop vcalue needs to be less than start value, ie neg step tells it we're going backwards'
backwards= letters[25:0:-1]
print(backwards)

# How to include the a ?
print(letters[25::-1])

# challenge #qpo #edcba #last 8 in reverse order
print(letters[16:13:-1])
print(letters[-10:-13:-1])

print(letters[4::-1])
print(letters[-22::-1])

# Using neg integers
print(letters[:17:-1])
print(letters[-1:-9:-1])
print(letters[:-9:-1])

##############
print(letters[-4:])
print(letters[:-5:-1])





