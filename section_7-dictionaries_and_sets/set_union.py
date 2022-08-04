# farm_animals = {"sheep","hen","cow","horse","goat"}
#
# wild_animals = {"lion","elephant","tiger","goat","panther","horse"}
#
# print(farm_animals | wild_animals)

from prescription_data import adverse_interactions
meds_to_watch = set()

# for interaction in adverse_interactions:
#     #meds_to_watch = meds_to_watch.union(interaction)
#     #meds_to_watch = meds_to_watch | interaction
#     #meds_to_watch |= interaction
#     meds_to_watch.update(interaction)

# This does the same thing but obvs looks shite, dont do this way. Unpack with tuple
# meds_to_watch.update(adverse_interactions[0],
#                      adverse_interactions[1],
#                      adverse_interactions[2],
#                      adverse_interactions[3],
#                      adverse_interactions[4],
#                      adverse_interactions[5],
#                      adverse_interactions[6],
#                      adverse_interactions[7])

# Do it this way
print("START HERE")
# This is a really good way to see how a tuple is unpacking, or what its made up of. Print each part on a new line
# and you'll see what one level is made up of, and what could be unpacked from there

print(*adverse_interactions, sep="\n")
meds_to_watch.update(*adverse_interactions)
print("MEDS TO WATCH")
print(*meds_to_watch,sep ="\n")


# neat trick to print out visually