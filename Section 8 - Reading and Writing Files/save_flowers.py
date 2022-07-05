data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

filename = "flowers_print.txt"

with open(filename,'w') as plants:
    for plant in data:
        print(plant, file=plants)

# with open(filename) as plants:
#     text = plants.readlines()
# print(text)

new_list=[]
with open(filename) as plants:
    for line in plants:
        new_list.append(line.strip('\n'))
print(new_list)



plants_filename = "flowers_write.txt"
with open(plants_filename,"w") as plants:
    for plant in data:
        plants.write(plant)


numbers_file = "test_numbers.txt"
with open(numbers_file,'w') as test:
    for i in range(10):
        print(i,file=test)

with open(numbers_file,'w') as test:
    for i in range(10):
        # Writing exactly what we want, no more no less
        test.write(str(i))
        # have to force it to do new line etc
        test.write(str(i) + "\n")