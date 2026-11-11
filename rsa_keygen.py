#! /usr/bin/python3
import time
import crypto_lib
import random


def main():
    print("This script illustrates in a very simplified way how the generation of a public/private key pair works for the RSA algorithm. It is NOT a secure algorithm and must absolutely not be used in the production of real RSA keys")
    print("Prime numbers must be chosen with other techniques and must meet certain requirements to avoid creating weak keys (they must be far apart from each other)")
    bitq = int(input("bit size of prime q:"))
    bitp = int(input("bit size of prime p:"))
    d = None
    start = time.perf_counter()
    while d is None:
        p = random.randint( crypto_lib.Groups.fast_exp(2, bitp-1)-1, crypto_lib.Groups.fast_exp(2, bitp)-1)
        while crypto_lib.NumberTheory.isprime(p) is False:
            p -=1
        q = random.randint(crypto_lib.Groups.fast_exp(2, bitq-1)-1, crypto_lib.Groups.fast_exp(2, bitq)-1)
        while crypto_lib.NumberTheory.isprime(q) is False:
            q -=1
        print("found primes q and p in ",time.perf_counter()-start," seconds")
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


    print("key generation completed in ", time.perf_counter()-start, " seconds")
    print("p: ", p)
    print("q: ", q)
    print("phi: ", phin)
    print("n: ", n)
    print("e: ", e)
    print("d: ", d)

    m = int(input("insert m (<n):"))
    start = time.perf_counter()
    c = crypto_lib.Groups.fast_exp_mod(m, e, n)
    print("encryption completed in ", time.perf_counter()-start, " seconds")
    print("c =  ", c)
    start = time.perf_counter()
    print("decrypted: ", crypto_lib.Groups.fast_exp_mod(c, d, n))
    print("decryption completed in ", time.perf_counter()-start, " seconds")

if __name__ == "__main__":
    main()
