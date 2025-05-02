import numpy as np

def char_to_num(c):
    return ord(c) - ord('A')

def num_to_char(n):
    return chr(n + ord('A'))

def hill_encrypt(plaintext, key_matrix):
    plaintext_nums = [char_to_num(c) for c in plaintext]
    
    if len(plaintext_nums) % 2 != 0:
        plaintext_nums.append(char_to_num('X'))  

    ciphertext_nums = []
    for i in range(0, len(plaintext_nums), 2):

        vector = np.array([plaintext_nums[i], plaintext_nums[i + 1]])
        encrypted_vector = np.dot(key_matrix, vector) % 26 
        ciphertext_nums.extend(encrypted_vector)

    ciphertext = ''.join([num_to_char(num) for num in ciphertext_nums])
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):

    determinant = int(np.linalg.det(key_matrix)) 
    determinant_inv = pow(determinant, -1, 26)  
    adjugate_matrix = np.round(np.linalg.inv(key_matrix) * determinant).astype(int) % 26 
    inverse_key_matrix = (determinant_inv * adjugate_matrix) % 26  

    ciphertext_nums = [char_to_num(c) for c in ciphertext]

    plaintext_nums = []
    for i in range(0, len(ciphertext_nums), 2):
        vector = np.array([ciphertext_nums[i], ciphertext_nums[i + 1]])
        decrypted_vector = np.dot(inverse_key_matrix, vector) % 26  
        plaintext_nums.extend(decrypted_vector)

    plaintext = ''.join([num_to_char(num) for num in plaintext_nums])
    return plaintext

key_matrix = np.array([[3, 3], [2, 5]])

plaintext = input("Enter the plain text : ")

ciphertext = hill_encrypt(plaintext, key_matrix)
print("Ciphertext:", ciphertext)

decrypted_message = hill_decrypt(ciphertext, key_matrix)
print("Decrypted message:", decrypted_message)
