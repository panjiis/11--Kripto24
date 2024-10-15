def generate_autokey(text, key):
    key = key + text[:len(text) - len(key)]
    return key

def encrypt_autokey(plaintext, key):
    key = generate_autokey(plaintext, key)
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

def decrypt_autokey(ciphertext, key):
    plaintext = []
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = (ord(ciphertext[i].lower()) - ord(key[i].lower()) + 26) % 26
            decrypted_char = chr(shift + ord('a'))
            print(f"(({ciphertext[i]}) {ord(ciphertext[i].lower())-97} - ({key[i]}){ord(key[i].lower())-97}) % 26 = {decrypted_char}")
            if ciphertext[i].isupper():
                decrypted_char = decrypted_char.upper()
            plaintext.append(decrypted_char)
            key += decrypted_char.lower() 
        else:
            plaintext.append(ciphertext[i])
    
    return "".join(plaintext)

def main():
    choice = input("Pilih 'e' untuk enkripsi atau 'd' untuk dekripsi: ").lower()
    
    if choice == 'e':
        plaintext = input("Masukkan plaintext: ")
        key = input("Masukkan key: ")
        encrypted_text = encrypt_autokey(plaintext, key)
        print(f"Hasil enkripsi: {encrypted_text}")
    
    elif choice == 'd':
        ciphertext = input("Masukkan ciphertext: ")
        key = input("Masukkan key: ")
        decrypted_text = decrypt_autokey(ciphertext, key)
        print(f"Hasil dekripsi: {decrypted_text}")
    
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
