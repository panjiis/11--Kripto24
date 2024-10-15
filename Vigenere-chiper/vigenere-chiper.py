def generate_vigenere_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(plaintext, key):
    key = generate_vigenere_key(plaintext, key)
    ciphertext = []
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = (ord(plaintext[i].lower()) + ord(key[i].lower()) - 2 * ord('a')) % 26

            encrypted_char = chr(shift + ord('a'))
            print(f"(({plaintext[i]}) {ord(plaintext[i].lower())-97} + ({key[i]}){ord(key[i].lower())-97}) % 26 = {encrypted_char}")
            if plaintext[i].isupper():
                encrypted_char = encrypted_char.upper()
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(plaintext[i])
    
    return "".join(ciphertext)

def decrypt_vigenere(ciphertext, key):
    key = generate_vigenere_key(ciphertext, key)
    plaintext = []
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = (ord(ciphertext[i].lower()) - ord(key[i].lower()) + 26) % 26
            decrypted_char = chr(shift + ord('a'))
            print(f"(({ciphertext[i]}) {ord(ciphertext[i].lower())-97} - ({key[i]}){ord(key[i].lower())-97}) % 26 = {decrypted_char}")
            if ciphertext[i].isupper():
                decrypted_char = decrypted_char.upper()
            plaintext.append(decrypted_char)
        else:
            plaintext.append(ciphertext[i])
    
    return "".join(plaintext)

def main():
    choice = input("Pilih 'e' untuk enkripsi atau 'd' untuk dekripsi: ").lower()
    
    if choice == 'e':
        plaintext = input("Masukkan plaintext: ")
        key = input("Masukkan key: ")
        encrypted_text = encrypt_vigenere(plaintext, key)
        print(f"Hasil enkripsi: {encrypted_text}")
    
    elif choice == 'd':
        ciphertext = input("Masukkan ciphertext: ")
        key = input("Masukkan key: ")
        decrypted_text = decrypt_vigenere(ciphertext, key)
        print(f"Hasil dekripsi: {decrypted_text}")
    
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
