#! /usr/bin/python3
from crypto_lib import *
import math
import random
print("This script is a very simple demonstration of how the el_gamal asymmetric cryptography algorithm works")
m = int(input("insert the message: "))
bitlength = math.ceil(math.log2(m))
bitlength = bitlength+1
n = 10
while not NumberTheory.isprime(n):
    n = random.randint(2**bitlength, 2**(bitlength+1))
print("n= ", n)
g = Groups.find_generator(n)
print("g= ", g)
I = random.randint(2, n)
print("I=",I)
s = random.randint(3,n-1)
print("s=", s)
gs = Groups.fast_exp_mod(g, s, n)
print("gs=", gs)
gamma = Groups.fast_exp_mod(g, I, n)
delta = (m*Groups.fast_exp_mod(gs, I, n))%n
print("delta=",delta)
print("gamma=",gamma)
print("decrypting:")
print("decrypted:", (Groups.fast_exp_mod(gamma,NumberTheory.phi(n)-s,n)*delta)%n )
