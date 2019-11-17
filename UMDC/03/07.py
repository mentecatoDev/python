"""
Ejercicio 07

Algoritmo de Euclides
Implementar en python el algoritmo de Euclides para calcular el máximo común
divisor de dos números n y m, dado por los siguientes pasos.
Teniendo n y m, se obtiene r, el resto de la división entera de m/n.
Si r es cero, n es el mcd de los valores iniciales.
Se reemplaza m ← n, n ← r, y se vuelve al primer paso.
Hacer un seguimiento del algoritmo implementado para los siguientes pares de
números: (15,9);(9,15); (10,8); (12,6).
"""


def euclides(m, n):
    if m < n:
        cambio = m
        m = n
        n = cambio
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n


print(euclides(15, 9), euclides(9, 15), euclides(10, 8), euclides(12, 6))
