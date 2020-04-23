"""
Ejercicio 4

Escribir una función que reciba una cadena que contiene un largo número entero
y devuelva una cadena con el número y las separaciones de miles. Por ejemplo,
si recibe 1234567890, debe devolver 1.234.567.890

### TESTS

>>> puntua("1234567890")
'1.234.567.890'

>>> puntua1("1234567890")
'1.234.567.890'

>>> puntua2("1234567890")
'1.234.567.890'

>>> puntua3("1234567890")
'1.234.567.890'

"""

import locale


def puntua(cad):
    """DocString
    """
    long = len(cad)
    primeros = long % 3
    if primeros > 0:
        salida = cad[0:primeros]+"."
    else:
        salida = ""
    for i in range(0, (long//3)*3, 3):
        salida = salida + cad[primeros+i:primeros+i+3] + "."
    return salida[:-1]


def puntua1(cad):
    """DocString
    """
    try:
        return '{0:,}'.format(int(cad)).replace(",", ".")
    except TypeError:
        return -1


def puntua2(cad):
    """DocString
    """
    locale.setlocale(locale.LC_ALL, '')
    try:
        return locale.format_string("%d", int(cad), grouping=True)
    except TypeError:
        return -1


def puntua3(cad):
    """DocString
    """
    locale.setlocale(locale.LC_ALL, '')
    try:
        return '{:n}'.format(int(cad))
    except TypeError:
        return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
