"""
Ejercicio 09b

Números perfectos y números amigos

b) Usando la función anterior, escribir una función que imprima los primeros m números tales que la suma de sus divisores sea igual a sí mismo (es decir los primeros m números perfectos).
"""


def suma_divisores(n):
    suma = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            suma += i


def perfecto(m):
    n = 1
    for i in range(m):
        while n != suma_divisores(n):
            n += 1
        print(n)
        n += 1


perfecto(5)
