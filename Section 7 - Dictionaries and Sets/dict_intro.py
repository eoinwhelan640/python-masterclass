vehicles = {
    'dream':'Honda 250T',
    'roadster':'BMW R1100',
    'er5':'Kawasaki ER5',
    'can-am':'Bombardier Can-Am 250',
    'virago':'Yamaha XV250',
    'tenere':'Yamaha XT650',
    'jimny':'Suzuki Jimny 1.5',
    'fiesta':'Ford Fiesta Ghia 1.4',
}

my_car= vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

# Using get() method
learner = vehicles.get('er5')
print(learner)

for key in vehicles:
    print(key,vehicles[key],sep=',')

# Dictionaries have .items attribute we can call to look at key,value
print((20*'*') + ' TRYING ITEMS METHOD ' + (20*'*'))
for key, value in vehicles.items():
    print(key,value,sep=' ')


vehicles['starfighter'] = 'Lockheed F-104'
vehicles['learjet'] = 'Bombardier Learjet 75'
vehicles['toy'] = 'glider'
print(vehicles)

# change values
vehicles['toy'] = 'EOIN'
print(vehicles)

del vehicles['starfighter']
# This will delete the toy key, and if it doesnt exist it won't fail, it'll return None
out = vehicles.pop('toy',None)
print(out)
# This would throw error if key didnt exist - need to specifiy default or it acts like del
#vehicles.pop('fake_key')
print(vehicles)
# What if we try remove something that doesnt exist ?


