data = [
    ("orange", "a sweet orange,citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy")
]

# ord gives you the unicode value for the letters - stands for ordinal
# Every char represented by an integer
print(ord("a"))
print(ord("b"))
print(ord("z"))
print()

# Any string to a fixed size value -> an integer
def simple_hash(s: str) -> int:
    """A simplified hashing function"""
    basic_hash=ord(s[0])
    # Scramble bits of key in some way, we do a divide by 10
    return basic_hash % 10


def get(k: str) ->str:
    """Return the value for a key, or None if the key doesn't exist"""
    hash_code = simple_hash(k)
    if values[hash_code]:
        return values[hash_code]
    else:
        return None


keys = [""] * 10
values = keys.copy()

for key,value in data:
    #Using our one
    h = simple_hash(key)
    #Pythons hash function
    #h = hash(key)
    print(key,h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print()
value = get("lemon")
print(value)


