available_parts = {
    '1':'computer',
    '2':'monitor',
    '3':'keyboard',
    '4':'mouse',
    '5':'hdmi cable',
    '6':'dvd drive',
}
# My way
# current_choice = None
# Challenge
# while current_choice != '0':
#     if current_choice in available_parts:
#         chosen_part = available_parts[current_choice]
#         print(f"Adding {chosen_part}")
#     else:
#         print(f'{current_choice} is an invalid choice')
#     [print(f"[{k}]: {v}") for k,v in available_parts.items()]
#     current_choice = input('> ')
# else:
#     print('Exiting...')

# His way - makes sense to only printr menu when chose invalid option
current_choice = None
# Challenge
while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
    else:
        print(f'Please select an option from the list')
        for key,value in available_parts.items():
            print(f"{key}: {value}")
        print('0: To Finish')
    current_choice = input('> ')

