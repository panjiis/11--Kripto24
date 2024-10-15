import numpy as np

# Fungsi untuk menghitung invers modular dari sebuah bilangan dalam modulus m.
def mod_inv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Fungsi untuk menghitung invers modular dari matriks 3x3 dalam modulus tertentu.
def matrix_mod_inv(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inv(det, mod)
    
    if det_inv is None:
        raise ValueError("Matrix tidak memiliki invers modular.")
    
    # Matriks kofaktor (adjugate) dari matriks 3x3
    matrix_adj = np.round(det * np.linalg.inv(matrix)).astype(int)
    
    matrix_inv = (det_inv * matrix_adj) % mod
    return matrix_inv

# Fungsi untuk enkripsi teks menggunakan Hill Cipher dengan matriks 3x3
def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    if len(plaintext) % 3 != 0:
        plaintext += "X" * (3 - len(plaintext) % 3)  # Pad agar bisa dibagi menjadi 3 huruf
    
    plaintext_nums = [ord(c) - 65 for c in plaintext]
    encrypted_nums = []
    
    for i in range(0, len(plaintext_nums), 3):
        vector = np.array(plaintext_nums[i:i+3])
        encrypted_vector = np.dot(key_matrix, vector) % 26
        encrypted_nums.extend(encrypted_vector)
    
    ciphertext = ''.join(chr(num + 65) for num in encrypted_nums)
    return ciphertext

# Fungsi untuk dekripsi teks menggunakan Hill Cipher dengan matriks 3x3
def hill_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.replace(" ", "").upper()
    if len(ciphertext) % 3 != 0:
        ciphertext += "X" * (3 - len(ciphertext) % 3)
    
    ciphertext_nums = [ord(c) - 65 for c in ciphertext]
    decrypted_nums = []
    
    key_matrix_inv = matrix_mod_inv(key_matrix, 26)
    
    for i in range(0, len(ciphertext_nums), 3):
        vector = np.array(ciphertext_nums[i:i+3])
        decrypted_vector = np.dot(key_matrix_inv, vector) % 26
        decrypted_nums.extend(decrypted_vector)
    
    plaintext = ''.join(chr(int(num) + 65) for num in decrypted_nums)
    return plaintext

# Fungsi untuk mencari matriks kunci Hill Cipher dari plaintext dan ciphertext
def find_key(plaintext, ciphertext):
    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = ciphertext.replace(" ", "").upper()

    if len(plaintext) < 9 or len(ciphertext) < 9:
        raise ValueError("Plaintext dan ciphertext harus memiliki setidaknya 9 karakter.")
    
    plaintext_nums = [ord(c) - 65 for c in plaintext[:9]]
    ciphertext_nums = [ord(c) - 65 for c in ciphertext[:9]]
    
    plaintext_matrix = np.array(plaintext_nums).reshape(3, 3)
    ciphertext_matrix = np.array(ciphertext_nums).reshape(3, 3)

    # Cek determinan sebelum mencari invers
    det_plaintext = int(np.round(np.linalg.det(plaintext_matrix)))
    print(f"Determinan matriks plaintext: {det_plaintext}")

    # Pastikan determinan relatif prima dengan 26
    if mod_inv(det_plaintext, 26) is None:
        raise ValueError(f"Determinan matriks plaintext ({det_plaintext}) tidak memiliki invers modular dalam mod 26.")
    
    plaintext_matrix_inv = matrix_mod_inv(plaintext_matrix, 26)
    
    key_matrix = np.dot(ciphertext_matrix, plaintext_matrix_inv) % 26
    return key_matrix


# Menu utama untuk memilih operasi
def main():
    print("Pilih operasi yang ingin dilakukan:")
    print("1. Enkripsi (Hill Cipher)")
    print("2. Dekripsi (Hill Cipher)")
    print("3. Mencari Kunci (Hill Cipher)")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "1":
        plaintext = input("Masukkan plaintext: ")
        key_matrix_input = input("Masukkan elemen matriks kunci 3x3 (9 elemen, dipisahkan dengan spasi): ")
        key_matrix = np.array(list(map(int, key_matrix_input.split()))).reshape(3, 3)
        ciphertext = hill_encrypt(plaintext, key_matrix)
        print("Hasil enkripsi (ciphertext):", ciphertext)
    
    elif choice == "2":
        ciphertext = input("Masukkan ciphertext: ")
        key_matrix_input = input("Masukkan elemen matriks kunci 3x3 (9 elemen, dipisahkan dengan spasi): ")
        key_matrix = np.array(list(map(int, key_matrix_input.split()))).reshape(3, 3)
        plaintext = hill_decrypt(ciphertext, key_matrix)
        print("Hasil dekripsi (plaintext):", plaintext)

    elif choice == "3":
        plaintext = input("Masukkan plaintext: ")
        ciphertext = input("Masukkan ciphertext: ")
        key_matrix = find_key(plaintext, ciphertext)
        print("Matriks kunci adalah:")
        print(key_matrix)
    
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
