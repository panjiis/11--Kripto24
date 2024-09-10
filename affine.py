# Fungsi untuk menghitung Modular Inverse dari a
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fungsi enkripsi Affine Cipher
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        
        if char.isalpha():
            if char.isupper():
                print(f"({a} * {ord(char)-65} ({char}) + {b}) % 26 = {((a * (ord(char) - 65) + b) % 26)} ({chr(((a * (ord(char) - 65) + b) % 26) + 65)})")
                result += chr(((a * (ord(char) - 65) + b) % 26) + 65)
            else:
                print(f"({a} * {ord(char)-97}({char}) + {b}) % 26 = {((a * (ord(char) - 97) + b) % 26)} ({chr(((a * (ord(char) - 97) + b) % 26) + 97)})")
                result += chr(((a * (ord(char) - 97) + b) % 26) + 97)
        else:
            result += char
            print("")
    return result

# Fungsi dekripsi Affine Cipher
def affine_decrypt(text, a, b):
    result = ""
    a_inv = mod_inverse(a, 26) 
    if a_inv is None:
        return "Invers modulus dari a tidak ditemukan, dekripsi tidak dapat dilakukan."
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                print(f"({a_inv} * ({ord(char)-65} ({char}) - {b})) % 26 = {((a_inv * (ord(char) - 65 - b)) % 26)} ({chr(((a_inv * (ord(char) - 65 - b)) % 26) + 65)})")
                result += chr(((a_inv * (ord(char) - 65 - b)) % 26) + 65)
            else:
                print(f"({a_inv} * ({ord(char)-65} ({char}) - {b})) % 26 = {((a_inv * (ord(char) - 97 - b)) % 26)} ({chr(((a_inv * (ord(char) - 97 - b)) % 26) + 97)})")
                result += chr(((a_inv * (ord(char) - 97 - b)) % 26) + 97)
        else:
            # Jika bukan huruf, biarkan tetap sama
            result += char
            print("")
    return result

# Input dari pengguna
text = input("Masukkan teks: ")
choice = input("Pilih 'e' untuk enkripsi atau 'd' untuk dekripsi: ")

# Tetapkan nilai a dan b
a = 9
b = 11

# Proses enkripsi atau dekripsi
if choice == 'e':
    encrypted_text = affine_encrypt(text, a, b)
    print("Hasil enkripsi:", encrypted_text)
elif choice == 'd':
    decrypted_text = affine_decrypt(text, a, b)
    print("Hasil dekripsi:", decrypted_text)
else:
    print("Pilihan tidak valid.")
