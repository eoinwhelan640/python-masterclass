burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans", "spam"]

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)
# if want to just print instead of storing in a list
for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)

# for burger in burgers:
#     for topping in toppings:
#         print(burger,topping)

print(80*"*")
for nested_meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meal)

print(80*"*")
val = [[(burger, topping) for burger in burgers] for topping in toppings]
print(val)






# Can loop in all exact same way as for loops, so can nest when inheriting but also without
#XX = [("a", "b","c","d"), (1,2), ("e"), (1.0, "dove")]
# for t in XX:
#     for it in t:
#         print(it)
#val = [print(t, it, topping ) for t in XX for it in t for topping in toppings]
# print(val)