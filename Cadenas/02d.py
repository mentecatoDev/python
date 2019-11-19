"""
Ejercicio 02d

Escribir funciones que dada una cadena y un carácter:

d) Inserte el carácter cada 3 dígitos en la cadena.
Ej. 2552552550 y . debería devolver 255.255.255.0
"""


def puntos(cad):
    if cad == "":
        return cad
    salida = ""
    numero_puntos = len(cad)//3
    for veces in range(numero_puntos):
        for trio in range(3):
            salida += cad[veces*3+trio]
        salida += "."
    salida += cad[numero_puntos*3:]
    if salida[-1] == ".":
        salida = salida[:-1]
    return salida


def puntos2(cad, rmax):
    if rmax == 0 or cad == "":
        return cad
    salida = ""
    long = len(cad)
    if rmax > long//3:
        numero_puntos = long//3
    else:
        numero_puntos = rmax
    for veces in range(numero_puntos):
        for trio in range(3):
            salida += cad[veces*3 + trio]
        salida += "."
    salida += cad[numero_puntos*3:]
    if salida[-1] == ".":
        return salida[:-1]
    return salida


print(puntos(""))
print(puntos("2"))
print(puntos("25"))
print(puntos("255"))
print(puntos("2552552550"))
print(puntos("25525525525"))
print(puntos("255255255255"))

print(puntos2("", 1))
print(puntos2("2", 1))
print(puntos2("25", 1))
print(puntos2("255", 1))
print(puntos2("2552552550", 1))
print(puntos2("25525525525", 1))
print(puntos2("255255255255", 1))

print(puntos2("", 3))
print(puntos2("2", 3))
print(puntos2("25", 3))
print(puntos2("255", 3))
print(puntos2("2552552550", 3))
print(puntos2("25525525525", 3))
print(puntos2("255255255255", 3))

print(puntos2("", 7))
print(puntos2("2", 7))
print(puntos2("25", 7))
print(puntos2("255", 7))
print(puntos2("2552552550", 7))
print(puntos2("25525525525", 7))
print(puntos2("255255255255", 7))
