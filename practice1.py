a = int(input("Enter the Number that you want to reverse: "))

rev = 0
sign = 1

if a < 0:
    sign = -1
    a = abs(a)

while a > 0 :
    rev = rev * 10 + a % 10
    a = a // 10

print(rev * sign)
    