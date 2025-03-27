# Write a program which prompts the user for a temperature in Fahrenheit
# (this can be a number with decimal places!) and outputs the temperature
#  converted to Celsius.

def convert_fre_to_cel():
    fahrenheit_no = float(input("Enter Freanheit Unit to Convert In Celsius"))
    convert_cel = (fahrenheit_no - 32) * 5.9 / 9.0
    print(f"Temperature {fahrenheit_no}F ={round(convert_cel, 2)}C  ")

convert_fre_to_cel()