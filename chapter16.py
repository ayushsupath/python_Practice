#Decorators

# def extragreeting(func):
#     def wrapper():
#         print("Hello from the AYUSH")
#         func()
#         print("Thankyou visit again")
    
#     return wrapper


# @extragreeting
# def greetings():
#     print("good moring")

# greetings()


#*args and **kwargs


# def add(*args):
#     s = 0
#     for i in args:
#         s = s + i
#     return s

# print(add(10,20, 80))


# def information(**kwargs):
#     return kwargs

# print(information(name = "Ayush", age = 23, size = 11))


# Comprehensions - one liners

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# b = [i for i in a if i % 2 == 0]

# # for i in a:
# #     if i % 2 == 0:
# #         b.append(i)

# print(b)

# Lambda Functions

# check = lambda x: print("Even Number") if x % 2 == 0 else print("odd number")

# add = lambda x,y: print(x  + y)
# add(1 , 2)


# # def check(a):
# #     if a % 2 == 0:
# #         print("Even Number")
# #     else:
# #         print("Odd Number")

# check(12)



# MAP()
# a = ["ayush", "shrutie", "shraddha", "ABby"]
# lengths = list(map(len, a))

# print(lengths)

# for i in a:
#     print(len(i))


# temp = [0,20,30,35]

# def converter(a):
#     far = (a * 9/5) + 32
#     return far

# # for i in temp:
# #     print(converter(i))

# temp_far = list(map(converter, temp))

# print(temp_far)


# Filter()

# m = [35,80,80,12,60,49]

# passed = list(filter(lambda x : x >= 40, m))

# print(passed)


# ZIP()

name = ["ayush", "shruu", "billu", "raju"]

marks = [10,90,32,11]

result = list(zip(name, marks))

print(result)