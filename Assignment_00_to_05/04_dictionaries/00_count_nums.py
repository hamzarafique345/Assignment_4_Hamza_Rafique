# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.



# Program to count how many times each number appears in a list using a dictionary

# Initialize an empty dictionary to store number counts


count_dict = {}

while True:
    user_input = input("Enter a number (or type 'done' to finish): ")
    
    if user_input.lower() == "done":
        break
    try:
        number = int(user_input)
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    except ValueError:
        print("❌ Please enter a valid number!")

for num, count in count_dict.items():
    print(f"{num} appears {count} time{'s' if count > 1 else ''}.")
