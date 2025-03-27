# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot.
#  Foot is the singular, and feet is the plural.

inches_in_foot = 12

def inc_to_foot():
    feet = float(input("Enter number of feet : "))
    inches = feet * inches_in_foot
    print(f"The Answer was {inches} ")

inc_to_foot()