"""
Ejercicio 7a

Escribir funciones que dadas dos cadenas de caracteres:

a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo,
"cadena" es una subcadena de "subcadena".

### TESTS
>>> subcadena("subcadena", "cadena")
True
>>> subcadena("subcalena", "cadena")
False
>>> subcadena_2("subcadena", "cadena")
True
>>> subcadena_2("subcalena", "cadena")
False

"""


def subcadena(cad, subcad):
    return cad.find(subcad) != -1


def subcadena_2(cad, subcad):
    return subcad in cad


if __name__ == '__main__':
    import doctest
    doctest.testmod()
