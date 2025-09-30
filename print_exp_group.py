#! /usr/bin/python3
print("Questo script serve per visualizzare l' operazione di esponenziazione sulle classi di resto modulo n, l' insieme delle classi di resto è un gruppo ciclico rispetto al prodotto solo se n è un numero primo")
n=int(input("inserisci la cardinalità del gruppo: "))
a=[]
for i in range (1,n):
    b=[]
    for j in range (1,n):
        b.append(i**j%n)
    a.append(b.copy())
for i in a:
    print(i)
