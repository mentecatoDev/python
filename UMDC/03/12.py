"""
Ejercicio 12

Escribir una función que reciba un número natural e imprima todos los números
que hay hasta ese número.
"""


def primos(n):
    print(1)
    if n >= 2:
        print(2)
    for i in range(3, n+1):
        primo = True
        for j in range(2, i):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(i)


primos(20)
