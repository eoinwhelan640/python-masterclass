import os
import fnmatch


def find_albums(root, artist):
    ''' Prints tuple (filepath, albumname)'''
    for path, dir, files in os.walk(root):
        #caps_name = artist.upper()
        for artist in fnmatch.filter(dir, artist):
        #for artist in fnmatch.filter((d.upper() for d in dir), caps_name):
        #for artist in (d f;lr d in dir if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    val1, val2 = os.path.join(album_path, album), album
                    yield val1,val2

def find_songs(albums):
    for album in albums:
        print(f"Album - {album[1]}")
        for song in os.listdir(album[0]): # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "Aerosmith")
# if wanted to use pattern matching
#album_list = find_albums("music", "black*")
#print(album_list)
songs_list = find_songs(album_list)

for s in songs_list:
    print(f"\t\t{s}")

