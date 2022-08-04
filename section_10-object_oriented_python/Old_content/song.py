import csv

# with open('albums.txt', encoding='utf-8', newline='') as csv_file:
#     # sample = ""
#     # for line in range(3):
#     #     sample += csv_file.read()
#     # print(sample)
#     #headings = ['artist','album','year','song']
#     reader = csv.reader(csv_file, delimiter='\t')
#     for row in reader:
#         print(*tuple(row))


class Song():
    """ Class to represent a song

    Attributes:
        title (str): The title of the song
        artist: The name of songs creator.
        duration (int): The duration of the song in seconds. may be zero
    """
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


#help(Song)
# print(Song.__doc__)
# print(Song.__init__.__doc__)
# Song.__init__.__doc__ = """ xyz """


class Album:
    """Class to represent an album, using it's track list

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (str): The name of the artist
        the artist will default to an artist with the name 'Various Artists'.
        tracks: (List[Song]): A list of songs on the album

    Methods:
        addSong: Used to add a new song to the album's tracklist
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []


    def add_song(self, song, position = None):
        """ Adds a song to the track list

        Args:
            song (Song): the title of a song to add
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added to the end of the list
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Basic class to store artist details

    Attributes:
        name (str): name of the artist
        albums (List[Album]): A list of the albums by this artist
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artists's published albums
    Methods:
        add_album: use to add a new album to the artist's album list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album object to add to the list.
                If the album is already present, it will not be added again (although this is yet to be implemented)
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """ Add a new song to the collection of albums

        This method will add the song to an album in the collection
        A new album will be created in the collection if it doesnt already exist.

        Args:
            name (str): The name of the album
            year (int): The year the album was produced
            title (str): The title of the song
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            #print(f"SELF IS {self}")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)



def find_object(field, object_list):
    """Check `object_list` to see if an object with a `name` attribute equal to `field` exists, returns it if found"""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []
    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_filed = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

        return artist_list





# Non OOP designed function
# def load_data():
#     new_artist = None
#     new_album = None
#     artist_list = []
#
#     with open("albums.txt","r") as albums:
#         for line in albums:
#             artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
#             year_filed = int(year_field)
#             print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))
#
#             if new_artist is None:
#                 new_artist = Artist(artist_field)
#                 artist_list.append(new_artist)
#
#             elif new_artist.name != artist_field:
#                 # this is us reading details for new artist
#                 # retrieve artist object if there is one
#                 # otherwise create new artist object
#                 new_artist = find_object(artist_field, artist_list)
#                 if new_artist is None:
#                     new_artist = Artist(artist_field)
#                     artist_list.append(new_artist)
#                 new_album = None
#
#             if new_album is None:
#                 new_album = Album(album_field, year_field, new_artist)
#                 new_artist.add_album(new_album)
#             elif new_album.name != album_field:
#                 # We've just read a new album for the current artist
#                 # retrieve the album object if there is one
#                 # Otherwise create a new album object and store it in Artists collection
#                 new_album = find_object(album_field, new_artist.albums)
#                 if new_album is None:
#                     new_album = Album(album_field, year_field, new_artist)
#                     new_artist.add_album(new_album)
#
#             # create a new song object and add it to albums collection
#             new_song = Song(song_field, new_artist)
#             new_album.addSong(new_song)
#
#         return artist_list


# my attempt
# def load_data():
#     artists = []
#     artists_list = []
#     artists_to_albums = {}
#     with open('albums.txt',encoding='utf-8', newline='') as csv_file:
#         reader = csv.reader(csv_file, delimiter='\t')
#         for row in reader:
#             artist, album, year, song = tuple(row)
#             if not artist in artists_to_albums:
#                 artists_to_albums[artist] = []
#             # Its breaking here, because once we add our current artist to the list of artists, we never update our
#             # current artist again. ie after round one, current artist will always be true
#             # Need to update current artist or else not use it
#             if not artist in artists_list:
#                 current_artist = Artist(artist)
#                 artists.append(current_artist)
#                 artists_list.append(artist)
#
#             # current_artist will always be populated, whenever we have a new row we want to check if this album
#             # is already recorded
#             if not album in artists_to_albums[artist]:
#                 # Add the current album to our list of albums
#                 current_album = Album(album, int(year), current_artist)
#                 current_artist.add_album(current_album)
#                 artists_to_albums[artist].append(album)
#
#
#             current_song = Song(song, current_artist)
#             current_album.addSong(current_song)
#
#     return artists


def create_checkfile(artist_list):
    """ Create a checkfile from the object data for comparison with original file"""
    with open('checkfile.txt', 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(f"{new_artist.name}\t{new_album.name}\t{new_album.year}\t{new_song.title}", file=checkfile)



if __name__ == '__main__':
    artists = load_data()
    print(f"There are {len(artists)} artists")
    create_checkfile(artists)

