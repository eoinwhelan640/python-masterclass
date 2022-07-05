travel_mode = {"1": "car", "2": "plane"}

pack = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print('Please choose your mode of travel')
for key,value in travel_mode.items():
    print(f'[{key}]: {value}')

mode='-'
while mode not in travel_mode:
    mode = input("> ")

#Boring way
# if mode == "2":
#     for forbidden_item in restricted_items:
#         pack.discard(forbidden_item)

# using difference_update to directly remove items
# if mode == "2":
#     pack.difference_update(restricted_items)

# Using the -= operator (think set + set operations, works the same way)
# Sets use a lot of mathematical formula
# if mode == "2":
#     pack -= restricted_items


print("You need to pack:")
for item in sorted(pack):
    print(item)

# challenge
# make a list of  favourites without the stuff thats in the basket
favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

# Add your code here.
suggestions = sorted(favourites - basket)
