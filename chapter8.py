# a = 1
# while a <= 20:
#     print(a)
#     a += 1


#question 1:

# a = int(input("Enter a number: "))
# while a > 0:
#     print(a % 10)
#     a = a // 10


#question 2:

# a = int(input("Enter a number: "))

# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print("This is your Rev: " + str(rev))


#question 3:

a= int(input("Enter a number: "))
copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

if rev == copy:
    print("yes palindrome")
else:    print("no not palindrome")
