#! /usr/bin/python3
import math
print("Questo script illustra il funzionamento dell' algoritmo di euclide esteso, è uno degli algoritmi alla base della crittografia asimmetrica poichè:")
print("permette di trovare l' inverso moltiplicativo di un numero in maniera veloce")
print("verifica se 2 numeri sono coprimi trovando il massimo comun divisore")
a=int(input("inserisci a:"))
b=int(input("inserisci b:"))
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
print("mcd:",u)
print("coefficienti bezout: chi=",xua,"eta:",xub)
