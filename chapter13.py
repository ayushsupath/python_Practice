#d = {1:10, 2:20, 3:30, 4:40}

#method approach
# d.clear()

# q = d.fromkeys([1,2], 60)

# print(d.get(1))

# print(d.items())

# print(d.keys())

# print(d.pop(4))
# print(d.setdefault(3, 45))

# d.update({1:200})

# vanilla python

# d[5] = 50 #creating a new key value pairs

# d[1] = 100 # updating a key value that already exist


# for i in d:
#     print(d[i])
        

#question 1:

# d1 = {"a":10, "b":20, "c":30,"d":40}
# d2 = {"e":50, "f":60, "g":70,"h":80}


# for i in d2:
#     d1[i] = d2[i]
# # d1.update(d2)

# print(d1)

#Question 2

# d = {"a":10, "b":20, "c":30,"d":40}
# sum = 0

# for i in d:
#     sum = sum + d[i]
#     # print(d[i])

# print(sum)


#Question 3

l = ["a","b", "c","a","c","b","c"]
# count = 0

# for i in l:
#     if i == 'c':
#         count = count + 1

# print(count)


# d = {}

# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d) 

#question 4


d1 = {"a":10, "b":20, "c":30}
d2 = {"a":50, "c":60}

for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]

print(d1)