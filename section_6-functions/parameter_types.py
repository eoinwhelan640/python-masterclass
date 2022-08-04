# Function with each type of arg
# p1,p2 are positional args
# *args
# k is keyword parameter, nees to be passed with it's keyword (because its after the variable args obvs)
# **kwargs "var keyword parameter". Also called keyword args - these are optional keyword args
def func(p1,p2,*args,k, **kwargs):
    print('positional-or-keyword:...{}, {}'.format(p1,p2))
    print('var-positional (*args):..{}'.format(args))
    print('keyword:.................{}'.format(k))
    print('var-keyword:.............{}'.format(kwargs))

func(1,2,3,4,5,k=6,key1=7,key2=8)

print(80*'*')
def sum_numbers(*args: tuple) -> float:
    '''
    Sum all numbers passed to function

    :param args: tuple of numbers to be summed
    :return: cumulative sum of input tuple
    '''
    out = 0
    for n in args:
        out += n
    return out

print(sum_numbers(2,3,4))
print(sum_numbers(0,10,20))
print(sum_numbers(0,0,0))
print(sum_numbers(1))
print(sum_numbers())


# His solution
def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    result = 0
    for number in values:
        result += number
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))


# Way better solution
def sum_numbers(*values: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    return sum(values)
