a = int(input("Enter your Number: "))

n = len(str(a))
temp = a        # a ko bachao comparison ke liye baad mein
total = 0

while temp > 0:
    digit = temp % 10      # tune ye samjha 
    total += digit ** n    # power lagao aur add karo
    temp = temp // 10      # number chota karo

if total == a:           # kisse compare karein?
    print("Armstrong")
else:
    print("Not Armstrong")

