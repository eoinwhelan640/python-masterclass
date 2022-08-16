import timeit

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

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("-" * 40)

def spamless():
    meals = [meal for meal in menu if "spam" not in meal]
    return meals

print("-" * 40)

# Using filter
def not_spam(meal_list: list):
    return "spam" not in meal_list

def spamless_filter():
    spamless_meals = list(filter(not_spam, menu))
    return spamless_meals

if __name__ == "__main__":
    print(timeit.timeit(spamless, number=10000))
    print(timeit.timeit(spamless_filter, number=10000))