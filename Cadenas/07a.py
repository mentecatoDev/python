"""
Ejercicio 7a

Escribir funciones que dadas dos cadenas de caracteres:

a) Indique si la segunda cadena es una subcadena de la primera. Por ejemplo,
"cadena" es una subcadena de "subcadena".
"""


def subcadena(cad, subcad):
    return cad.find(subcad) != -1


def subcadena_2(cad, subcad):
    return subcad in cad


print(subcadena("subcadena", "cadena"))
print(subcadena_2("subcadena", "cadena"))
