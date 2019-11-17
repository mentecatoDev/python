"""
Ejercicio 13

Escribir una función que reciba un dígito y un número natural, y decida
numéricamente si el dígito se encuentra en la notación decimal del segundo.
"""


def digitoEn(d, n):
    while n:
        if n % 10 == d:
            return True
        n = n // 10
    return False


print(digitoEn(7, 89343733), digitoEn(7, 0), digitoEn(7, 7),
      digitoEn(7, 700), digitoEn(7, 897), digitoEn(7, 8980))
