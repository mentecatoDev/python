"""
Ejercicio 01d

Escribir funciones que dada una cadena de caracteres:

cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

d) Dicha cadena en sentido inverso.

Ej.: ¡Hola mundo! debe imprimir !odnum aloH¡
"""


def inversa(cad):
    salida = ""
    for i in range(len(cad)-1, -1, -1):
        salida += cad[i]
    print(salida)


def inversa_2(cad):
    print(cad[::-1])


cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
inversa(cad)
inversa("¡Hola mundo!")
inversa_2(cad)
