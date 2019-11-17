"""
Ejercicio 09cd

Números perfectos y números amigos

c) Usando la primera función, escribir una función que imprima las primeras m
parejas de números(a,b), tales que la suma de los divisores de a es igual a b
y la suma de los divisores de b es igual a a(es decir las primeras m parejas
de números amigos).
"""


def suma_divisores(n):
    suma = 1
    for i in range(2, n//2+1):
        if n % i == 0:
            suma += i
    return suma


def perfectos(m):
    a = 0
    for i in range(m):
        while True:
            a += 1
            b = suma_divisores(a)
            if suma_divisores(b) == a and a != b and a < b:
                print(a, b)
                break


perfectos(6)

"""
d) Proponer optimizaciones a las funciones anteriores para disminuir el tiempo de ejecución.
"""
