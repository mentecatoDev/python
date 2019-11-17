"""
Ejercicio 17a

Escribir funciones que resuelvan los siguientes problemas:

a) Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también
sea divisible por 400.
"""


def bisiesto(anio):
    if anio % 4:
        return False
    else:
        if anio % 100:
            return True
        else:
            if anio % 400:
                return False
            else:
                return True


print(bisiesto(2017), bisiesto(2016), bisiesto(1800), bisiesto(2000))
