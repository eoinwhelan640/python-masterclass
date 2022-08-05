class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('Weee this is fun')
        elif self.ratio == 1:
            print("This is hard work, but i'm flying")
        else:
            print("I think I'll just walk")


class Duck:

    def __init__(self):
        self._wing = Wing(1.8)


    def walk(self):
        print('Waddle Waddle Waddle')

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack Quack")

    def fly(self):
        self._wing.fly()


class Penguin:
    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print('Waddle Waddle, I Waddle Too')

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'avin a larf? I'm a penguin")

    def aviate(self):
        print("I won the lotto and bought a G6")

class Mallard(Duck):
    pass


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError(f"Cannot add Duck, are you sure it's not a {str(type(duck).__name__)}")

    def migrate(self):
        my_error = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("testing exception handler in migrate") #TODO remove this before release
            except AttributeError as error:
                print("One duck down")
                my_error = error
        if my_error:
            raise my_error



if __name__ == '__main__':
    donald = Duck()
    donald.fly()
