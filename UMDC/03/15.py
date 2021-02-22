"""
Ejercicio 15

Escribir una función que reciba por parámetro una dimensión n, e imprima la
matriz identidad correspondiente a esa dimensión.
"""


def matrizIdentidad(m):
    for i in range(m):
        linea = ""
        for j in range(m):
            if i == j:
                linea += "1 "
            else:
                linea += "0 "
        print(linea[:-1])


matrizIdentidad(5)
