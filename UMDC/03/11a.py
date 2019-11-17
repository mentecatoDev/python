"""
Ejercicio 11
Escribir una función que reciba dos números como parámetros, y devuelva
cuántos múltiplos del primero hay, que sean menores que el segundo.

a) Implementarla utilizando un ciclo for, desde el primer número hasta el
segundo.
"""


def numMulFor(m, n):
    numMul = 0
    for i in range(m, n+1):
        if i % m == 0:
            numMul += 1
    return numMul


print(numMulFor(12, 360))
