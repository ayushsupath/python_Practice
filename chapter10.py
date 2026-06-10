# a = [12,11,10,2,3,4]


# #order nature you can acces any elemet at any point of time
# # it has mutable nature you can change any values on your list
# # print(a[0])

# a[1] = 9

# print(a)


# l = [10,20,10,20,30,40,50]

#traversing on values

# for i in l:
#     print(i)

#traversing in index

# for i in range(0,len(l)):
#     print(f"{i} : {l[i]}")

# l = [10,20,30,40,45,50,60,70]
# l.append(60)
# l.insert(2, 30)
# a = l.pop(4)
# l.remove(45)

# print(l)
# print(a)

# list = [2,8,1,0,3,7,4]
# list.sort()
# print(list)


#Question1:

# l = [3,-1,-2,5,9,-4]

# pos = []
# neg = []

# for i in l:
#     if(i >= 0):
#         pos.append(i)
#     else:
#         neg.append(i)

# print(pos)
# print(neg)

#question2
# l = [10,20,30,40]
# sum = 0

# for i in l:
#     sum = sum + i


# print(sum)

# avg = sum / len(l)

# print(avg)

#qution3

# a = [20,99,88,34,55]

# largest = a[0]
# index = 0

# for i in range(0, len(a)):
#     if a[i]  > largest:
#         largest = a[i]
#         index = i
    
# print(f"your {largest} value at {index}")


#question4

# a = [20,99,88,34,55]

# largest = a[0]
# secondLar = a[0]

# for i in a:
#     if i > largest:
#         secondLar = largest
#         largest = i
#     elif i > secondLar:
#         secondLar = i

# print(secondLar)
# print(largest)

#question 5

a = [2, 7,1,3,8,4]

for i in range(0, len(a) - 1):
    if a[i] > a[i + 1]:
        print("your list is not sorted")
        break
else:
        print("your list is sorted")
