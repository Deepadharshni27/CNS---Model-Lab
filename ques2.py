import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_prime_number(start, end):
    primes = [p for p in range(start, end) if all(p % i != 0 for i in range(2, int(p**0.5) + 1))]
    return random.choice(primes)

p = int(input("Enter the value of P : "))
q = int(input("Enter the value of q : "))
m = int(input("Enter the value of m : "))

n = p * q
phi_n = (p - 1) * (q - 1)

e = int(input("Enter the value of e : "))

d = pow(e, -1, phi_n)

public_key = (e, n)
private_key = (d, n)

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

message = input("Enter the plain text : ")
print("Original Message:", message)

encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
