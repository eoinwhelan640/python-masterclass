a = 12
b= 3


print(a + b)
print(a - b)
print(a*b)
print(a/b)
print(a//b) # integer division, rounded down
print(a % b) # modulo, the remiander after division

####### Sequence operators
string1 = "He's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords "

print(string1 + string2 + string3 + string4 + string5)
print("He's " "probably " "pining " "for the " "fjords")
print("He's" ,"probably", "pining","for the" ,"fjords")

print("Hello" * 5)

today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in "fjord")

# replace fields
age=24
print("My age is {} years".format(age))

print("There are {0} days in {1},{2},{3},{4},{5},{6} and {7}"
      .format(31,"Jan","Mar","May","Jul","Aug","Oct","Dec"))

print("Jan:{2}, Feb:{0}, Mar:{2}, Apr:{1}, May:{2}, June:{1}, July:{2}".format(28,30,31))

print("""Jan:{2}
Feb:{0}
Mar:{2}
Apr:{1}
May:{2}
June:{1}
July:{2}""".format(28,30,31))


# String formatting with replacement fields
for i in range(0, 13):
    print("Number {0:2} squared is {1:<3}, cubed is {2:<4}".format(i,i **2, i**3))


print("Pi is approx {0:12}".format(22/7))
print("Pi is approx {0:12f}".format(22/7))
print("Pi is approx {0:12.50f}".format(22/7))
print("Pi is approx {0:52.50f}".format(22/7))
print("Pi is approx {0:62.50f}".format(22/7))
print("Pi is approx {0:72.50f}".format(22/7))

# f strings

age= 24
name='Eoin'
#print(name + " is" + age + " years old")

print(f"{name} is {age} years old")

print(f"Pi is approx {22/7:12f}")

# interpolation
# d signifies an integer
print("My age is %d years" % age)

major = "years"
minor="months"
print("My age is %d %s, %d %s" %(age,major,6,minor))
print("PI is approx %f" % (22/7))