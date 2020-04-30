"""
Ejercicio 01c

Escribir funciones que dada una cadena de caracteres:

cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

c) Retorne dicha cadena cada dos caracteres. Ej.: "recta" imprime "rca"

### TESTS

>>> cad = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme'
>>> cada_dos(cad)
'E nlgrd aMnh ecy oben ueoaodre'

>>> cada_dos("recta")
'rca'

>>> cada_dos_2(cad)
'E nlgrd aMnh ecy oben ueoaodre'
"""


def cada_dos(cad):
    cadena = ""
    for i in range(0, len(cad), 2):
        cadena += cad[i]
    return(cadena)


def cada_dos_2(cad):
    return(cad[::2])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
