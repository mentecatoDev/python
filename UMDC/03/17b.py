"""
Ejercicio 17b
Escribir funciones que resuelvan los siguientes problemas:

b) Dado un mes, devolver la cantidad de dias correspondientes.
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


print(dias_mes(1, 2016), dias_mes(11, 2016),
      dias_mes(2, 2016), dias_mes(2, 2017))
