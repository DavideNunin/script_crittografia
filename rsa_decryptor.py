#! /usr/bin/python3
from crypto_lib import *
import time

def inverse(e,n):
    for i in range(1,n):
        if((e*i)%n)==1:
            return i

print("Questo script spiega come trovare ricavare la chiave privata da una chiave pubblica RSA, ovviamente la parte computazionalmente difficile è la fattorizzazione e l' algoritmo usato da questo script è estremamente semplice e subottimale")
n=int(input("inserire n: "))
e=int(input("inserire e: "))
c=int(input("inserire messaggio cifrato:"))
start=time.perf_counter()
p=RSA.factorize_by_trial(n)
print("fattorizzazione completata in ",time.perf_counter()-start,"secondi")
print("trovato p:",p)
q=int(n/p)
print("trovato q:",q)
phin=(q-1)*(p-1)
print("trovato phi:",phin)
start=time.perf_counter()
d=Groups.mult_inv_euclid(e,phin)
print("trovato esponente privato: ", d," in ",time.perf_counter()-start," secondi")
print("decifrato:",Groups.fast_exp_mod(c, d, n))
