import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

headings = ['album','artist','year']


# for row in albums:
#     zip_object = zip(headings, row)
#     for thing in zip_object:
#         print('\t',thing)
#
# # To create the dict
# album_list = []
# for row in albums:
#     empty_dict = {}
#     for head,value in zip(headings,row):
#          empty_dict[head] = value
#     album_list.append(empty_dict)
#
# filename = 'albums.csv'
# dialect = csv.excel
# print(f"dialect quoting is {dialect.quoting}")
# with open(filename,'w',encoding='utf-8',newline='') as csv_file:
#     writer = csv.DictWriter(csv_file,fieldnames=headings,extrasaction='ignore', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writeheader()
#     writer.writerows(album_list)
#


# His way of doing it
filename = 'albums.csv'

with open(filename,'w',encoding='utf-8',newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headings, quoting= csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for row in albums:
        zip_object = zip(headings, row)
        albums_dict = dict(zip_object)
        writer.writerow(albums_dict)



