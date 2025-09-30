#! /usr/bin/python3
import time
import crypto_lib
import random
print("Questo script illustra in maniera molto semplificata come funziona la generazione di una coppia di chiavi pubblica/privata per l' algoritmo RSAi, NON è un algoritmo sicuro e non va assolutamente usato nella produzione di vere chiavi RSA")
print("I nummeri primi vanno scelti con altre tecniche e devono soddisfare certi requisiti pena la creazione di chiavi deboli (devono essere distanti tra di loro)")
bitq = int(input("dimensione in bit del primo q:"))
bitp = int(input("dimensione in bit del primo p:"))
d = None
start = time.perf_counter()
while d is None:
    p = random.randint( crypto_lib.Groups.fast_exp(2, bitp-1)-1, crypto_lib.Groups.fast_exp(2, bitp)-1)
    while crypto_lib.NumberTheory.isprime(p) is False:
        p -=1
    q = random.randint(crypto_lib.Groups.fast_exp(2, bitq-1)-1, crypto_lib.Groups.fast_exp(2, bitq)-1)
    while crypto_lib.NumberTheory.isprime(q) is False:
        q -=1
    print("trovati primi q e p in ",time.perf_counter()-start," secondi")
    n = p*q
    phin = (p-1)*(q-1)
    e = 3
    d = crypto_lib.Groups.mult_inv_euclid(e, phin)
    if d is None:
        e = 17
        d = crypto_lib.Groups.mult_inv_euclid(e, phin)
    if d is None:
        e = 65537
        d = crypto_lib.Groups.mult_inv_euclid(e, phin)


print("generazione chiavi completata in ", time.perf_counter()-start, " secondi")
print("p: ", p)
print("q: ", q)
print("phi: ", phin)
print("n: ", n)
print("e: ", e)
print("d: ", d)

m = int(input("inserire m (<n):"))
start = time.perf_counter()
c = crypto_lib.Groups.fast_exp_mod(m, e, n)
print("cifratura completata in ", time.perf_counter()-start, " secondi")
print("c =  ", c)
start = time.perf_counter()
print("decifrato: ", crypto_lib.Groups.fast_exp_mod(c, d, n))
print("decifratura completata in ", time.perf_counter()-start, " secondi")
