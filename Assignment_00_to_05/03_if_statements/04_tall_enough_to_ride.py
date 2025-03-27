#Write a program which asks the user how tall they are and prints whether or not they're taller
#than a pre-specified minimum height.

max_height = 50

def logic_ride():
    input_age = int(input("Enter your height to Check You can ride or not "))
    if input_age >= max_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

logic_ride()