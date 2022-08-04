# current_choice= "0"
# computer_parts = [] # create empty list
# parts_dict = {'1': 'computer','2': 'monitor','3': 'keyboard','4': 'mouse','5': 'mouse mat','6':' HDMI cable'}
# while current_choice != '0':
#     if current_choice in "123456":
#         if current_choice not in computer_parts:
#             print('Adding {} to shopping list'.format(parts_dict[current_choice]))
#             computer_parts.append(parts_dict[current_choice])
#     else:
#         print('Please add options from the list below: ')
#         print("1: computer\n2: monitor\n3: keyboard\n4: mouse\n5: mouse mat\n6: HDMI cable\n0: to finish ")
#     current_choice = input()
# else:
#     print('Final list {}'.format(computer_parts))
#
#
# # Iterate over the list
# available_parts = ['computer','monitor','keyboard','mouse','mouse mat','HDMI cable']
# current_choice= "0"
# computer_parts = [] # create empty list
# while current_choice != '0':
#     if current_choice in "123456":
#         if current_choice not in computer_parts:
#             print('Adding {} to shopping list'.format(parts_dict[current_choice]))
#             computer_parts.append(parts_dict[current_choice])
#     else:
#         print('Please add options from the list below: ')
#         for part in available_parts:
#             print("{0}:{1}".format(available_parts.index(part)+1,part))
#     current_choice = input()
# else:
#     print('Final list {}'.format(computer_parts))
#
#
# # Iterate over the list - use enumerate
# available_parts = ['computer','monitor','keyboard','mouse','mouse mat','HDMI cable']
# current_choice= "0"
# computer_parts = [] # create empty list
# while current_choice != '0':
#     if current_choice in "123456":
#         if current_choice not in computer_parts:
#             print('Adding {} to shopping list'.format(available_parts[-1+int(current_choice)]))
#             computer_parts.append(available_parts[-1+int(current_choice)])
#     else:
#         print('Please add options from the list below: ')
#         for i,part in enumerate(available_parts):
#             print("{0}:{1}".format(i+1,part))
#     current_choice = input()
# else:
#     print('Final list {}'.format(computer_parts))
#
#
#
# # Same again but would list cmprehension
# print('*'*80)
# # available_parts = ['computer','monitor','keyboard','mouse','mouse mat','HDMI cable']
# # valid_choice =[str(i) for i in range(0,1 + len(available_parts))]
# # print(valid_choice)
# # current_choice= "-"
# # computer_parts = [] # create empty list
# # while current_choice != '0':
# #     if current_choice in valid_choice:
# #         item = available_parts[-1+int(current_choice)]
# #         if item not in computer_parts:
# #             print('Adding {} to shopping list'.format(item))
# #             computer_parts.append(item)
# #     else:
# #         print('Please add options from the list below: ')
# #         for i,part in enumerate(available_parts):
# #             print("{0}:{1}".format(i+1,part))
# #     current_choice = input()
# # else:
# #     print('Final list {}'.format(computer_parts))
# #
#
# # challenge
# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac - Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]
# flowers = [fl for fl in data if 'Flower' in fl]
# shrubs = [fl for fl in data if 'Flower' not in fl]
# print(flowers)
# print(shrubs)
# # for item in enumerate(data):
# #     if 'Flower' in item:
# #         flowers += item
# #     else""
# #         shrubs += item
#
# # write your code here


## Adding code to remove element from list
current_choice= "a"
computer_parts = [] # create empty list
parts_dict = {'1': 'computer','2': 'monitor','3': 'keyboard','4': 'mouse','5': 'mouse mat','6':' HDMI cable'}
price_dict = {'computer':200,'monitor':100,'keyboard':20,'mouse':10,'mouse mat':5,'HDMI cable':15}

# while current_choice != '0':
#     if current_choice in "123456":
#         part = parts_dict[current_choice]
#         if part not in computer_parts:
#             print('Adding {} to shopping list'.format(part))
#             computer_parts.append(parts_dict[current_choice])
#         else:
#             computer_parts.remove(parts_dict[current_choice])
#             print('Removing {} from shopping list'.format(part))
#         print('Your list is now {}'.format(computer_parts))
#     else:
#         print('Please add options from the list below: ')
#         print("1: computer\n2: monitor\n3: keyboard\n4: mouse\n5: mouse mat\n6: HDMI cable\n0: to finish ")
#     current_choice = input()
# else:
#     print('Final list {}'.format(computer_parts))


# Modify the above to also tally the price