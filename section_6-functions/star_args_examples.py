numbers = (0,1,2,3,4,5)
# print(numbers)
# print(*numbers)
# print(0,1,2,3,4,5)


# The star indiates that this arg will be replaced by an unpacked tuple.
# ie when we're invoking the function, we can pass
def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(0,1,2,3,4,5)

# Could also do no value for *args and it'll still work
# def test_star(*args,test):
#     print(args)
#     print(test)
#
#
# test_star(test=(0,1,2,3,4,5))