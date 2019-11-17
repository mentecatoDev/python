"""
Ejercicio 08a

Potencias de dos
a) Escribir una función es_potencia_de_dos que reciba como parámetro un
número natural, y devuelva True si el número es una potencia de 2, y False
en caso contrario.
"""


def es_potencia_de_dos(n):
    while n != 1:
        if (n % 2) == 0:
            n = n / 2
        else:
            return False
    return True


def es_potencia_de_dos_2(n):
    from math import log2
    exp = log2(n)
    return (exp == int(exp))


print(es_potencia_de_dos(1), es_potencia_de_dos_2(1))
print(es_potencia_de_dos(2), es_potencia_de_dos_2(2))
print(es_potencia_de_dos(59), es_potencia_de_dos_2(59))
print(es_potencia_de_dos(256), es_potencia_de_dos_2(256))
