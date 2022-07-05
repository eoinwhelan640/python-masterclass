# The different dictionary methods
d = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'}

pantry_items = ['chicken','spam', 'egg', "bread", "lemon"]



# fromkeys
# new_dict = dict.fromkeys(pantry_items,10)
# print(new_dict)

# keys() method produces a view object, you cant add or subtract keys to the object, its kinda a link to the saved
# keys of the real dict on the mem, like a pointer. So if you update the real dict, this updates.
# Not really used, these two are the exact same
print(d.keys())
for item in d:
    print(item)
for key in d.keys():
    print(key)

# Update method
# Just lets you amend value of one dictionary using another dictionary
# Whichever one you pass as arg will be used to update the other one, its pretty self-explanatory
print("UPDATE METHOD\n"+80*'-')
d2 = {
    7:"lucky seven",
    10:"ten",
    3: "this is the new three",
}

d.update(d2)
for key,value in d.items():
    print(key,value)

d.update(enumerate(pantry_items))
for key,value in d.items():
    print(key,value)


# dict.values() - works the exact same ways as keys() but for the values
# Cant index into these objects in keys(), values() becaus ethey operate like sets and so dont have indexes
print("VALUES METHOD\n"+80*'-')
print(d.values())

# if wanted to find keys from values, but not really efficient
keys = list(d.keys())
values = list(d.values())
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

# More obvious way to do it
# This would also work if value four appeared a few times
# In general, work with keys on dict, shouldnt really be focusing on the values 
for key,value in d.items():
    if value =='four':
        print(f"{d[key]} was found with the key {key}")
