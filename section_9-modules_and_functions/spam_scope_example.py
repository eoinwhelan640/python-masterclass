def spam1():

    def spam2():


        def spam3():
            z = "even "
            z += y
            print(f"In spam3, locals are {locals()}")
            return z

        y = "more " + x
        y += spam3()
        print(f"In spam2, locals are {locals()}")
        return y

    # Doing the commented out part would break the code, cos then x isnt defined yet and cant be
    # used in spam2 as a free variable
    x = "spam " #+ spam2()
    #x += spam2()
    print(f"In spam1, lcals are {locals()}")
    return x


print(spam1())



# This contradicts what we learned before
def my_func():
    A = 10
    def other_func():
        print(A)
    print("done")

my_func()