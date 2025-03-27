# Ask the user for two numbers, one at a time, and then print the result of dividing
# the first number by the second and also the remainder of the division.


def div_and_rem():
    input_1 = int(input("Enter Your First Number to be divided : "))
    input_2 = int(input("Enter Your Second Number to be divide by : "))
    division = input_1 // input_2
    remainder = input_1 % input_2
    print(f"The result of the division is {division} with a remainder  of {remainder}")

div_and_rem()