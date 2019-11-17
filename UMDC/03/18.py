"""
Ejercicio 18
Suponiendo que el primer dia del año fue lunes, escribir una función que
reciba un número con el dia del año(de 1 a 366) y devuelva el dia de la semana
que le toca. Por ejemplo: si recibe 3 debe devolver miércoles, si recibe 9
debe devolver martes’.
"""


def dia_semana(dia):
    semana = dia % 7
    if semana == 0:
        return "domingo"
    elif semana == 1:
        return "lunes"
    elif semana == 2:
        return "martes"
    elif semana == 3:
        return "miércoles"
    elif semana == 4:
        return "jueves"
    elif semana == 5:
        return "viernes"
    else:
        return "sabado"


print(dia_semana(3), dia_semana(9), dia_semana(0))
