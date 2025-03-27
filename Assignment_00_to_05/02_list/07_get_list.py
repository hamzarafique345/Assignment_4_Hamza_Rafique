# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
# Here's a sample run (user input is in blue):
# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def logic():
    list = []
    input_user_num = input('Enter The Number which you want to add in List')

    while input_user_num:
        list.append(input_user_num)
        input_user_num = input('Enter The Number which you want to add in List')
    print(list)
 

logic()