# Fill out the function shorten(lst) which removes elements from the end of lst, which
# is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst
# is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main()
# function for you which gets a list and passes it into your function once you run the program.
# For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.




max_length = 3
def delete_item(list):
    while len(list) > max_length:
        x = list.pop() 
        print(f"Remove Element {x}")



def logic():
    list = []

    input_user = input("Enter Your Value to store in List") 
    while input_user:
        list.append(input_user)
        input_user = input("Enter Your Value to store in List") 
    print(f"Orignal List {list}")
    delete_item(list)
    print(list)

logic()