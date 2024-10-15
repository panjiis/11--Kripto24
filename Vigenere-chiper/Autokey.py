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
    key_index = 0  # Gunakan index untuk menjaga posisi key

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Ambil karakter dari key atau tambahkan dari plaintext jika key habis
            if key_index < len(key):
                current_key_char = key[key_index]
            else:
                current_key_char = plaintext[key_index - len(key)+2]
            
            shift = (ord(ciphertext[i].lower()) - ord(current_key_char.lower()) + 26) % 26
            decrypted_char = chr(shift + ord('a'))
            print(f"(({ciphertext[i]}) {ord(ciphertext[i].lower()) - 97} - ({current_key_char.lower()}) {ord(current_key_char.lower()) - 97}) % 26 = {decrypted_char}")

            # Jika huruf asli adalah huruf besar, hasilnya juga dibuat huruf besar
            if ciphertext[i].isupper():
                decrypted_char = decrypted_char.upper()
            plaintext.append(decrypted_char)
            key_index += 1  # Tambahkan index setelah setiap karakter diproses
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
