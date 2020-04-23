"""
Ejercicio 01a

Escribir funciones que dada una cadena de caracteres:

a) Retorne los dos primeros caracteres.

### TESTS

>>> cad = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme'
>>> dos(cad)
'En'
"""


def dos(cad):
    return cad[:2]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
