def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

text = input("Masukkan teks: ")
shift = int(input("Masukkan nilai pergeseran: "))

encrypted_text = caesar_cipher(text, shift)
print("Hasil enkripsi:", encrypted_text)
