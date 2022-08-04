import csv
filename='country_info.txt'


# this doesntw ork cos you're loading as one string then trying to stip that whoile thing, so individual bits dont get
# stripped
# with open('country_info.txt') as country_info:
#     text = country_info.read()
# print(text.strip('\n').split('|'))

# with open(filename) as country_info:
#     text = [line.strip('\n').split('|') for line in country_info.readlines()]
#
# print(text)

# Create a dictionary out of our loaded data
# countries = {}
# with open(filename) as country_file:
#     # Doing this reads the first level
#     country_file.readline()
#     # So when you start here, you're doing from the second line onward
#     for row in country_file:
#         data = row.strip('\n').split('|')
#         country,capital,code,code3,dialing,timezone,currency = data
#         country_dict = {
#                 'name':country,
#                 'capital':capital,
#                 'country_code':code,
#                 'cc3':code3,
#                 'dialing_code':dialing,
#                 'timezone':timezone,
#                 'currency':currency,
#             }
#         countries[country.casefold()] = country_dict
#         #countries[code.casefold()] = country_dict
#         # using a tuple to see how that works
#         #countries[(country.casefold(),code.casefold())] = country_dict



# while True:
#     chosen_country = input("Please choose a country: ").casefold()
#     #chosen_country = tuple([i.strip() for i in ''.join(chosen_country).split(',')])
#     if chosen_country in countries:
#         country_data = countries[chosen_country]
#         [print(f"{k}: {v}") for k,v in country_data.items()]
#     elif chosen_country == 'exit':
#         print('Exiting...')
#         break
#


