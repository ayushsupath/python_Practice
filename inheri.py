# class Animals(): # this will be your parent class
#     a = 12
    
#     def __init__(self, name):
#         self.name = name

#     def details(self):
#         print(f"Hello your name is {self.name}")


# class Humans(Animals):  # this is your child class
#     pass

# obj = Animals("Lion")

# obj2 = Humans("Shruu")
# obj2.details()
# print(obj2.a)

# your child class objects has all the powers has all the powers to access the attributes and methods of parent class

# Multilevel Inheritance


# class BagFactory:
#     def __init__(self, material, zips, pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def details(self):
#         print("Your bag details are: ")
#         print(self.pockets)
#         print(self.zips)
#         print(self.material)

# class nike(BagFactory):
#     def __init__(self, material, zips, pockets, colours):
#         super().__init__(material, zips, pockets, colours)
#         self.colours = colours

#     def details(self):
#         print(self.colours)
#         return super().details()
    
# class ayu(nike):
#     def __init__(self, material, zips, pockets, colours):
#         super().__init__(material, zips, pockets, colours)



# bag1 = BagFactory("Silk", 2, 3)

# bag2 = nike("pollyster",4,5, "green")


# Multiple inheritance

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Humans:
#     def __init__(self, id):
#         self.id = id
        
# class Robots(Animal, Humans):
#     def __init__(self, name, id):
#         super().__init__(name)
#         super().__init__(id)

# robo = Robots("Ayush", 13)
# print(robo.id)
# print(robo.name)



#PolyMorphism

# def hello():
#     print("Hello are you bro")

# def hello():
#     print("What are you doing bro")


# hello()


# class animal:
#     def speak(self):
#         print("Animal is not speak")

# class Humans:
#     def speak(self):
#         print("we are humans we can speak")


# obj = animal()
# obj2 = Humans()

# obj.speak()
# obj2.speak()

# Method Overriding (Achieving of Mthod overriding we need inheritance)

# class Animals:
#     def __init__(self, name):
#         self.name = name
    
#     def details(self):
#         print(f"your name is {self.name}")

# class Humans(Animals):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def info(self):
#         print("Your info is {self.name} and this is all we have")

# obj = Humans("Harsh")

#when we are doing inheritance and parent and child classes have same method name so the child method will override your parent class method

#method overloading   #they not support in a python

# class hello:
#     def speak(self, a):
#         print("How are you brother")
    
#     def speak(self, a, b):
#         print("Hello how are you bhai")


#Encapsulation

# class Animals:
#     a = 12

# print(Animals.a)


# class Factory:
#     __name = "TATA" #public class attibute
#     _old = 12   #Protected
#     def __init__(self, type, tyre, color):  # Public object attribute
#         self.type = type
#         self.__tyre = tyre  #this is private 
#         self.color = color
    
#     def detail(self):
#         print("Hello your details is :")

# car = Factory("SUV", "MRF", "Black")
# print(car.__name)


#Abstraction
# from abc import ABC, abstractmethod
# class enforce(ABC):
#     @abstractmethod
#     def engineStart():
#         pass

# class bike(enforce):
#     def engineStart():
#         pass

# class car(enforce):
#     def engineStart():
#         pass

# class truck(enforce):
#     def engineStart():
#         pass

# obj1 = bike()
# obj2 = car()
# obj3 = truck()

#dunder method

# class Animals:
#     def __init__(self, name):
#         self.name = name
    
#     def __str__(self):
#         return f"Hello My name is {self.name}"

# obj = Animals("Lion")
# obj2 = Animals("tiger")

# print(obj2)


# class numbers:
#     def __init__(self, num):
#         self.num = num
#     # def __add__(self, other):
#     #     return self.num + other.num

#     def __sub__(self, other):
#         return self.num - other.num

# num1 = numbers(10)
# num2 = numbers(20)

# print(num1 - num2)

# a = 10

# print(type(a))

# print(dir(int))


