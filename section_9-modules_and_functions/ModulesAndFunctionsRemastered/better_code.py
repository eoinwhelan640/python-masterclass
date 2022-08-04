# never do this way
# def area_of_square(length: float):
#     # Declare area is global, python wont make a new local one
#     global area
#     area = length*length

def area_of_square(length: float) -> float:
    # Declare area is global, python wont make a new local one
    return length*length

# So only run this on main script, rule it OUT of other places
if __name__ == '__main__':
    area = area_of_square(30)
    print(f"the area is {area}")
    print(f"in better_code.py, __name__ is {__name__}")