# jabber = open('Jabberwocky.txt','r')
# print(jabber)
# for line in jabber:
#     print(line.rstrip())
# jabber.close()


# using with
# with open('Jabberwocky.txt','r') as jabber:
#     for line in jabber:
#         print(line.rstrip())

# Using readlines()
# print("Doing readlines")
# with open('Jabberwocky.txt','r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
#
# print("Doing read")
# with open('Jabberwocky.txt','r') as jabber:
#     text = jabber.read()
#
# print(text)
#
# #lastly readlines
# print("Doing readline")
# with open('Jabberwocky.txt','r') as jabber:
#     while True:
#         line = jabber.readline().rstrip()
#         print(line)
#         if 'jubjub' in line.casefold():
#             break
#
#
# print(80*'-')
# # equivlent to
#
with open('Jabberwocky.txt', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())
