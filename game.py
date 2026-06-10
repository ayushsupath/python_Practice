import random

com = random.randint(1, 100)

score = 0

while True:
    hum = int(input("Enter a number between 1 and 100: "))

    if hum == com:
        print("Congratulations, you win!")
        break
    elif hum < com:
        print("Too low, try again")
    else:
        print("Too high, try again")
    score += 1

print(f"Your score is: {score}")