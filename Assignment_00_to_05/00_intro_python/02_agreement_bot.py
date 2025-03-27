# Write a program which asks the user what their favorite animal is, and then always
# responds with "My favorite animal is also ___!" (the blank should be filled in with
# the user-inputted animal, of course).


def response():
    user_answer = input("Whats your favoite animal?")
    print(f"My favorite animal is also {user_answer}")

response()