"""
Ejercicio 02a

Escribir funciones que dada una cadena y un carácter:

a) Inserte el carácter entre cada letra de la cadena. Ej: separar y , debería
devolver s,e,p,a,r,a,r
"""


def separar(cad):
    salida = ""
    for letra in cad:
        salida = salida + letra + ","
    return salida[:len(salida)-1]


def separar2(cad, rmax):
    if rmax == 0:
        return cad
    salida = ""
    rep = 0
    for i in range(len(cad)-1):
        salida = salida + cad[i] + ","
        rep += 1
        if rep == rmax:
            salida = salida + cad[i+1:]
            return salida
    salida += cad[len(cad)-1]
    return salida


cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
print(separar(cad))
print(separar2(cad, 0))
print(separar2(cad, 57))
print(separar2(cad, 100))
print(separar2("separar", 2))
