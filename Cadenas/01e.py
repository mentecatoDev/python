"""
Ejercicio 01e

Escribir funciones que dada una cadena de caracteres:

cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

e) Imprima la cadena en un sentido y en sentido inverso.

Ej: reflejo imprime reflejoojelfer.

"""


def reflejo(cad):
    salida = cad
    for i in range(len(cad)-1, -1, -1):
        salida += cad[i]
    print(salida)


def reflejo_2(cad):
    print(cad + cad[::-1])


cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
reflejo(cad)
reflejo("reflejo")
reflejo_2("reflejo")
