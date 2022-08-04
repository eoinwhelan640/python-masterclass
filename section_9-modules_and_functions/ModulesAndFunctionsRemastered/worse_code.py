area = 0
length= 30

def area_of_square():
    global area
    area = length*length


area = area_of_square()
print(f"the area is {area}")