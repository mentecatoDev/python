"""
Ejercicio 17c

Escribir funciones que resuelvan los siguientes problemas:
c) Dada una fecha (dia, mes, año), indicar si es válida o no.
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


def dias_mes(mes, anio):
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if bisiesto(anio):
            return 29
        else:
            return 28
    else:
        return -1


def validar_fecha(dia, mes, anio):
    dm = dias_mes(mes, anio)
    if dm == -1:
        return -1
    if dm < dia:
        return False
    elif mes > 12:
        return False
    else:
        return True


print(validar_fecha(29, 2, 2016), validar_fecha(29, 2, 2017),
      validar_fecha(3, 13, 2016), validar_fecha(5, 6, 1967))
