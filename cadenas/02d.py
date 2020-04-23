"""
Ejercicio 02d

Escribir funciones que dada una cadena y un carácter:

d) Inserte el carácter cada 3 dígitos en la cadena.
Ej. 2552552550 y . debería devolver 255.255.255.0

### TESTS

>>> puntos("", ".")
''
>>> puntos("2", ".")
'2'
>>> puntos("25", ".")
'25'
>>> puntos("255", ".")
'255'
>>> puntos("2552552550", ".")
'255.255.255.0'
>>> puntos("25525525525", ".")
'255.255.255.25'
>>> puntos("255255255255", ".")
'255.255.255.255'

>>> puntos2("", ".", 1)
''
>>> puntos2("2", ".", 1)
'2'
>>> puntos2("25", ".", 1)
'25'
>>> puntos2("255", ".", 1)
'255'
>>> puntos2("2552552550", ".", 1)
'255.2552550'
>>> puntos2("25525525525", ".", 1)
'255.25525525'
>>> puntos2("255255255255", ".", 1)
'255.255255255'

>>> puntos2("", ".", 3)
''
>>> puntos2("2", ".", 3)
'2'
>>> puntos2("25", ".", 3)
'25'
>>> puntos2("255", ".", 3)
'255'
>>> puntos2("2552552550", ".", 3)
'255.255.255.0'
>>> puntos2("25525525525", ".", 3)
'255.255.255.25'
>>> puntos2("255255255255", ".", 3)
'255.255.255.255'

>>> puntos2("", ".", 7)
''
>>> puntos2("2", ".", 7)
'2'
>>> puntos2("25", ".", 7)
'25'
>>> puntos2("255", ".", 7)
'255'
>>> puntos2("2552552550", ".", 7)
'255.255.255.0'
>>> puntos2("25525525525", ".", 7)
'255.255.255.25'
>>> puntos2("255255255255", ".", 7)
'255.255.255.255'
"""


def puntos(cad, car):
    if cad == "":
        return cad
    salida = ""
    numero_puntos = len(cad)//3
    for veces in range(numero_puntos):
        for trio in range(3):
            salida += cad[veces*3 + trio]
        salida += car
    salida += cad[numero_puntos*3:]
    if salida[-1] == car:
        salida = salida[:-1]
    return salida


def puntos2(cad, car, rmax):
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
        salida += car
    salida += cad[numero_puntos*3:]
    if salida[-1] == car:
        return salida[:-1]
    return salida


if __name__ == '__main__':
    import doctest
    doctest.testmod()
