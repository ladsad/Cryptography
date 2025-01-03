def caesar_cipher(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
            
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char

    return result

text = input("Enter text: ")
shift = int(input("Enter shift: "))

encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted: {encrypted_text}")