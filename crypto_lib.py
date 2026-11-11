import copy
import math

class NumberTheory:
    """Number theory operations"""

    @staticmethod
    def isprime(n):
        """Checks if n is prime"""
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
        """Factorizes n and returns a list of [prime, exponent]"""
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
        """Finds all divisors given the list of prime factors"""
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
        """Calculates Euler's totient function φ"""
        l = NumberTheory.factorize(n)
        val = 1
        for i in l:
            val *= (i[0]**i[1] - i[0]**(i[1]-1))
        return val

    @staticmethod
    def ext_euclid(a, b):
        """Extended Euclidean algorithm: returns [gcd, x, y] where ax + by = gcd"""
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
    """Modular arithmetic and group theory operations"""
    @staticmethod
    def fast_exp(x, y):
        """Fast exponentiation: calculates x^y"""
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
        """Fast modular exponentiation: calculates (x^y) mod n"""
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
        """Finds the multiplicative inverse using brute force"""
        for i in range(1, n):
            if (e * i) % n == 1:
                return i
        return None

    @staticmethod
    def mult_inv_phi(e, n):
        """Finds the multiplicative inverse using Euler's φ"""
        ph = NumberTheory.phi(n)
        return Groups.fast_exp(e, ph - 1) % n

    @staticmethod
    def mult_inv_euclid(e, n):
        """Finds the multiplicative inverse using the extended Euclidean algorithm"""
        a = NumberTheory.ext_euclid(e, n)
        if a[0] != 1:
            return None
        if a[1] < 0:
            a[1] = a[1] + n
        return a[1] % n

    @staticmethod
    def find_generator(modulo):
        """Finds a generator of the multiplicative group Z*_modulo"""
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
    """RSA specific operations"""
    @staticmethod
    def factorize_by_trial(n):
        """Factorizes n by finding a prime divisor (trial division)"""
        for i in range(2, math.ceil(math.sqrt(n))):
            if NumberTheory.isprime(i):
                if n % i == 0:
                    return i
        return None

class Montgomery:
    """Montgomery arithmetic operations"""
    @staticmethod
    def gen_radix(n):
        """Generates parameters for Montgomery arithmetic"""
        d = math.ceil(math.log2(n))
        d += 1
        r = 2 ** d
        vect = NumberTheory.ext_euclid(r, n)
        rp = vect[1]
        np = -vect[2]
        return r, rp, np, d

    @staticmethod
    def reduce(x, n, r, np, d):
        """Montgomery reduction"""
        tp = (x * np) % r
        x = x + n * tp
        x = x >> d  # Fix: was x << d, should be x >> d
        if x >= n:
            x = x - n
        return x

    @staticmethod
    def multiply(a, b, n, r, np, d):
        """Montgomery multiplication"""
        return Montgomery.reduce(a * b, n, r, np, d)
