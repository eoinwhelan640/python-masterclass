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

# jukebox application
# album_choice = int(input('Choose Your Album: '))
# name,artist,year,songs = albums[album_choice]
# print('Choose Your Song from {}: '.format(name))
# for ind,song in songs:
#     print('[{}] {}'.format(ind,song))
# song_choice = int(input('Choose number: '))
# print('Now playing: {}'.format(songs[song_choice][1]))

# Now what way would you mae this run in a loop ??
# while True:
#     print('Choose your album:')
#     for ind,items in enumerate(albums):
#         print('[{}] {}'.format(ind+1,items[0]))
#     album_choice = -1+int(input('Choice: '))
#     if album_choice >= len(items):
#         print('Exiting...')
#         break
#     name,artist,year,songs = albums[album_choice]
#     print('Choose Song from {}: '.format(name))
#     for ind,song in songs:
#         print('[{}] {}'.format(ind,song))
#     song_choice = -1+int(input('Choose Number: '))
#     if song_choice >= len(songs):
#         print('Exiting...')
#         break
#     print('Now playing: {}'.format(songs[song_choice][1]))
#     print('*'*80)



# How he does it
#from tuples_intro import albums

# this is a constant
# Python convention for constants
# SONGS_LIST_INDEX = 3
# SONG_TITLE_INDEX = 1
# while True:
#     print("Please choose your album (invalid choice will exit):")
#     for ind, (title,artist,year,songs) in enumerate(albums):
#         print("[{}]: {} - {}: ".format(ind+1,artist,title))
#     choice = int(input())
#     if 1<= choice <= len(albums):
#         songs_list = albums[choice -1][SONGS_LIST_INDEX]
#     else:
#         break
#     print('Please choose a song: ')
#     for ind, (track_number, song) in enumerate(songs_list):
#         print('[{}] {}'.format(ind+1, song))
#
#     song_choice = int(input())
#     if 1 <= song_choice <= len(songs_list):
#         title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
#     else:
#         break
#     print('Playing: {}'.format(title))
#     print('='*40)


# Challenge - if wrong number is chosen for songs, have it go back to start
# while True:
#     print('Choose your album:')
#     for ind,items in enumerate(albums):
#         print('[{}] {}'.format(ind+1,items[0]))
#     album_choice = -1+int(input('Choice: '))
#     if album_choice >= len(items):
#         print('Exiting...')
#         break
#     name,artist,year,songs = albums[album_choice]
#     print('Choose Song from {}: '.format(name))
#     for ind,song in songs:
#         print('[{}] {}'.format(ind,song))
#     song_choice = -1+int(input('Choose Number: '))
#     if song_choice >= len(songs):
#         print('Invalid choice, resetting...')
#         continue
#     print('Now playing: {}'.format(songs[song_choice][1]))
#     print('*'*80)

# Another way we could do it, is not to have an explcit continue statement, but reverse the if to be the oppsoite,
# and include the prinrt within that block, so if it fails it just repeats the while loop.
# Not overly keen on this though cos you get no messages about an invalid choice
# Diff between explcitly coding behaviour vs letting it be implcit 
while True:
    print('Choose your album:')
    for ind,items in enumerate(albums):
        print('[{}] {}'.format(ind+1,items[0]))
    album_choice = -1+int(input('Choice: '))
    if album_choice >= len(items):
        print('Exiting...')
        break
    name,artist,year,songs = albums[album_choice]
    print('Choose Song from {}: '.format(name))
    for ind,song in songs:
        print('[{}] {}'.format(ind,song))
    song_choice = -1+int(input('Choose Number: '))
    if not song_choice >= len(songs):
        print('Now playing: {}'.format(songs[song_choice][1]))
        print('*'*80)

