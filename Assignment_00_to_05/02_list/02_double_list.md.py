
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def double_list():
    x = [1,2,3,4]
    y =[]
    for i in x:
        x = i * 2
        y.append(x)
    print(y)

double_list()

    