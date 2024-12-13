def pow_mod(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) 
        exp = exp // 2
        base = (base * base) 
    return result

# Constants
p = 97  # Modulus
a = 36  # Exponent for 44
b = 58  # Exponent for 50

# Calculate powers
result_a = pow_mod(44, a, p)
result_b = pow_mod(50, b, p)

print(result_a, result_b)
