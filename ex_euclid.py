#! /usr/bin/python3
import math
print("This script illustrates how the extended Euclidean algorithm works. It is one of the foundational algorithms of asymmetric cryptography because:")
print("it allows finding the multiplicative inverse of a number quickly")
print("it verifies if 2 numbers are coprime by finding the greatest common divisor")
a=int(input("insert a:"))
b=int(input("insert b:"))
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
print("gcd:",u)
print("bezout coefficients: chi=",xua,"eta:",xub)
