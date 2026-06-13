# class cars:
#     brand = "BMW" # is called Attributes
#     type = "EV"

#     def hello():      # is know as method
#         print("HEllo bro")  


# print(cars.brand)
# cars.hello()

    

#Objectss

# class Bags:
#     name = "Ayushsupath"


#     def details(self):
#         print("Hello this is a Company who creats a BAgs")

# nike = Bags()

# print(nike.name)

# nike.details()


# Constructors

# class Bags():
#     def __init__(self, material, zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    

# nike = Bags("Silk", 3, 2)
# ayuu = Bags("leather",4,5)

# print(nike.material)
# print(nike.pockets)
# print(nike.zips)
# print(ayuu.material)
# print(ayuu.pockets)
# print(ayuu.zips)



class Animal:
    a = 12;  #this is a class attributes

    def __init__(self, name):    # this is called instant attributes
        self.name = name
            

    def hello(self): #instance method captures the location of object
        print(f"Hellooooo, my name is {self.name}")

    @classmethod
    def details(cls):   #this think capture the location of class
        print("Hello How are you bro")


    @staticmethod
    def speak(): # this is a static method and it will not target any location
        print("Hello i am a static method")


obj = Animal("Dog")

# print(obj.name)

obj.hello()
