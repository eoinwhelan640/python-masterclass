pangram = 'The quick brown fox jumps over the lazy dog'
# A pangram is a sentence with all the letters of the alphabet in one
letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_num= sorted(numbers)
print(sorted_num)

names= ['Graham', 'John','terry','eric','Terry','michael']
names.sort(key=str.casefold)
print(names)