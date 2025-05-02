def generate_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  
    key = key.replace('J', 'I') 
    matrix = key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  
    matrix = ''.join(sorted(set(matrix), key=lambda x: matrix.index(x)))  
    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def preprocess_message(message):
    message = message.replace(" ", "").upper()  

    new_message = []
    for i in range(0, len(message), 2):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            new_message.append(message[i] + 'X')
        else:
            new_message.append(message[i:i + 2])
    if len(new_message[-1]) == 1:
        new_message[-1] += 'X'  
    return ''.join(new_message)

def encrypt(message, matrix):
    encrypted_message = []
    message = preprocess_message(message)
    for i in range(0, len(message), 2):
        x1, y1 = find_position(matrix, message[i])
        x2, y2 = find_position(matrix, message[i + 1])
        if x1 == x2: 
            encrypted_message.append(matrix[x1][(y1 + 1) % 5])
            encrypted_message.append(matrix[x2][(y2 + 1) % 5])
        elif y1 == y2:  
            encrypted_message.append(matrix[(x1 + 1) % 5][y1])
            encrypted_message.append(matrix[(x2 + 1) % 5][y2])
        else: 
            encrypted_message.append(matrix[x1][y2])
            encrypted_message.append(matrix[x2][y1])
    return ''.join(encrypted_message)


key = input("Enter the key : ")
message = input("Enter the plain text : ")

matrix = generate_matrix(key)

ciphertext = encrypt(message, matrix)
print("Encrypted message:", ciphertext)
