area = 0

def area_of_square(length: float):
    # Declare area is global, python wont make a new local one
    global area
    area = length*length


area = area_of_square(30)
print(f"the area is {area}")



