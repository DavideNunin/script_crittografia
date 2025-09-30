#! /usr/bin/python3

import crypto_lib
import time
import random

def main():
    n=int(input("inserisci il modulo del gruppo: "))
    x=int(input("inserisci il numero di cui vuoi trovare l' inverso moltiplicativo: "))
    inv=crypto_lib.Groups.mult_inv_phi(x,n)
    print("l' inverso è ",inv)

    n = int(input("let me get n: "))
    x = int(input("let me get x: "))
    y = int(input("let me get y: "))

    r, rp, np, d = crypto_lib.Montgomery.gen_radix(n)
    print(r,rp,np,d)

    print(crypto_lib.Montgomery.multiply(x, y, n, r, np, d))


if __name__ == "__main__":
    print("Questo script è un playground dove è possibile testare il modulo crypto_lib per verificare il funzionamento dei vari metodi")
    main()

#ext_euclid(int(input()),int(input()))
#a=int(input("inserire a:"))
#b=-1
#while b < a:
#    b=random.randint(1,fast_exp(2,25)-1)
#while not isprime(b):
#    b=b+1
#print("trovato gruppo moltiplicativo di ordine ",b-1)
#start=time.perf_counter()
#inv=mult_inv_brute(a,b)
#cut=time.perf_counter()-start
#print("inverso moltiplicativo di a in Zb: ",inv,"calcolato in ",cut," secondi")
#start=time.perf_counter()
#inv=mult_inv_phi(a,b)
#cut=time.perf_counter()-start
#print("inverso moltiplicativo di a in Zb: ",inv,"calcolato in ",cut," secondi")
#start=time.perf_counter()
#inv=mult_inv_euclid(a,b)
#cut=time.perf_counter()-start
#print("inverso moltiplicativo di a in Zb: ",inv,"calcolato in ",cut," secondi")
