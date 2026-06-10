# range(1, 50, 1)
# range(0, 20, 2)

# for i in range(0, 11, 2):
#     print(i)

# n = int(input("Enter a number: "))
# for n in range(n, (n*10)+1, n):
#     print(n)


# a = "Ayush Supath"
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(f"{i}:{a[i]}")

# for i in range(1, 11,1):
#     if i == 45:
#         break
#     print(i)
# else:
#     print("No break was countered")

#Question 1:
# n = int(input("Enter a number: "))
# for i in range(n):
#     print("HEllo Ayush")

#Question 2:

# n = int(input("Enter a number: "))
# for i in range(1, n + 1, 1):
#     print(i)

#Question 3:

# n = int(input("Enter your number brother: "))
# for  i in range(n, 0 , -1):
#     print(i)

#question 4:

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{n} X {i} = {i * n}")

# Question 5:

# a = 0
# n = int(input("Sum of your natural numbers: "))
# for i in range(1 ,n+1):
#     a = a + i;
# print(f"The sum of first {n} natural numbers is {a}")



#question 6:

# fact = 1
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     fact = fact * i
#     print(fact)


#question 7:

# n = int(input("Enter your number: "))

# OddSum = 0
# EvenSum = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         EvenSum = EvenSum + i
#     else:
#         OddSum = OddSum + i

# print(f"Sum of even numbers: {EvenSum}")
# print(f"Sum of odd numbers: {OddSum}")

# question 8:

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(f"{i} is a factor of {n}")
#     else:
#         print(f"{i} is not a factor of {n}")


#question 9:

# sum = 0
# n = int(input("Enter a number: "))
# for i in range(1, n):
#     if n % i == 0:
#         sum = sum + i

# if sum == n:
#     print(f"{n} is a perfect number")
# else:
#     print(f"{n} is not a perfect number")


#Question 10:

# n = int(input("Enter a number: "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1

# if count == 2:
#     print("prime number")
# else:
#     print("not a prime number")


#question 11:

# a = str(input("Enter a string: "))

# for i in  range(len(a)- 1, -1 , -1):
#     print(a[i], end = " ")

# Question 12:

# a = str(input("Enter a string: "))

# for i in range(len(a)- 1, -1, -1):
#     print(a[i], end = "")

# if end == a:
#     print("yes this is palindrome")
# else:    print("no this is not palindrome")


# Question 13:

a = str(input("Enter a string: "))

char = 0
spchar = 0
dig = 0

for i in a:
    if i.isalpha():
        char = char + 1
    elif i.isdigit():
        dig = dig + 1
    else:
        spchar = spchar + 1
        
print(f"characters: {char}")
print(f"spaces: {spchar}")
print(f"digits: {dig}")