# Definisi Permutasi dan Substitusi
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
P4 = [2, 4, 3, 1]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP = [4, 1, 2, 3, 2, 3, 4, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

# Fungsi Permutasi
def permute(bits, table):
    return [bits[i - 1] for i in table]

# Fungsi Left Shift
def left_shift(bits, n):
    return bits[n:] + bits[:n]

# Fungsi untuk Menghasilkan Kunci
def generate_keys(key):
    print("\n-- Proses Generasi Kunci --")
    key = permute(key, P10)
    print("P10:", ''.join(map(str, key)))
    
    left, right = key[:5], key[5:]
    print(''.join(map(str, left)), ''.join(map(str, right)))
    left, right = left_shift(left, 1), left_shift(right, 1)
    print("Left Shift-1:", ''.join(map(str, left)), ''.join(map(str, right)))
    k1 = permute(left + right, P8)
    print("K1:", ''.join(map(str, k1)))
    
    left, right = left_shift(left, 2), left_shift(right, 2)
    print("Left Shift-2:", ''.join(map(str, left)), ''.join(map(str, right)))
    k2 = permute(left + right, P8)
    print("K2:", ''.join(map(str, k2)))
    return k1, k2

# Fungsi Substitusi menggunakan S-Box
def substitute(bits, sbox):
    row = int(f"{bits[0]}{bits[3]}", 2)
    col = int(f"{bits[1]}{bits[2]}", 2)
    return [int(x) for x in f"{sbox[row][col]:02b}"]

# Fungsi F (bagian fungsi Feistel S-DES)
def fk(bits, key):
    left, right = bits[:4], bits[4:]
    print("\nKiri:", ''.join(map(str, left)), "| Kanan:", ''.join(map(str, right)))
    
    right_expanded = permute(right, EP)
    print("E/P:", ''.join(map(str, right_expanded)))
    
    xor_result = [right_expanded[i] ^ key[i] for i in range(8)]
    print("XOR dengan Kunci:", ''.join(map(str, xor_result)))
    
    left_sbox = substitute(xor_result[:4], S0)
    right_sbox = substitute(xor_result[4:], S1)
    print("S-Box S0:", ''.join(map(str, left_sbox)))
    print("S-Box S1:", ''.join(map(str, right_sbox)))
    
    sbox_result = permute(left_sbox + right_sbox, P4)
    print("P4:", ''.join(map(str, sbox_result)))
    
    fk_result = [left[i] ^ sbox_result[i] for i in range(4)] + right
    print("Hasil FK:", ''.join(map(str, fk_result)))
    return fk_result

# Fungsi untuk Proses Enkripsi dan Dekripsi
def sdes_encrypt_decrypt(plaintext, keys, encrypt=True):
    print("\n-- Proses", "Enkripsi" if encrypt else "Dekripsi", "--")
    bits = permute(plaintext, IP)
    print("IP:", ''.join(map(str, bits)))
    
    if encrypt:
        bits = fk(bits, keys[0])
        bits = bits[4:] + bits[:4]  # SWAP
        print("Swap:", ''.join(map(str, bits)))
        bits = fk(bits, keys[1])
    else:
        bits = fk(bits, keys[1])
        bits = bits[4:] + bits[:4]  # SWAP
        print("Swap:", ''.join(map(str, bits)))
        bits = fk(bits, keys[0])
        
    final_result = permute(bits, IP_INV)
    print("IP_INV:", ''.join(map(str, final_result)))
    return final_result

# Fungsi utama untuk menjalankan program
def main():
    # Input key dan plaintext
    key = input("Masukkan 10-bit key (contoh: 1010000010): ")
    key = [int(bit) for bit in key]
    
    plaintext = input("Masukkan 8-bit plaintext (contoh: 10101010): ")
    plaintext = [int(bit) for bit in plaintext]
    
    # Menghasilkan kunci K1 dan K2
    k1, k2 = generate_keys(key)
    
    # Enkripsi
    ciphertext = sdes_encrypt_decrypt(plaintext, (k1, k2), encrypt=True)
    print("Hasil enkripsi:", ''.join(map(str, ciphertext)))
    
    # Dekripsi
    decrypted_text = sdes_encrypt_decrypt(ciphertext, (k1, k2), encrypt=False)
    print("Hasil dekripsi:", ''.join(map(str, decrypted_text)))

# Menjalankan program
main()
