"""
Ejercicio 11bc

Escribir una función que reciba dos números como parámetros, y devuelva
cuántos múltiplos del primero hay, que sean menores que el segundo.
b) Implementarla utilizando un ciclo while, que multiplique el primer número
hasta que sea mayor que el segundo.
"""


def num_mul(m, n):
    i = 1
    mul = m
    while mul <= n:
        i += 1
        mul *= i
    return (i-1)


print(num_mul(12, 360))

"""
c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos
operaciones?

La primera es más clara pero la segunda es manifiestamente más rápida.
"""
