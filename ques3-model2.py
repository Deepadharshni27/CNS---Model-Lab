import hashlib

password = input("Enter your password: ")

hashed_password = hashlib.sha1(password.encode()).hexdigest()

print("SHA-1 Hash:", hashed_password)
