"""Module for investigating importing and namespace"""

from better_code import area_of_square
import better_code
import supported_hashes

area = better_code.area_of_square(40)
#area = area_of_square(40)
#print(area)

print('Global namespace')
print(__name__)
print(globals())
namespace = globals().copy()
for name,obj in namespace.items():
    print(name, obj)


