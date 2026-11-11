#! /usr/bin/python3
import math
def factorize(n):
    a=n
    ret=[]
    i=2
    while a!=1:
        if isprime(i):
            cont=0
            while a%i==0:
                a=a/i
                cont=cont+1
            if cont!=0:
                ret.append([i,cont])
        i=i+1
    return ret


def phi(n):
    l=factorize(n)
    val=1
    for i in l:
        val*=(i[0]**i[1]-i[0]**(i[1]-1))
    return val

def isprime(n):
    if n==2:
        return True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0 :
            return False
    return True
def coprimes(a,b):
    u=a
    v=b
    xua=1
    xub=0
    xva=0
    xvb=1
    w=1
    while w!=0:
        w=u%v
        xwa=xua - math.floor(u/v)*xva
        xwb=xub - math.floor(u/v)*xvb
        u=v
        xua=xva
        xub=xvb
        v=w
        xva=xwa
        xvb=xwb
    if u==1:
        return 1
    else:
        return 0

def find_gen(n):
    a=[]
    for i in range(1,n):
        flag=True
        for j in range(1,math.ceil(n/2)):
            if (i**j%n)==1:
                flag=False
        if flag :
            a.append(i)
            break
    for i in range(a[0],n):
        if coprimes(i,n-1):
            a.append(a[0]**i%n)
    return a

def remove_dup(a):
    a= list(dict.fromkeys(a))
    return a

n=int(input("insert the order of the group: "))
#print(factorize(int(n)))
#print (phi(int(n)))
print("the number of generators is: ",phi(n))
print(remove_dup(find_gen(n)))
