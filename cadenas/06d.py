"""
Ejercicio 6d

Escribir funciones que dada una cadena de caracteres:
d) Indique si se trata de un palíndromo. Por ejemplo, anita lava la tina es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

### TESTS

>>> palindromo('el bar es iman o zona miserable')
True

>>> palindromo('anytalava la tina')
False

>>> palindromo_2('antalava la tina')
False

>>> palindromo_2('anita la gorda lagartona no traga la droga latina')
True
"""


def palindromo(cad):
    cad_limpia = ""
    for car in cad:
        if car != " ":
            cad_limpia += car
    tramo1 = len(cad_limpia)//2
    tramo2 = tramo1 - (len(cad_limpia)+1) % 2
    return cad_limpia[:tramo1] == cad_limpia[:tramo2:-1]


def palindromo_2(cad):
    cad_limpia = ""
    for car in cad:
        if car != " ":
            cad_limpia += car
    return cad_limpia == cad_limpia[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
