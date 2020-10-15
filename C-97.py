import random

print("Guess the number")
rng = random.randint(1,9)
noOfChances = 0

print("guess the number between 1 and 9")
while noOfChances < 5 :
    num = int(input("Enter a number : "))
    if num == rng :
        print("you won")
        break
    elif num < rng :
        print("your guess was low guess a higher number")
    else :
        print("your guess was higher guess a lower number")
    noOfChances = noOfChances + 1

if not noOfChances < 5 :
    print("you lose. The number is : ", rng)