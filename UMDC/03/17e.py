"""
Ejercicio 17e

Escribir funciones que resuelvan los siguientes problemas:
e) Dada una fecha, indicar los dias que faltan hasta fin de año.
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


def dias_faltan(dia, mes, anio):
    if validar_fecha(dia, mes, anio):
        return dias_mes(mes, anio)-dia
    else:
        return -1


print(dias_faltan(1, 1, 2000))


def dias_fin_anio(dia, mes, anio):
    if validar_fecha(dia, mes, anio):
        dias = 0
        for m in range(mes+1, 12+1):
            dias += dias_mes(m, anio)
        dias += dias_faltan(dia, mes, anio)
        return dias
    else:
        return -1


print(dias_fin_anio(31, 12, 2000), dias_fin_anio(30, 11, 2000),
      dias_fin_anio(1, 1, 2015), dias_fin_anio(1, 1, 2016))
