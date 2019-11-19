"""
Ejercicio 5a

Escribir una función que dada una cadena de caracteres, devuelva:

a) La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial
Bus debe devolver USB.
"""


def siglas1(cad):
    cad = " " + cad.strip()
    sig = ""
    while True:
        i = cad.find(" ")
        if i != -1:
            cad = cad[i+1:]
            if cad[0] == " ":
                continue
            else:
                sig = sig + cad[0]
        else:
            return sig


def siglas2(cad):
    cad = " " + cad.strip()
    sig = ""
    i = cad.find(" ")
    while i != -1:
        cad = cad[i+1:]
        if cad[0] != " ":
            sig = sig + cad[0]
        i = cad.find(" ")
    return sig


print(siglas1("   Universal Serial     Bus     "))
print(siglas2("   Universal     Serial     Bus     "))
