shopping_list= ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ['cookies']
print(shopping_list)
print(id(shopping_list))



var = ['Eoin','Conor','Sarah']
other_var = var
other_var += ['Mel','Tony']
print(other_var)
print(var)

# Set multiple values equal to one list
#a,b,c,d,e,f = another_list doesnt work because that is done for multiple returns
a=b=c=d=e=f = another_list

print(a)
# Remember append happens in place!
c.append('Henry')
print(d)






