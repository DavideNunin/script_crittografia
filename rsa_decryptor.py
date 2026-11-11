#! /usr/bin/python3
from crypto_lib import *
import time

def inverse(e,n):
    for i in range(1,n):
        if((e*i)%n)==1:
            return i

print("This script explains how to derive the private key from an RSA public key. Obviously, the computationally difficult part is the factorization, and the algorithm used by this script is extremely simple and suboptimal")
n=int(input("insert n: "))
e=int(input("insert e: "))
c=int(input("insert encrypted message:"))
start=time.perf_counter()
p=RSA.factorize_by_trial(n)
print("factorization completed in ",time.perf_counter()-start,"seconds")
print("found p:",p)
q=int(n/p)
print("found q:",q)
phin=(q-1)*(p-1)
print("found phi:",phin)
start=time.perf_counter()
d=Groups.mult_inv_euclid(e,phin)
print("found private exponent: ", d," in ",time.perf_counter()-start," seconds")
print("decrypted:",Groups.fast_exp_mod(c, d, n))
