import os
import fnmatch as fn
import id3reader_p3 as id3

# return filename of mp3 files
# start is arg + extension as second param
def find_music(root, ext = "emp3"):
    for path, dir, files in os.walk(root):
        for file in fn.filter(files, f"*.{ext}"):
            # create an absolute path
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)

unread = []
for f in find_music('music', 'emp3'):
    try:
        # first few of these pass because fle is big enough that reading tag succeeds
        id3r = id3.Reader(f)
        print(f"Artist: {id3r.get_value('performer')}, "
              f"Album: {id3r.get_value('album')}, "
              f"Track: {id3r.get_value('track')}, "
              f"Song:{id3r.get_value('title')}")
    except OSError:
        unread.append(f)

for error in unread:
    print(error)
