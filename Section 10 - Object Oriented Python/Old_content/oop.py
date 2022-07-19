# a = 12
# b = 10
# print(a + b)
# print(a.__add__(b))


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)


Kettle.switch_on(kenwood)
print(kenwood.on)


print("*"*80)
kenwood.power = 1.5
print(kenwood.power)

print("*"*80)
Kettle.power_source = "atomic"
hamilton.power_source = "Solar"
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
