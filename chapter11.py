# a = ["monday", "tuesday", "wednesday", 1234, 211,221,3221,211,323,211]

# tup = tuple(a)

# print(type(tup))

#it has immutable nature - you cannot change any value inside your tuple 
# print(tup.index("tuesday"))

# print(tup.count(211))

def student():
    return "ayush",24,"ayush@gmail"

info = student()
name , age, mail = info  

print(info)

print(name)