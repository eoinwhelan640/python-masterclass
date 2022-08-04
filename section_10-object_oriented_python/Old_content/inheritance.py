class Bird:
    def __init__(self):
        self.beak = True
        self.feathers = True
        self.wings = True
        self.legs = 2

    def peck(self):
        print("Bird pecks you")


class flightlessBirds(Bird):
    def __init__(self):
        super().__init__()
        self.fly = False

    def misery(self):
        print('Im miserable' )


class flightBirds(Bird):
    def __init__(self):
        super().__init__()
        self.fly = True

    def fly_away(self):
        print("I can fly")



class Eagle(flightBirds):
    def __init__(self):
        super().__init__()


class Penguin(flightlessBirds):
    def __init__(self):
        super().__init__()

class MultipleInh(flightBirds, flightlessBirds):
    def __init__(self):
        super().__init__()




thing = MultipleInh()

thing.fly_away()
thing.misery()


peng = Penguin()
eagle = Eagle()

print("BIRD")
print(Bird.__dict__)
print('flight and flightless')
print(flightlessBirds.__dict__)
print(flightBirds.__dict__)
print('Penguin and eagle')
print(Penguin.__dict__)
print(Eagle.__dict__)

