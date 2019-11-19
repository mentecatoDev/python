"""
Ejercicio 6c

Escribir funciones que dada una cadena de caracteres:

c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe
vestuario debe devolver vistaerou.
"""


def revocaliza(cad):
    revoca = ""
    voc = "aeiouaAEIOUA"
    for car in cad:
        if car in "aeiouAEIOU":
            revoca += voc[voc.find(car)+1]
        else:
            revoca += car
    return revoca


print(revocaliza("vestUariO"))
