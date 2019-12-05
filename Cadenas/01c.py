"""
Ejercicio 01c

Escribir funciones que dada una cadena de caracteres:

cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

c) Imprima dicha cadena cada dos caracteres. Ej.: "recta" debería imprimir "rca"
"""


def cada_dos(cad):
    cadena = ""
    for i in range(0, len(cad), 2):
        cadena += cad[i]
    print(cadena)


def cada_dos_2(cad):
    print(cad[::2])


cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
cada_dos(cad)
cada_dos("recta")
cada_dos_2(cad)
