from Crypto.Util.number import long_to_bytes
from sympy import prevprime

# Nilai m yang diketahui
m = 5129055


# Konversi bilangan bulat kembali ke byte
flag_bytes = long_to_bytes(m)

# Decode byte kembali ke string
flag = flag_bytes.decode()
print("Isi flag:", flag)
