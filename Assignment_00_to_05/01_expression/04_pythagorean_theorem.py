# Write a program that asks the user for the lengths of the two perpendicular 
# sides of a right triangle and outputs the length of the third side (the hypotenuse) 
# using the Pythagorean theorem!


import math

ab = float(input("Enter the length of AB: "))
ac = float(input("Enter the length of AC: "))

# Calculate the hypotenuse using the Pythagorean theorem
bc = math.sqrt(ab**2 + ac**2)

print(f"The length of BC (the hypotenuse) is: {bc}")
