"""
Ejercicio 5a

Escribir una función que dada una cadena de caracteres, devuelva:

a) La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial
Bus debe devolver USB.

### TESTS

>>> siglas1(" Universal Serial     Bus     ")
'USB'
>>> siglas2("   Universal     Serial     Bus     ")
'USB'
>>> siglas3("   Universal     Serial     Bus     ")
'USB'
"""


def siglas1(cad):
    if cad == '':
        return ''
    cad = " " + cad.strip()
    sig = ""
    i = 0
    while i != -1:
        i += 1
        if cad[i] != " ":
            sig = sig + cad[i]
        i = cad.find(" ", i)
    return sig


def siglas2(cad):
    if cad == '':
        return ''
    cad = " " + cad.strip()
    sig = ""
    i = 0
    while i != -1:
        cad = cad[i+1:]
        if cad[0] != " ":
            sig = sig + cad[0]
        i = cad.find(" ")
    return sig


def siglas3(cad):
    if cad == '':
        return ''
    palabras = cad.split()
    sig = ''
    for palabra in palabras:
        sig = sig + palabra[0]
    return sig


if __name__ == '__main__':
    import doctest
    doctest.testmod()