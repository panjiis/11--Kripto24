import numpy as np

def mod_inv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inv(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inv(det, mod)
    
    if det_inv is None:
        raise ValueError("Matrix tidak memiliki invers modular.")
    
    matrix_adj = np.array([[matrix[1][1], -matrix[0][1]], 
                           [-matrix[1][0], matrix[0][0]]])
    matrix_inv = (det_inv * matrix_adj) % mod
    return matrix_inv

def hill_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    if len(plaintext) % 2 != 0:
        plaintext += "X"
    
    plaintext_nums = [ord(c) - 65 for c in plaintext]
    encrypted_nums = []
    
    for i in range(0, len(plaintext_nums), 2):
        vector = np.array(plaintext_nums[i:i+2])
        encrypted_vector = np.dot(key_matrix, vector) % 26
        encrypted_nums.extend(encrypted_vector)
    
    ciphertext = ''.join(chr(num + 65) for num in encrypted_nums)
    return ciphertext

def hill_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.replace(" ", "").upper()
    if len(ciphertext) % 2 != 0:
        ciphertext += "X"
    
    ciphertext_nums = [ord(c) - 65 for c in ciphertext]
    decrypted_nums = []
    
    key_matrix_inv = matrix_mod_inv(key_matrix, 26)
    
    for i in range(0, len(ciphertext_nums), 2):
        vector = np.array(ciphertext_nums[i:i+2])
        decrypted_vector = np.dot(key_matrix_inv, vector) % 26
        decrypted_nums.extend(decrypted_vector)
    
    plaintext = ''.join(chr(int(num) + 65) for num in decrypted_nums)
    return plaintext

def find_key(plaintext, ciphertext):
    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = ciphertext.replace(" ", "").upper()

    if len(plaintext) < 4 or len(ciphertext) < 4:
        raise ValueError("Plaintext dan ciphertext harus memiliki setidaknya 4 karakter.")

    plaintext_nums = [ord(c) - 65 for c in plaintext[:4]]
    ciphertext_nums = [ord(c) - 65 for c in ciphertext[:4]]

    plaintext_matrix = np.array([plaintext_nums[0], plaintext_nums[2], plaintext_nums[1], plaintext_nums[3]]).reshape(2, 2)
    ciphertext_matrix = np.array([ciphertext_nums[0], ciphertext_nums[2], ciphertext_nums[1], ciphertext_nums[3]]).reshape(2, 2)

    plaintext_matrix_inv = matrix_mod_inv(plaintext_matrix, 26)

    key_matrix = np.dot(ciphertext_matrix, plaintext_matrix_inv) % 26
    return key_matrix

def main():
    print("Pilih operasi yang ingin dilakukan:")
    print("1. Enkripsi (Hill Cipher)")
    print("2. Dekripsi (Hill Cipher)")
    print("3. Mencari Kunci (Hill Cipher)")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == "1":
        plaintext = input("Masukkan plaintext: ")
        key_matrix_input = input("Masukkan elemen matriks kunci 2x2 (4 elemen, dipisahkan dengan spasi): ")
        key_matrix = np.array(list(map(int, key_matrix_input.split()))).reshape(2, 2)
        ciphertext = hill_encrypt(plaintext, key_matrix)
        print("Hasil enkripsi (ciphertext):", ciphertext)
    
    elif choice == "2":
        ciphertext = input("Masukkan ciphertext: ")
        key_matrix_input = input("Masukkan elemen matriks kunci 2x2 (4 elemen, dipisahkan dengan spasi): ")
        key_matrix = np.array(list(map(int, key_matrix_input.split()))).reshape(2, 2)
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
