def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha(): 
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            plaintext += decrypted_char
        else:
            plaintext += char  
    return plaintext

ciphertext = "WKLQNLQJ LV WKH NHB WR VXFFHVV"

for shift in range(26):
    decrypted_message = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_message}")
