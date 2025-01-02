def generateKeyMatrix(n, key):
    k = 0
    keyMatrix = [[ ord(key[j*n+i]) % 65 for i in range(n) ] for j in range(n)]
    return keyMatrix

def encrypt(cipherMatrix, keyMatrix, msgVctr, n):
    for i in range(n):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(n):
                cipherMatrix[i][j] += (keyMatrix[i][x] * msgVctr[x][j])
            
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(msg, key):
    n = len(msg)
    keyMatrix = generateKeyMatrix(n, key)
    msgVctr = [[ord(msg[i]) % 65] for i in range(n)]
    cipherMatrix = [[0] for _ in range(n)]

    encrypt(cipherMatrix, keyMatrix, msgVctr, n)
  
    CipherText = []
    for i in range(n):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    print("Ciphertext:", "".join(CipherText))

n = int(input("Length of message: "))
msg = input("Message: ") 
key = input("Key of length square of message: ")

HillCipher(msg, key)