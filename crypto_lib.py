import copy
import math

class NumberTheory:
    """Operazioni di teoria dei numeri"""

    @staticmethod
    def isprime(n):
        """Verifica se n è primo"""
        if n == 2:
            return True
        if n < 2:
            return False
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def factorize(n):
        """Fattorizza n e restituisce lista di [primo, esponente]"""
        a = n
        ret = []
        i = 2
        while a != 1:
            if NumberTheory.isprime(i):
                cont = 0
                while a % i == 0:
                    a = a // i
                    cont = cont + 1
                if cont != 0:
                    ret.append([i, cont])
            i = i + 1
        return ret

    @staticmethod
    def divisors(factors):
        """Trova tutti i divisori dato l'elenco di fattori primi"""
        primefactors = []
        for i in factors:
            for j in range(0, i[1]):
                primefactors.append(i[0])
        print("primefactors", primefactors)

        divis = set()
        for i in range(1, (2**len(primefactors)) - 1):
            select = bin(i)[2:].zfill(len(primefactors))
            newdiv = 1
            for j in range(0, len(select)):
                if select[j] == '1':
                    newdiv *= primefactors[-j]
            divis.add(newdiv)

        returned = list(divis)
        print("returned", returned)
        return returned

    @staticmethod
    def phi(n):
        """Calcola la funzione φ di Eulero"""
        l = NumberTheory.factorize(n)
        val = 1
        for i in l:
            val *= (i[0]**i[1] - i[0]**(i[1]-1))
        return val

    @staticmethod

    def ext_euclid(a, b):
        """Algoritmo esteso di Euclide: restituisce [gcd, x, y] dove ax + by = gcd"""
        if a > b:
            u = [a, 1, 0]
            v = [b, 0, 1]
        else:
            u = [b, 0, 1]
            v = [a, 1, 0]

        w = [-200, -200, -200]
        while w[0] != 0:
            r = u[0] % v[0]
            intermediate = u[0] - r
            q = int(intermediate / v[0])
            for i in range(0, 3):
                w[i] = u[i] - q*v[i]
            u = copy.deepcopy(v)
            v = copy.deepcopy(w)

        return u


class Groups:
    """Operazioni di aritmetica modulare e teoria dei gruppi"""

    @staticmethod
    def fast_exp(x, y):
        """Esponenziazione veloce: calcola x^y"""
        exp = bin(y)[2:]
        if y == 0:
            return 1
        if y == 1:
            return x

        c = x
        for i in range(1, len(exp)):
            c = c * c
            if exp[i] == '1':
                c = c * x
        return c

    @staticmethod
    def fast_exp_mod(x, y, n):
        """Esponenziazione modulare veloce: calcola (x^y) mod n"""
        exp = bin(y)[2:]
        if y == 0:
            return 1
        if y == 1:
            return x % n

        c = x % n
        for i in range(1, len(exp)):
            c = (c * c) % n
            if exp[i] == '1':
                c = (c * x) % n
        return c % n

    @staticmethod
    def mult_inv_brute(e, n):
        """Trova l'inverso moltiplicativo con forza bruta"""
        for i in range(1, n):
            if (e * i) % n == 1:
                return i
        return None

    @staticmethod
    def mult_inv_phi(e, n):
        """Trova l'inverso moltiplicativo usando φ di Eulero"""
        ph = NumberTheory.phi(n)
        return Groups.fast_exp(e, ph - 1) % n

    @staticmethod
    def mult_inv_euclid(e, n):
        """Trova l'inverso moltiplicativo usando l'algoritmo esteso di Euclide"""
        a = NumberTheory.ext_euclid(e, n)
        if a[0] != 1:
            return None
        if a[1] < 0:
            a[1] = a[1] + n
        return a[1] % n

    @staticmethod
    def find_generator(modulo):
        """Trova un generatore del gruppo moltiplicativo Z*_modulo"""
        attempts = NumberTheory.divisors(NumberTheory.factorize(NumberTheory.phi(modulo)))
        attempts.sort()

        for i in range(2, modulo):
            if NumberTheory.ext_euclid(i, modulo)[0] == 1:
                flag = True
                for divisor in attempts:
                    if Groups.fast_exp_mod(i, divisor, modulo) == 1:
                        flag = False
                        break
                if flag:
                    return i
        return None


class RSA:
    """Operazioni specifiche per RSA"""

    @staticmethod
    def factorize_by_trial(n):
        """Fattorizza n cercando un divisore primo (trial division)"""
        for i in range(2, math.ceil(math.sqrt(n))):
            if NumberTheory.isprime(i):
                if n % i == 0:
                    return i
        return None

class Montgomery:
    """Operazioni per l'aritmetica di Montgomery"""

    @staticmethod
    def gen_radix(n):
        """Genera i parametri per l'aritmetica di Montgomery"""
        d = math.ceil(math.log2(n))
        d += 1
        r = 2 ** d
        vect = NumberTheory.ext_euclid(r, n)
        rp = vect[1]
        np = -vect[2]
        return r, rp, np, d

    @staticmethod
    def reduce(x, n, r, np, d):
        """Riduzione di Montgomery"""
        tp = (x * np) % r
        x = x + n * tp
        x = x >> d  # Fix: era x << d, dovrebbe essere x >> d
        if x >= n:
            x = x - n
        return x

    @staticmethod
    def multiply(a, b, n, r, np, d):
        """Moltiplicazione di Montgomery"""
        return Montgomery.reduce(a * b, n, r, np, d)
