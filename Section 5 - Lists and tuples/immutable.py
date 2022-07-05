# result = True
# another_result= result
# print(id(result))
# print(id(another_result))
#
#
# result=False
# print(id(result))


result = "correct"
another_result=result

print(id(result))
print(id(another_result))
# Strings are immutable, when we add the extra chars a new string is created under the hood, old still exists 
result += "ish"
print(id(result))
print(id(another_result))








