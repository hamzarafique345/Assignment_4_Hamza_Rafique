# user to enter the lengths of each side of a triangle and then calculate
# and print the perimeter of the triangle (the sum of all of the side lengths).

def tri():
    user_input_len_side_1 = int(input("What is the length of side 1 ?"))
    user_input_len_side_2 = int(input("What is the length of side 2 ?"))
    user_input_len_side_3 = int(input("What is the length of side 3 ?"))
    print(f"The perameter of all triangle is {user_input_len_side_1 + user_input_len_side_2 + user_input_len_side_3}")

tri()