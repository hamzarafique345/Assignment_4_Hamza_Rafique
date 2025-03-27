"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""
import random

# Number of sides on each die to roll
NUM_SIDES = 6

# Simulate rolling two dice and printing their total
def roll_dice():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2
    print(f"Die 1 = {die1}, Die 2 = {die2}, Total = {total}")

# Main function to demonstrate variable scope
def main():
    die1: int = 10  # Local variable in main
    print("die1 in main() starts as: " + str(die1))
    
    # Simulate three rolls
    roll_dice()
    roll_dice()
    roll_dice()
    
    print("die1 in main() ends as: " + str(die1))

# Run the program
if __name__ == "__main__":
    main()