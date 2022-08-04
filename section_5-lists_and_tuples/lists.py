

#  Start section 5 - lists
l= "abcdefgh"

# print(l.__iter__)
# print(l.__getitem__)

computer_parts =["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "mouse mat"]


# replacing parts on a list
print(computer_parts)
#computer_parts[3] = 'trackball'
#print(computer_parts)

# replace a slice - this wont work
# print(computer_parts[3:])
# computer_parts[3:] = "trackball"
# print(computer_parts)
# this does work
# print(computer_parts[3:])
# computer_parts[3:] = ["trackball"]
# print(computer_parts)
#
# print(list('eoin') == ['eoin'])


# What if we wanted to delete items ??
data = [4,5,104,105,110,120,130,140,150,160,183,1000, 2000]
# del data[0:2]
# print(data)
# del data[-2:]
# print(data)

min_valid=100
max_valid=200
# print(data)
#
# # process the low values in the list
# # work through every value until a value breaks threshold
# # Use that value to index in our delete
# stop=0
# for ind, val in enumerate(data):
#     if val >= min_valid:
#         stop = ind
#         break
# print(stop)
# del data[:stop]
# print(data)
#
# # process high values in list
# # work backwards
# # starting out its a good idea to print index numbers
# for ind in range(len(data) - 1,-1,-1):
#     print('We\'re on index {}'.format(ind))
#     if val <= max_valid:
#         #start = ind
#
#         start = ind + 1
#         break
# print(stop)
# # needs to be +1 off the index we get, cos thats the first item we wanna delete, so need to go back one to start from
# #del data[stop + 1:]
# del data[start:]


# Do the top and bottom in one go
# for ind,val in enumerate(data):
#     if not min_valid<= val <= max_valid:
#         if val >= min_valid:

# high,low =[],[]
# for ind,val in enumerate(data):
#     if min_valid >= val:
#         low.append(1+ind)
#     elif val >= max_valid:
#         high.append(ind)
#
# #print(data[:max(low)])
# #print(data[min(high):])
# #print(data[max(low):min(high)])
# # this would delete everything except the indexs
# #del data[max(low):min(high)]
# print(data[:max(low):min(high):])
# #print(data)


#How would we delete thngs working backwards
data= [104,101,4, 105, 308, 103, 5, 107, 100, 306, 106, 102, 108]
min_valid=100
max_valid=200

# Working backwards means you wont mess up any idexes by deleting at the end
# So go around the loop, delete the object where you see it
# The n because we're moving backwards, ie start at 10 and go down toward 0, we always move down
# one index at a time, and delete one at a time, so its impossible for index to go ou of range
# for ind in range(len(data)-1,-1,-1):
#     print('index is {}'.format(ind))
#     if data[ind] <= min_valid or data[ind] > max_valid:
#         print(ind,data)
#         del data[ind]



# Use a differnt type of reversal method
# reversed()
# Use this top thing to get back the original idexes for when we wanna delete things from real list using reverse list
top_ind=len(data)-1
for ind,val in enumerate(reversed(data)):
    if val < min_valid or val > max_valid:
        print(top_ind - ind,val)
        del data[top_ind - ind]





