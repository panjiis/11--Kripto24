import math

# Fungsi untuk menghitung modulus invers menggunakan Algoritma Euclidean Extended
def mod_inverse(e, m):
    m0, x0, x1 = m, 0, 1
    while e > 1:
        q = e // m
        e, m = m, e % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Fungsi untuk mencari nilai gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fungsi untuk mengonversi teks ke representasi numerik
def text_to_number(text):
    return [ord(char) for char in text]

# Fungsi untuk mengonversi representasi numerik kembali ke teks
def number_to_text(numbers):
    return ''.join([chr(num) for num in numbers])

# Fungsi untuk mengenkripsi teks dengan RSA
def encrypt_rsa(plaintext, e, n):
    plaintext_numbers = text_to_number(plaintext)
    encrypted_numbers = [pow(num, e, n) for num in plaintext_numbers]
    i=1
    for num in plaintext_numbers:
        print(f"C{i} = {num}^{e} mod {n}")
        print(f"C{i} = {num**e} mod {n}")
        print(f"C{i} = ")
        print(f"")
    return encrypted_numbers

# Fungsi untuk mendekripsi teks dengan RSA
def decrypt_rsa(ciphertext, d, n):
    decrypted_numbers = [pow(num, d, n) for num in ciphertext]
    i=0
    for num in ciphertext:
        print(f"P{i} = {num}^{d} mod {n}")
        print(f"P{i} = {num**d} mod {n}")
        print(f"P{i} = {num**d%n}")
        print(f"")
        i=i+1
    return number_to_text(decrypted_numbers)

# Fungsi utama untuk menjalankan program
def main():
    print("Program RSA")
    p = int(input("Masukkan bilangan prima p: "))
    q = int(input("Masukkan bilangan prima q: "))

    # Menghitung n dan totient (m)
    n = p * q
    print(f"n = {p} * {q} = {n}")

    m = (p - 1) * (q - 1)
    print(f"m = ({p} - 1) * ({q} -1 )= {m}")
    # Memilih nilai e yang relatif prima dengan m
    e = 5
    print("misal e = 5")


    # Menghitung kunci privat d
    d = mod_inverse(e, m)

    print("\nKunci publik (e, n):", (e, n))
    print("Kunci privat (d, n):", (d, n))

    # Menu untuk memilih enkripsi atau dekripsi
    while True:
        print("\nPilih opsi:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == '1':
            plaintext = input("Masukkan plaintext: ")
            encrypted_message = encrypt_rsa(plaintext, e, n)
            print("Hasil enkripsi:", encrypted_message)

        elif choice == '2':
            ciphertext_input = input("Masukkan ciphertext (pisahkan dengan koma jika lebih dari satu angka): ")
            ciphertext = list(map(int, ciphertext_input.split(',')))
            decrypted_message = decrypt_rsa(ciphertext, d, n)
            print("Hasil dekripsi:", decrypted_message)

        elif choice == '3':
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
main()
