import random

play = True
random_number = random.randint(1,10)
while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if (guess == random_number):
        again = input("You've won! Want to play again? (y/n)")
        if (again.lower() == "y"):
            random_number = random.randint(1,10)
        else:
            break
    elif(guess > random_number):
        print("Too high, try again!")
    elif(int(guess) < random_number):
        print("Too low, try again!")
    else:
        print("Invalid input, try again!")


