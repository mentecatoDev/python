"""
Ejercicio 01b

Escribir funciones que dada una cadena de caracteres:

cad = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"

b) Imprima los tres últimos caracteres.

### TESTS

>>> cad = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme'
>>> tres(cad)
'rme'

>>> tres('Rosa ha vuelto de la oscuridad')
'dad'
"""


def tres(cad):
    return(cad[-3:])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
