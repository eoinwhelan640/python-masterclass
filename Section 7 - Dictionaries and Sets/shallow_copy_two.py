animals = {
    'lion':["scary","cat",'yellow'],
    "elephant":["big","grey",'wrinkled'],
    "teddy": ["cuddly","stuffed"]
}

# The dict above is written explicitly and can be a bit misleading
# Easier to think of our dict as being stored this way
# Ie our list exists somewhere in mem, and the value for key "lion" eg, is that list
lion_list = ["scary","cat"]
elephant_list = ["big","grey"]
teddy_list = ["cuddly","stuffed"]

animals = {
    'lion':lion_list,
    "elephant":elephant_list,
    "teddy": teddy_list,
}

things = animals.copy()
print(animals['teddy'])
print(things['teddy'])

print()


#things["teddy"].append("toy")
teddy_list.append('toy')
print(animals['teddy'])
print(things['teddy'])