# You want to be safe online and use different passwords for different websites. However, you are forgetful at times
# and want to make a program that can match which password belongs to which website without storing the actual password!


import hashlib

# Function jo password ka hash generate karega
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Stored logins ka dictionary
stored_logins = {
    "user1@example.com": hash_password("mypassword123"),
    "hamza@example.com": hash_password("securepassword"),
    "test@example.com": hash_password("hello123")
}

# Login function jo check karega password sahi hai ya nahi
def login(email, password_to_check):
    # Agar email database mein nahi hai, toh return False
    if email not in stored_logins:
        return False

    # User ka diya password hash mein convert karo
    hashed_input_password = hash_password(password_to_check)

    # Compare karo stored hash aur naye hash ko
    return hashed_input_password == stored_logins[email]


# ✅ Test Cases
print(login("hamza@example.com", "securepassword"))  # Output: True
print(login("hamza@example.com", "wrongpassword"))   # Output: False
print(login("unknown@example.com", "securepassword")) # Output: False
