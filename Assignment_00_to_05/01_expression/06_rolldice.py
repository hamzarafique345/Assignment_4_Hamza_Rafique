import random
# Simulate rolling two dice, and prints results of each roll as well as the total. 



def dice_2():
    first_dice = random.randint(1,6)
    second_dice = random.randint(1,6)
    total = first_dice + second_dice
    print(f" Die 1: {first_dice},  Die 2: {second_dice},  Total: {total}")

dice_2()