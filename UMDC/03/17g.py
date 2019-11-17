"""Ejercicio 17g."""

"""
Escribir funciones que resuelvan los siguientes problemas:

g) Dadas dos fechas (dia1, mes1, año1, dia2, mes2, año2), indicar el tiempo
transcurrido entre ambas, en años, meses y dias. Nota: en todos los casos,
involucrar las funciones escritas previamente cuando sea posible.
"""


def bisiesto(anio):
    """Devuelve True si el anio es bisiesto."""
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
    """Devuelve los días de cualquier mes teniendo en cuenta el anio."""
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


def dias_principio(dia, mes, anio):
    if validar_fecha(dia, mes, anio):
        if bisiesto(anio):
            return 365 - dias_fin_anio(dia, mes, anio)
        else:
            return 364 - dias_fin_anio(dia, mes, anio)
    else:
        return -1


def dias_transcurridos(dia1, mes1, anio1, dia2, mes2, anio2):
    if anio1 == anio2:
        total = -dias_principio(dia1, mes1, anio1) + \
            dias_principio(dia2, mes2, anio2)
    else:
        total = dias_fin_anio(dia1, mes1, anio1) + \
            dias_principio(dia2, mes2, anio2)+1
        for a in range(anio1+1, anio2):
            if bisiesto(a):
                total += 366
            else:
                total += 365
    return total


print(dias_transcurridos(1, 1, 2001, 31, 12, 2002))
