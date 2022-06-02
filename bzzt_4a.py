import math
import random


def losuj(n):
    wylosowane = []

    for i in range(n):
        wylosowane.append(random.randint(0, 100000000))

    return wylosowane


def nwd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def wzgl_pierwsza(x, y):
    return nwd(x, y) == 1


def rozdziel(losy, n):
    pierwsze = []
    for i in range(0, n, 2):
        if wzgl_pierwsza(losy[i], losy[i+1]):
            pierwsze.append([losy[i], losy[i+1]])
    return pierwsze


def main(n):
    pierwsze = rozdziel(losuj(2*n), 2*n)
    odsetek = len(pierwsze) / n
    pi = math.sqrt(6/odsetek)
    print(pi)


if __name__ == "__main__":
    n = int(input("Ile par wylosowac?: "))
    for i in range(10):
        main(n)
