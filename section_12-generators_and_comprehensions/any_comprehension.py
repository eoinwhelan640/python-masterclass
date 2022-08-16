from data import people, basic_plants_list, plants_list, plants_dict


# writing an email and choose whos getting the email from contacts email

# Check everyone has an email
if all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit list of receipts")


# check at least one planttype in a group is a grass
# use named tuple here for easy access to plant.plant_type field
if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This plant contains grass")
else:
    print("No grasses in this pack")


# Challenge - use any & comprehension to check plant in plants dict to see if theres grasses there
print("-"*80)
print(plants_dict)
#any(["Grass" == val.plant_type for name,val in plants_dict.items()])

# Remember you dont have to loop over dict or dict items, can directly loop over the values!!
# Using a generator expression here instead of a comprehension to save memory
# generate at time of instead of one huge list, all use less memory
if any((plant.plant_types == "Grass" for plant in plants_dict.values())):
    print("This dict has grass")
else:
    print("No grass")
