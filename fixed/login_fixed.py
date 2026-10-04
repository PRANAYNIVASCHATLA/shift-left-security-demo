
import os
import re
import hmac
import getpass

# Fixed Login Application (v2)

def is_valid_username(name):
    # 3-20 characters: letters, numbers, underscore only
    return re.fullmatch(r"[A-Za-z0-9_]{3,20}", name) is not None

# 1. Read the secret from the environment
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

if not ADMIN_PASSWORD:
    print("Error: ADMIN_PASSWORD environment variable is not set.")
    raise SystemExit(1)

# 2. Collect input
username = input("Enter username: ").strip()
password = getpass.getpass("Enter password: ").strip()

# 3. Basic input validation
if not is_valid_username(username):
    print("Invalid username format.")
    raise SystemExit(1)

if not 1 <= len(password) <= 64:
    print("Invalid password length.")
    raise SystemExit(1)

# 4. Compare safely
password_ok = hmac.compare_digest(
    password.encode(),
    ADMIN_PASSWORD.encode()
)

if username == "admin" and password_ok:
    print("Login Successful!")
else:
    print("Invalid Username or Password!")
