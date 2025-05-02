def create_matrix(key):
    key = ''.join(sorted(set(key), key=key.index))
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key:
        if char not in matrix and char != 'J':
            matrix.append(char)
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    return matrix
def format_message(message):
    message = message.upper().replace(" ", "")  
    formatted_message = []
    i = 0
    while i < len(message):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            formatted_message.append(message[i] + 'X')  
            i += 1
        else:
            formatted_message.append(message[i:i + 2])
            i += 2
    if len(formatted_message[-1]) == 1:
        formatted_message[-1] += 'X'  
    return formatted_message
def get_position(letter, matrix):
    index = matrix.index(letter)
    return divmod(index, 5)  
def encrypt(message, key):
    matrix = create_matrix(key)
    formatted_message = format_message(message)
    ciphertext = []
    for pair in formatted_message:
        row1, col1 = get_position(pair[0], matrix)
        row2, col2 = get_position(pair[1], matrix)
        if row1 == row2:
            ciphertext.append(matrix[row1 * 5 + (col1 + 1) % 5])
            ciphertext.append(matrix[row2 * 5 + (col2 + 1) % 5])
        elif col1 == col2:
            ciphertext.append(matrix[((row1 + 1) % 5) * 5 + col1])
            ciphertext.append(matrix[((row2 + 1) % 5) * 5 + col2])
        else:
            ciphertext.append(matrix[row1 * 5 + col2])
            ciphertext.append(matrix[row2 * 5 + col1])
    return ''.join(ciphertext)
def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    formatted_message = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = []
    for pair in formatted_message:
        row1, col1 = get_position(pair[0], matrix)
        row2, col2 = get_position(pair[1], matrix)
        if row1 == row2:
            plaintext.append(matrix[row1 * 5 + (col1 - 1) % 5])
            plaintext.append(matrix[row2 * 5 + (col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(matrix[((row1 - 1) % 5) * 5 + col1])
            plaintext.append(matrix[((row2 - 1) % 5) * 5 + col2])
        else:
            plaintext.append(matrix[row1 * 5 + col2])
            plaintext.append(matrix[row2 * 5 + col1])
    return ''.join(plaintext).replace('X', '')  
message = input("Enter the message : ").strip()
key = input("Enter the key: ").strip()
ciphertext = encrypt(message, key)
print("Encrypted Message :", ciphertext)
decrypted_message = decrypt(ciphertext, key)
print("Decrypted Message:", decrypted_message)

