"""
Ejercicio 6d

Escribir funciones que dada una cadena de caracteres:
d) Indique si se trata de un palíndromo. Por ejemplo, anita lava la tina es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
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


print(palindromo("antalava la tina"))
print(palindromo_2("anytalava la tina"))
