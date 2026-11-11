#! /usr/bin/python3


def main():
print("This script is used to visualize the multiplication operation on the set of residue classes modulo n. This is a cyclic group only if n is a prime number")
n=int(input("insert the cardinality of the group: "))
a=[]
for i in range(1,n):
    b=[]
    for j in range(1,n):
        b.append(i*j%n)
    a.append(b.copy())
for i in a:
    print(i)


if __name__ == "__main__":
    main()
