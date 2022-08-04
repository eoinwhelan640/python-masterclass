even = [2,4,6,8]
odd = [1,3,5,7,9]

#
# print(min(even))
# print(odd.max())
# print()
# # handy for counting item occurence in a list without for looping
# print("mississipi".count('s'))
# print("mississipi".count('iss'))


# even.extend(odd)
# print(even)
# another_even= even
# print(another_even)
#
# even.sort(reverse=True)
# print(even)
# # So REMEMBER, when you set a variable equal to another varaiable, its bound to that variable not the underlying value
# print(another_even)

empty_list=[]
#numbers= even + odd
numbers= [even,odd]
print(numbers)

# sorted_numbers= sorted(numbers)
# print(sorted_numbers)
#
#
# # can take a copy of list in many ways
# # Copy is best way since pythion3.3
# # Lots of code online will have come from old python, so uses sliciong [:] etc cos it still works well
# more_numbers = numbers.copy()
# #more_numbers = list(numbers)
# #more_numbers = numbers[:]
# print(more_numbers)
#
#print elements of a nested list
for ind,lst in enumerate(numbers):
    print('Printing {} list'.format(ind+1))
    for j in lst:
        print('Element {}'.format(j))



