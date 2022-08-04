from contents import pantry

chicken_quantity = pantry.setdefault('chicken',0)
print(f'chicken: {chicken_quantity}')


beans_quantity = pantry.setdefault('beans',0)
print(f'beans: {beans_quantity}')

ketchup_quantity = pantry.get('ketchup',0)
print(f'ketchup: {ketchup_quantity}')

# exercise

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
for letter in text.casefold():
    if letter.isalnum():
        word_count[letter] = word_count.setdefault(letter,0) + 1


# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)

# solution
# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Iterate over every character in the string.
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        word_count[char] = word_count.setdefault(char, 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
