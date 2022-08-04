menu = [
    ["egg", 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
]

for meal in menu:
    print(meal)
    if 'spam' not in meal:
        print("I can eat this")
        for item in meal:
            print(item)
    else:
        print('{} has a spam score of {}'.format(meal,meal.count('spam')))







