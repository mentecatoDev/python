"""
Ejercicio 5a

Escribir una función que dada una cadena de caracteres, devuelva:

b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por
ejemplo, si recibe república argentina debe devolver República Argentina.
"""


def mayus(cad):
    cad = cad.strip() + " "
    sig = ""
    i = cad.find(" ")
    while i != -1:
        if i != 0:
            sig = sig + cad[0:i].capitalize() + " "
        cad = cad[i+1:]
        i = cad.find(" ")
    return sig[:-1]


print(mayus("La confianza pública en ellos tendrá que ser destruida",
            "completamente para acabar realmente con ellos"))
