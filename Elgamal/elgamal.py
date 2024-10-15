from sympy import mod_inverse
import random

def elgamal_key_generation(p, g, x):
    y = pow(g, x, p) 
    public_key = (p, g, y)
    private_key = x
    return public_key, private_key

def elgamal_encrypt(plaintext, p, g, y, k):
    plaintext_integers = [ord(char) for char in plaintext]
    encrypted_pairs = []

    for m in plaintext_integers:
        a = pow(g, k, p)  
        print(f"a = {g}^{k} mod {p}")
        b = ((m-97) * pow(y, k, p)) % p 
        print(f"b = {m} - 97 * {y}^{k} mod {p}")
        encrypted_pairs.append((a, b))
        print(f"Encrypting: a = {a}, b = {b}")
    
    return encrypted_pairs

def elgamal_decrypt(encrypted_pairs, p, x):
    decrypted_chars = []

    for a, b in encrypted_pairs:
        s = pow(a, x, p) 
        print(f"s =  {a}^{x} mod {p}")
        s_inv = mod_inverse(s, p) 
        print(f"s_inv = {s}^(-1) mod {p}")
        m = (b * s_inv) % p + 97 
        print(f"m = {b} * {s_inv} mod {p} + 97")
        decrypted_chars.append(chr(m))
        print(f"Decrypting: a = {a}, b = {b}, s = {s}, s_inv = {s_inv}, m = {m}")
    
    return ''.join(decrypted_chars)

def main():
    choice = input("Pilih 'e' untuk enkripsi atau 'd' untuk dekripsi: ").lower()
    p = int(input("Masukkan nilai p (bilangan prima): "))
    g = int(input("Masukkan nilai g (generator): "))
    x = int(input("Masukkan nilai x (private key): "))
    k = int(input("Masukkan nilai k (random key, harus coprime dengan p-1): "))

    if choice == 'e':
        plaintext = input("Masukkan plaintext: ")
        public_key, _ = elgamal_key_generation(p, g, x)
        encrypted_pairs = elgamal_encrypt(plaintext, *public_key, k)
        print(f"Hasil enkripsi: {encrypted_pairs}")
    
    elif choice == 'd':
        encrypted_pairs = input("Masukkan pasangan terenkripsi (a, b) dalam format [(a1, b1), (a2, b2), ...]: ")
        encrypted_pairs = eval(encrypted_pairs)
        decrypted_text = elgamal_decrypt(encrypted_pairs, p, x)
        print(f"Hasil dekripsi: {decrypted_text}")
    
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    main()
