# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints
# the first element in the list. The list is guaranteed to be non-empty. We've written some code for
# you which prompts the user to input the list one element at a time.

def first_index(list):
    print(list[0])

def logic():
    list = []
    user_input = input("Enter Your Element to add in list and if you want stop enter empty input")
    while user_input != "":
        list.append(user_input)
        user_input = input("Enter Your Element to add in list and if you want stop enter empty input")
    return list
        

x = logic()
first_index(x)