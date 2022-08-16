# for i in range(1, 11):
#     for j in range(1,11):
#         print(i, i*j)

# write a nested comprehension
for val in [(i,j) for i in range(1,11) for j in range(1,11)]:
    print(f"{i} x {j} = {i*j}")


gen = ((i,j) for i in range(1,11) for j in range(1,11))

# print(next(gen))
# input()
# print(next(gen))
# input()
# print(next(gen))
# input()
# print(next(gen))
# input()