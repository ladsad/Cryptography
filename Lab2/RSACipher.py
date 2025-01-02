def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def findE(phi):
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            return e
        e += 1
    return -1

def modInverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return -1

def encryptRSA(message, e, n):
    messageInt = 0
    for char in message:
        messageInt = messageInt*10 + ord(char)%65
    
    cipher = (messageInt ** e) % n
    return cipher

p = int(input("Enter a prime number p: "))
q = int(input("Enter another prime number q: "))
n = p * q
phi = (p - 1) * (q - 1)

e = findE(phi)
d = modInverse(e, phi)

print(f"Public key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")

message = input("Enter the message to encrypt: ")
cipher = encryptRSA(message, e, n)
print("Encrypted message:", cipher)