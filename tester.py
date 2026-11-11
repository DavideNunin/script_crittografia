#! /usr/bin/python3

import crypto_lib
import time
import random

def main():
    n=int(input("insert the module of the group: "))
    x=int(input("insert the number for which you want to find the multiplicative inverse: "))
    inv=crypto_lib.Groups.mult_inv_phi(x,n)
    print("the inverse is ",inv)

    n = int(input("let me get n: "))
    x = int(input("let me get x: "))
    y = int(input("let me get y: "))

    r, rp, np, d = crypto_lib.Montgomery.gen_radix(n)
    print(r,rp,np,d)

    print(crypto_lib.Montgomery.multiply(x, y, n, r, np, d))


if __name__ == "__main__":
    print("This script is a playground where you can test the crypto_lib module to verify how the various methods work")
    main()

#ext_euclid(int(input()),int(input()))
#a=int(input("insert a:"))
#b=-1
#while b < a:
#    b=random.randint(1,fast_exp(2,25)-1)
#while not isprime(b):
#    b=b+1
#print("found multiplicative group of order ",b-1)
#start=time.perf_counter()
#inv=mult_inv_brute(a,b)
#cut=time.perf_counter()-start
#print("multiplicative inverse of a in Zb: ",inv,"calculated in ",cut," seconds")
#start=time.perf_counter()
#inv=mult_inv_phi(a,b)
#cut=time.perf_counter()-start
#print("multiplicative inverse of a in Zb: ",inv,"calculated in ",cut," seconds")
#start=time.perf_counter()
#inv=mult_inv_euclid(a,b)
#cut=time.perf_counter()-start
#print("multiplicative inverse of a in Zb: ",inv,"calculated in ",cut," seconds")
