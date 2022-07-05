import copy
# behaviour before, animlas and things are same object, use copy to make a new one
animals = {
    'lion':"scary",
    "elephant":"big",
    "teddy": "cuddly"
}

things = animals
animals['teddy'] = 'toy'
print(things['teddy'])
things['lion'] = 'EOIN'
print(animals['lion'])

other_thing = animals.copy()
things['EOIN'] = 'COOL'
print(animals)
print(things)
print(other_thing)




# shallow copy
print(80*'-')

animals = {
    'lion':["scary","cat"],
    "elephant":["big","grey"],
    "teddy": ["cuddly","stuffed"]
}
# This does a shallow copy
#things = animals.copy()
# This does a deep copy
things = copy.deepcopy(animals)

print(id(things['teddy']),things['teddy'])
print(id(animals['teddy']), animals['teddy'])
print()
things["teddy"].append("toy")
print(animals['teddy'])
print(things['teddy'])

# challenge - create a function which copies a dictionary
# def copy_dict(dictionary: dict)->dict:
#     """ Make a copy of a dictionary"""
#     new_dict={}
#     for key,value in dictionary.items():
#         new_dict[key] = new_dict.setdefault(key,value)
#     return new_dict

# def copy_dict(dictionary: dict)->dict:
#     """ Make a copy of a dictionary"""
#     return {k:v.copy() for k,v in dictionary.items()}

# His solution
def copy_dict(d: dict) -> dict:
    new_dict = {}
    for key,value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict

from contents_quantities import recipes
new_dict = copy_dict(recipes)
print(id(animals))
print(id(new_dict))
print()
new_dict['Butter chicken']['lemon'] = 100
print(new_dict['Butter chicken'])
print(recipes['Butter chicken'])


