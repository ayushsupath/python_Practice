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


def information(**kwargs):
    return kwargs

print(information(name = "Ayush", age = 23, size = 11))

