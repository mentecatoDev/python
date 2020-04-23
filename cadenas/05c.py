"""
Ejercicio 5b

Escribir una función que dada una cadena de caracteres, devuelva:

c) Las palabras que comiencen con la letra A. Por ejemplo, si recibe "Antes de
ayer" debe devolver "Antes ayer".

### TESTS

>>> aes("    Antes de  fdfff      Antonio    ayer     ")
'Antes Antonio ayer'
"""


def aes(cad):
    cad = " " + cad.strip() + " "
    i = cad.find(" ")
    sig = ""
    while i != -1:
        cad = cad[1:]
        encontrado = cad.find(" ")
        if (encontrado != -1) and (cad[0] in "aA"):
            sig = sig + cad[0:encontrado] + " "
        cad = cad[encontrado:]
        i = cad.find(" ")
    return sig[:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
