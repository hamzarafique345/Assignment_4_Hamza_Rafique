
# Write a function that takes a list of numbers and returns the sum of those numbers.


def sum(number_list):
    num = 0
    for i in number_list:
        num += i
    return num

x = [1,2,3,4,5,6]
result = sum(x)
print(result)