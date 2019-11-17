"""
Ejercicio 15

Escribir una función que reciba por parámetro una dimensión n, e imprima la
matriz identidad correspondiente a esa dimensión.
"""


def matrizIdentidad(m):
    for i in range(m):
        linea = ""
        for j in range(m):
            if i != j:
                linea += "0 "
            else:
                linea += "1 "
        print(linea)


matrizIdentidad(10)
