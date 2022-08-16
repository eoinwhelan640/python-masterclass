import timeit

text = "what have the romans ever done for us"

def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


def comp_words():
    words = [word.upper() for word in text.split(" ")]
    return words


#print(capitals)
#print(words)

# can use map for the same thing
print(80*'*')
def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals

def map_words():
    map_w = list(map(str.upper, text.split(" ")))
    return map_w


if __name__ == "__main__":
    print("Timing")
    print("Comprehension")
    print(timeit.timeit(comp_caps, setup="from map_func import comp_caps", number=10000))
    print(timeit.timeit(comp_words, setup="from map_func import comp_words", number=10000))
    print("Map")
    print(timeit.timeit(map_caps, setup="from map_func import map_caps", number=10000))
    print(timeit.timeit(map_words, setup="from map_func import map_words", number=10000))