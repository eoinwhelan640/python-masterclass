text = "what have the Romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

# not neccessary to always use comprehension
words = [word.upper() for word in text.split(' ')]
print(words)
