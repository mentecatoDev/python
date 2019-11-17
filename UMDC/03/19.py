"""
Ejercicio 19

Escribir un programa que reciba como entrada un año escrito en números
arábigos y muestre por pantalla el mismo año escrito en números romanos.
"""


def romano(anio):
    roma = ""
    for i in range(anio//1000):
        roma += "M"
    anio %= 1000
    d = anio // 100
    anio %= 100
    if d == 9:
        roma += "CM"
    elif d >= 5:
        roma += "D"
        for i in range(d-5):
            roma += "C"
    elif d == 4:
        roma += "CD"
    elif d <= 3:
        for i in range(d):
            roma += "C"
    d = anio // 10
    anio %= 10
    if d == 9:
        roma += "XC"
    elif d >= 5:
        roma += "L"
        for i in range(d-5):
            roma += "X"
    elif d == 4:
        roma += "XL"
    elif d <= 3:
        for i in range(d):
            roma += "X"
    d = anio
    if d == 9:
        roma += "IX"
    elif d >= 5:
        roma += "V"
        for i in range(d-5):
            roma += "I"
    elif d == 4:
        roma += "IV"
    elif d <= 3:
        for i in range(d):
            roma += "I"
    return roma


print(romano(2019))
