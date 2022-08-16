import timeit


setup = '''\
gc.enable()
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
'''


locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


def nested_loop():
    result = []
    for loc in sorted(locations):
        exits_to_destination = []
        for ex in exits:
            if loc in exits[ex].values():
                exits_to_destination.append((ex, locations[ex]))
        result.append(exits_to_destination)
    # show diff with comprehension and generator when iterating on generator
    # for x in result:
    #     pass
    return result


def loop_comp():
    result = []
    for loc in sorted(locations):
        exits_to_destination = [(ex, locations[ex]) for ex in exits if loc in exits[ex].values()]
        result.append(exits_to_destination)
    # for x in result:
    #     pass
    return result


def nested_comp():
    exits_to_destination = [[(ex, locations[ex]) for ex in exits if loc in exits[ex].values()]
                            for loc in sorted(locations)]
    # for x in exits_to_destination:
    #     pass
    return exits_to_destination


# can time the functions like this as long as they are funcs without args
print(nested_loop())
print(loop_comp())
print(nested_comp())
result = []
for string in [nested_loop, loop_comp, nested_comp]:
    result.append(timeit.timeit(string, setup, number=1000))
print(result)
