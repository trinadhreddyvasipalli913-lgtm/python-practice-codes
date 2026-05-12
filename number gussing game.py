import random
secreat_number=random.randint(1,100)
attempts=0
print("number gussing game".center(80))
print("guess a number between 1 and 100:")
while True:
    guess=int(input("enter your guss:"))
    attempts+=1
    if guess < secreat_number:
        print("too low! try again:")
    elif guess > secreat_number:
        print("too high!! try again:")
    else:
        print("correct! you gussed the number.")
        print("total attempts:",attempts)
        break
