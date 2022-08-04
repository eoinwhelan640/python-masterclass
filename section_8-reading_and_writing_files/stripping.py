filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'Twasebv"
no_apostrophe = first.strip(chars)
print(no_apostrophe)


# Write a remove prefix & remove suffix function

# char = "'Twas"
# print(first.split(char)[1])
#
# def removeprefix(string:str, prefix:str) -> str:
#     if string.startswith(prefix):
#         return string[len(prefix):]
#     else:
#         return string[:] # remove a copy of string
#
#
# def removesuffix(string,suffix):
#     if string.endswith(suffix):
#         return string[:-len(prefix)]
