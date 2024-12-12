def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used_chars = set()
    
    for char in key:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    ciphertext = ""
    
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        
        if a == b:
            b = 'X'
            i -= 1
        
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]
        
        i += 2
    
    return ciphertext

key = input("Enter key: ")
plaintext = input("Enter plaintext: ")
ciphertext = playfair_encrypt(plaintext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")