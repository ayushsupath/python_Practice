# if True:
#     print("Hello How are you brother?")

# input_age = int(input("What is your age?: "))
# if input_age >= 18:
#     print("Bhai tu Vote de skta he")
# else:
#     print("Bhai tu abhi chhota he, tu vote nhi de skta")

# rupees = int(input("Mummy give me some money:"))
# if rupees == 10:
#     print("I will buy a Chips")
# elif rupees == 50:
#     print("I will buy a Shawarma")
# elif rupees == 100:
#     print("I will buy a Burger")
# elif rupees == 500:
#     print("I am going to buy a Shirt")
# else:
#     print("Thank you Mummy for giving me some money")


#Question 1:

# num1 = int(input("Give me 1st number:"))
# num2 = int(input("Give me 2nd number:"))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print(f"{num1} and {num2} are equal")


# gender = str(input("What is your gender?: "))
# if gender == "Male":
#     print("Hello Brother, Good Morning")
# elif gender == Female:
#     print("Hello Sister, Good Morning")
# else:
#     print("Other")

# num = int(input("Give me a number: "))
# if num % 2 == 0:
#     print(f"{num} is an Even number")
# else:
#     print(f"{num} is an Odd number")

# name = str(input("What is your name?: "))
# age = int(input("What is your age?: "))

# if age >= 18:
#     print(f"Hello {name}, your are eligible for a vote!")
# else:
#     print(f"Hello {name}, your can vote after {18 - age} years!")

# year = int(input("Enter a year: "))
# if (year % 100 == 0 and year % 400 == 0):
#     print(f"{year} is a Leap year")
# elif(year % 100 != 0 and year % 4 == 0):
#     print(f"{year} is a Leap year")
# else:    print(f"{year} is not a Leap year")



temp = int(input("What is the temperature outside?: "))
if temp > -5 and temp < 5:
    print("It is very cold outside, wear a jacket")
elif temp >= 5 and temp < 18:
    print("It is cold Outside, plss wear a jacket")
else:
    print("It is not cold outside, you can wear normal clothes")