trial_1 = {"Bob","Charlie","Georgia","John"}
trial_2 = {"Anne","Charley","Eddie","Georgia"}


print(trial_1.intersection(trial_2))


farm_animals = {"sheep","hen","cow","horse","goat"}
wild_animals = {"lion","elephant","tiger","goat","panther","horse"}
potential_rides = {"donkey","horse","camel"}

# intersection of all three sets
mounts = potential_rides.intersection(farm_animals,wild_animals)
print(mounts)

# using the operator
mounts = potential_rides & farm_animals & wild_animals
print(mounts)

# potential_rides.intersection_update(farm_animals,wild_animals)
# print(potential_rides)


# Challenge - split the quote into words and see which ones are prepositions using intersection
text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Dont actually need to use set here, remember the keyword versions of intersection/union etc can acdept lists
#preps_used = prepositions.intersection(set(text.split()))
preps_used = prepositions.intersection(text.split())
print(preps_used)

# Using the operator &
preps_used = prepositions & set(text.split())
print(preps_used)