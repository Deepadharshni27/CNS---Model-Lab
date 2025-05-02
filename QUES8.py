def vigenere_encrypt(plaintext, keyword):
    ciphertext = ""
    keyword = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]
    
    for p, k in zip(plaintext, keyword):
        if p.isalpha(): 
            shift = ord(k.upper()) - ord('A')
            encrypted_char = chr((ord(p.upper()) - ord('A') + shift) % 26 + ord('A'))
            if p.islower():
                encrypted_char = encrypted_char.lower()
            ciphertext += encrypted_char
        else:
            ciphertext += p
    return ciphertext

def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""
    keyword = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]
    
    for c, k in zip(ciphertext, keyword):
        if c.isalpha():  
            shift = ord(k.upper()) - ord('A')
            decrypted_char = chr((ord(c.upper()) - ord('A') - shift) % 26 + ord('A'))
            if c.islower():
                decrypted_char = decrypted_char.lower()
            plaintext += decrypted_char
        else:
            plaintext += c 
    return plaintext


plaintext = input("Enter the plaintest : ")
keyword = input ("Enter the key : ")

encrypted_message = vigenere_encrypt(plaintext, keyword)
print("Encrypted message:", encrypted_message)

decrypted_message = vigenere_decrypt(encrypted_message, keyword)
print("Decrypted message:", decrypted_message)
