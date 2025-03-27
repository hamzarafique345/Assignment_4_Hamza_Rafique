# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48
import random


def logic():
    generate_rad_num = random.randint(1,10)

    while True:
        input_from_user = int(input("Enter Your Guess number"))

        if generate_rad_num == input_from_user:
            print("Oh my God You Are Correct")
        elif generate_rad_num > input_from_user:
            print("Broo Too Low")
        else:
            print("Too High")

logic()