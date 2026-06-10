a = int(input("Enter your number: "))

if a <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, a):      # 2 se shuru 
        if a % i == 0:
            is_prime = False   # flag False karo
            break              # loop todo
    
    if is_prime:               # loop ke BAAD check karo
        print("Prime")
    else:
        print("Not Prime")