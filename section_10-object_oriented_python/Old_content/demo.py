# a_string = "this is \na string split\t\tand tabbed"
# print(a_string)
#
# b_string = r"this is \na string split\t\tand tabbed"
# print(b_string)


class boyfriend:
    def __init__(self, age, height, name):
        self.age = age
        self.height = height
        self.name = name


class girlfriend:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def make_bf(self, bfage, bfheight, bfname):
        print(self)
        bf = boyfriend(bfage, bfheight, self)
        return bf.name


anet = girlfriend(27, "Annette")
eoin = anet.make_bf(100, 200, 'Eoin')
print(eoin)
# print(eoin.age)
# print(eoin.height)

