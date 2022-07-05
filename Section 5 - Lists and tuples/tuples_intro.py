# same thing
# t= "a","b","c"
t = ("a", "b", "c")

print(t)

# need parenthesis when pass as arg to a function
# eg (name,age,python, 2020)
name = "Eoin"
age = 26
print(name, age, "Python", 2020)
# So print one thing, the tuple vs 4 things ^
print((name, age, "Python", 2020))

# brackets or no brackets makes no diff
welcome = "Welcome to my nightmare", 'Alice Cooper', 1975
bad = ("Bad company", "Bad company", 1974)
budgie = "Nightflight", "Budgie", 1981
imelda = ("More Mayhem", "Imelda May", 2011)
metallica = "Ride the lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.5)
print(table[1] * table[2])
# unpack instead to make operations more obvious
name, length, width, height, price = table
print(length * width)

# albums = ["Welcome to my nightmare", 'Alice Cooper', 1975,
#           "Bad company", "Bad company", 1974,
#           "Nightflight", "Budgie", 1981
#           "More Mayhem", "Imelda May", 2011
#           "Ride the lightning", "Metallica", 1984,
#           ]

albums = [("Welcome to my nightmare", 'Alice Cooper', 1975,(('0','first song'),('1','second song'))),
          ("Bad company", "Bad company", 1974,(('0','first song'),('1','second song'))),
          ("Nightflight", "Budgie", 1981,(('0','first song'),('1','second song'))),
          ("More Mayhem", "Imelda May", 2011,(('0','first song'),('1','second song'))),
          ("Ride the lightning", "Metallica", 1984,(('0','first song'),('1','second song')))
          ]

print(albums)

# Me trying to do something
# for album,(x,y) in albums:
#     print('VAL is {}'.format(album))
#     print('X is {}'.format(x))
#     #print('Y is {}'.format(y))
#     #print('Z is {}'.format(z))


# Other way of doing it
# Think about enumerate, we can do ind,val even though enumerate creates a list of tuples, album is the same thing
# for name,artist,year in albums:
#     print("Album: {}, Artist: {}, Year:{} ".format(name,artist,year))


# for album in albums:
#     name,artist,year=album
#     print("Album: {}, Artist: {}, Year:{} ".format(name,artist,year))

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

print(albums)
for name,artist,year,songs in albums:
    print('Album: {}, Artist: {}, Year: {}, Songs: {}'.format(name,artist,year,songs))

print()
album=albums[2]
print(album)

songs=album[3]
print(songs)

song= songs[1]
print(song)
print(song[1])
print(80*'*')
print(albums[1][3][2][1])
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

print(albums[1][3][5][1])
print(albums[2][2])
print(albums[3][3][3][0])
print(albums[2][3][1])