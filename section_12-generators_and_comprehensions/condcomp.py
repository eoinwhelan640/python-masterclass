menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)
#
# meals = [meal for meal in menu if "spam" not in meal]
# print(meals)
#
#
# x = 12
# expression = "twelve" if x== 12 else "unknown"
# print(expression)
# meals = [meal if "spam" not in meal else "Meal skipped" for meal in menu]
# print(meals)

# conditional expression syntax for multiple checks
# for meal in menu:
#     print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")


items = set()
for meal in menu:
    for item in meal:
        items.add(item)

print(items)


for meal in menu:
    for item in items:
        if item in meal:
            print(f"{meal} contains {item}")

# conditional expression for fizz buzz
for n in range(36):
    "fizz buzz" if (n%3==0 and n%5==0) else "buzz" if n%5 == 0 else "fizz" if n%3 == 0 else str(n)



challenge = ["fizz buzz" if (n%3==0 and n%5==0) else "buzz" if n%5 == 0 else "fizz" if n%3 == 0 else str(n) for n in range(1,36)]
print(challenge)