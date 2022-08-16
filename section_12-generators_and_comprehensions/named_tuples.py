from data import basic_plants_list, plants_list, plants_dict

print(plants_list[0])
# for plant in basic_plants_list:
#     print(plant[0])

for plant in plants_list:
    print(plant.name)


print(plants_dict["Andromeda"])

example = plants_list[0]
example = example._replace(lifecyle="Annual")