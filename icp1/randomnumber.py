import random
num = random.randint(0, 10)
while True:
    print("enter the number to guess")
    guess = int(input())

    if guess == num:
        print("the number is correct")
        break
    elif guess < num:
        print("the number is low")
    elif guess > num:
        print("the number is high")