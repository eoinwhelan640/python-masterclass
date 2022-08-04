farm_animals = {'cow','sheep','hen','goat','horse'}
print(farm_animals)
for animal in farm_animals:
    print(animal)

print()
print("Indexing a sequence")
animals_list = ['cow','sheep','hen','goat','horse']

print(animals_list[3])
# print(farm_animals[2])

more_animals = {'cow','sheep','hen','goat','horse'}
if more_animals == farm_animals:
    print('The sets are equal')