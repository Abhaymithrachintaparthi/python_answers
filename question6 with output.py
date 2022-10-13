#program for guessing random number
import random

print("welcome to random number guessing name!")
n = random.randint(1,10)
while True:
    user_input = int(input("please enter any number between 1 to 10:\n"))
    if user_input>n:
        print("your guess is too high")
    elif user_input<n:
        print("your guess is too low")
    elif user_input==n:
        print("you won the game")
        break
#output:
# welcome to random number guessing name!
# please enter any number between 1 to 10:
# 8
# your guess is too high
# please enter any number between 1 to 10:
# 6
# your guess is too low
# please enter any number between 1 to 10:
# 7
# you won the game
#
# Process finished with exit code 0
