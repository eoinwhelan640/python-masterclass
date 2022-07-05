from contents import pantry, recipes

print(pantry)
print(recipes)
print()

display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key
# while True:
#     print('Please choose your recipe')
#     print('---------------------------')
#     print('0 - Exit')
#     for key, value in display_dict.items():
#         print(f'{key} - {value}')
#
#     choice = input('>: ')
#     if choice == '0':
#         break
#     elif choice in display_dict:
#         selected_item = display_dict[choice]
#         print(f'You have selected {selected_item}')
#         print('checking ingredients...')
#         ingredients = recipes[selected_item]
#         print(ingredients)
#         # Check the pantry and confirm we have it all - all or nothing
#         # supplies = [food_item in pantry for food_item in ingredients]
#         # if all(supplies):
#         #     print('We have all the ingredients, enjoy the food')
#         # else:
#         #     missing_items=[]
#         #     for i,bool in enumerate(supplies):
#         #         if bool == False:
#         #             missing_items.append(ingredients[i])
#         #     print(f"We're short on supplies, we don't have {missing_items}")
#
#         # Just print out when we're missing stuff
#         # Basically achieving the same thing as above but with less code and neater
#         # It actually prints the list with an "ok" beside each ingredient
#         for food_item in ingredients:
#             if food_item in pantry:
#                 print(f'\t{food_item} OK')
#             else:
#                 print(f"\tYou don't have a necessary ingredient: {food_item}")


# Adapting this to check quantities as well
from contents_quantities import pantry, recipes

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key


# my attempt
# while True:
#     print('Please choose your recipe')
#     print('---------------------------')
#     print('0 - Exit')
#     for key, value in display_dict.items():
#         print(f'{key} - {value}')
#
#     choice = input('>: ')
#     if choice == '0':
#         break
#     elif choice in display_dict:
#         selected_item = display_dict[choice]
#         print(f'You have selected {selected_item}')
#         print('checking ingredients...')
#         ingredients = recipes[selected_item]
#         print(ingredients)
#         for food_item, quantity_needed in ingredients.items():
#             if food_item not in pantry:
#                 print(f"\t{food_item.upper()}: Out of Stock")
#                 # Check we have the required quantities
#             else:
#                 if pantry[food_item] >= quantity_needed:
#                     print(f'\t{food_item.upper()}: OK')
#                 else:
#                     print(f'\t{food_item.upper()}: Insufficient Quantity')


# the way he does the quantity choice
# he utilises get() for the dictionary method as well
# while True:
#     print('Please choose your recipe')
#     print('---------------------------')
#     print('0 - Exit')
#     for key, value in display_dict.items():
#         print(f'{key} - {value}')
#
#     choice = input('>: ')
#     if choice == '0':
#         break
#     elif choice in display_dict:
#         selected_item = display_dict[choice]
#         print(f'You have selected {selected_item}')
#         print('checking ingredients...')
#         ingredients = recipes[selected_item]
#         print(ingredients)
#
#         for food_item,required_quantity in ingredients.items():
#             # very useful, grab the quanity, if its not there use 0
#             # Allows us to see what we need when we're short an item
#             quantity_in_pantry = pantry.get(food_item,0)
#             if required_quantity <= quantity_in_pantry:
#                 print(f'\t{food_item} OK')
#             else:
#                 quantity_to_buy = required_quantity - quantity_in_pantry
#                 print(f"\tYou need to buy {quantity_to_buy} of {food_item}")


# Challenge - have this program output some kind of data structure we can use to build a shopping list
#My attempt works but is a bit nasty, lets see his code
# def shopping():
#     '''
#     Function to create a shopping list for the week
#     :return: A list of ingredients and the quantity to get
#     '''
#     meals, shopping_list = build_shopping_list()
#     print(f"Meal plan for this week is {', '.join(meals)}")
#     print(f'Shopping list is {shopping_list}')
#     return shopping_list
#
# def add_to_list(ingredients):
#     shopping_list = {}
#     for food_item, required_quantity in ingredients.items():
#         # very useful, grab the quanity, if its not there use 0
#         # Allows us to see what we need when we're short an item
#         quantity_in_pantry = pantry.get(food_item, 0)
#         if required_quantity >= quantity_in_pantry:
#             quantity_to_buy = required_quantity - quantity_in_pantry
#             print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
#             current_amount_on_list = shopping_list.get(food_item,0)
#             add_to_list = quantity_to_buy + current_amount_on_list
#             shopping_list[food_item] = add_to_list
#     return shopping_list
#
# def build_shopping_list() -> str:
#     '''
#     Build a shopping list based off user input for meals during the week
#
#     :returns: The meals planned for the week. The list of ingredients and quantity needed to purchase.
#
#     '''
#     meal_plan = []
#     shopping_list={}
#     while True:
#         print('Please choose your recipe')
#         print('---------------------------')
#         print('0 - Exit')
#         for key, value in display_dict.items():
#             print(f'{key} - {value}')
#         choice = input('>: ')
#         if choice == '0':
#             break
#         elif choice in display_dict:
#             selected_item = display_dict[choice]
#             if not selected_item in meal_plan:
#                 meal_plan.append(selected_item)
#                 print(f'Adding {selected_item} to meal plan')
#
#             else:
#                 meal_plan.remove(selected_item)
#                 print(f'Removing {selected_item} from meal plan')
#                 continue
#
#             ingredients_needed = recipes[selected_item]
#             shopping_list = add_to_list(ingredients_needed)
#     return meal_plan, shopping_list
#



# His attempt
# def add_shopping_item(data: dict, item: str,amount: int)-> None:
#     """Add a tuple containing item and `amount` to the data `dict` """
#     if item in data:
#         data[item] += amount
#     else:
#         data[item] += amount

# Using setdefault method instead
def add_shopping_item(data: dict, item: str,amount: int)-> None:
    """Add a tuple containing item and `amount` to the data `dict` """
    data[item] = data.setdefault(item,0) + amount


shopping_list= {}
while True:
    print('Please choose your recipe')
    print('---------------------------')
    print('0 - Exit')
    for key, value in display_dict.items():
        print(f'{key} - {value}')

    choice = input('>: ')
    if choice == '0':
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f'You have selected {selected_item}')
        print('checking ingredients...')
        ingredients = recipes[selected_item]
        print(ingredients)

        for food_item,required_quantity in ingredients.items():
            # very useful, grab the quanity, if its not there use 0
            # Allows us to see what we need when we're short an item
            quantity_in_pantry = pantry.get(food_item,0)
            if required_quantity <= quantity_in_pantry:
                print(f'\t{food_item} OK')
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)
for things in shopping_list.items():
    print(things)






