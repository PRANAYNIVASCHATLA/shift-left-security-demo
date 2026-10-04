import os

# Fixed Login Application

username = input("Enter username: ")
password = input("Enter password: ")

# Read password from an environment variable
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if username == "admin" and password == ADMIN_PASSWORD:
    print("Login Successful!")
else:
    print("Invalid Username or Password!")