# Vulnerable Login Application

username = input("Enter username: ")
password = input("Enter password: ")

# Security Vulnerability: Hardcoded Password
ADMIN_PASSWORD = "admin123"

if username == "admin" and password == ADMIN_PASSWORD:
    print("Login Successful!")
else:
    print("Invalid Username or Password!")