# turtle is pretty unique code so can import this way, dont do it usually
#from turtle import *
import turtle
import math
#from math import radians, cos



# turtle.pendown()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.done()
def encircled_square(length: int) -> None:
    """Draws a square then encloses it in a circle"""
    square(length)
    angle = math.radians(45)
    radius = length * math.cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    print(f'Inside function, the scope is {dir()}')

def square(length: int) -> None:
    """Draws a square of length `length"""
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)


#turtle.speed("fast")
#encircled_square(300)
# for s in range(72):
#     encircled_square(120)
#     turtle.circle(100)
#     turtle.left(5)
#turtle.done()

print(f"Default scope is {f'{dir()}':>190}")
# print(f"Outside the function the scope is {dir(encircled_square)}")
g = globals()
print(g['square'])
print(dir(__builtins__))

print(80*'*')
