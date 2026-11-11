# Cryptography Educational Scripts

This repository contains educational Python scripts to understand how some fundamental cryptographic primitives work.

## 📚 Content

The `crypto_lib.py` module implements various cryptographic operations organized in thematic classes:

### `NumberTheory`
Number theory operations:
- Primality test
- Prime factorization
- Euler's totient function φ
- Extended Euclidean algorithm
- Divisor calculation

### `Groups`
Modular arithmetic and group theory:
- Fast exponentiation (normal and modular)
- Multiplicative inverse calculation (3 methods: brute force, Euler's φ, extended Euclid)
- Search for generators in multiplicative groups

### `RSA`
RSA specific operations:
- Factorization via trial division

### `Montgomery`
Montgomery arithmetic for efficient modular calculations:
- Parameter generation
- Montgomery reduction
- Montgomery multiplication

## 🚀 Usage

```python
from crypto_lib import NumberTheory, Groups, RSA, Montgomery

# Primality test
print(NumberTheory.isprime(17))  # True

# Modular exponentiation
result = Groups.fast_exp_mod(3, 5, 7)  # 3^5 mod 7

# Euler's totient function φ
phi_10 = NumberTheory.phi(10)  # 4

# Multiplicative inverse
inv = Groups.mult_inv_euclid(3, 11)  # 4

# Group generator
gen = Groups.find_generator(11)
