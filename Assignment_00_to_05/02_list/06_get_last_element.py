# ill out the function get_last_element(lst) which takes in a list lst as a parameter
# and prints the last element in the list. The list is guaranteed to be non-empty, but
# there are no guarantees on its length.


def first_index(list):
    print(list[-1])

def logic():
    list = []
    user_input = input("Enter Your Element to add in list and if you want stop enter empty input")
    while user_input != "":
        list.append(user_input)
        user_input = input("Enter Your Element to add in list and if you want stop enter empty input")
    return list
        

x = logic()
first_index(x)