"""
Ejercicio 02

Escribir una implementación propia de la función abs, que devuelva el valor
absoluto de cualquier valor que reciba.
"""


def abs(n):
    if n < 0:
        n = -n
    return n
