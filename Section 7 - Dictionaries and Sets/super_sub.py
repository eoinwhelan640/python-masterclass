animals = {"turtle","seagull","horse","robin","python","swallow","hedgehog","wren","aardvark","cat"}

birds = {"robin","swallow","wren"}


print(f"birds is a subset of animals: {animals >= birds}")
print(f"animals is a superset of birds: {animals > birds}")


# print(f"birds is a subset of animals: {birds.issubset(animals)}")
# print(f"animals is a superset of birds: {animals.issuperset(birds)}")
