"""
Ejercicio 20
Programa de astrologia: el usuario debe ingresar el dia y mes de su cumpleaños
y el programa le debe decir a qué signo corresponde.

Nota:
    Aries: 21 de marzo al 20 de abril.
    Tauro: 21 de abril al 21 de mayo.
    Geminis: 22 de mayo al 21 de junio.
    Cancer: 22 de junio al 23 de julio.
    Leo: 24 de julio al 23 de agosto.
    Virgo: 24 de agosto al 23 de septiembre.
    Libra: 24 de septiembre al 23 de octubre.
    Escorpio: 24 de octubre al 22 de noviembre.
    Sagitario: 23 de noviembre al 21 de diciembre.
    Capricornio: 22 de diciembre al 20 de enero.
    Acuario: 21 de enero al 19 de febrero.
    Piscis: 20 de febrero al 20 de marzo.
"""


def astro(dia, mes):
    if mes == 1:
        if dia >= 21:
            return "Acuario"
        else:
            return "Capricornio"
    elif mes == 2:
        if dia >= 20:
            return "Piscis"
        else:
            return "Acuario"
    elif mes == 3:
        if dia >= 21:
            return "Aries"
        else:
            return "Piscis"
    elif mes == 4:
        if dia >= 21:
            return "Tauro"
        else:
            return "Aries"
    elif mes == 5:
        if dia >= 22:
            return "Géminis"
        else:
            return "Tauro"
    elif mes == 6:
        if dia >= 22:
            return "Cáncer"
        else:
            return "Géminis"
    elif mes == 7:
        if dia >= 24:
            return "Leo"
        else:
            return "Cáncer"
    elif mes == 8:
        if dia >= 24:
            return "Virgo"
        else:
            return "Leo"
    elif mes == 9:
        if dia >= 24:
            return "Libra"
        else:
            return "Virgo"
    elif mes == 10:
        if dia >= 24:
            return "Escorpio"
        else:
            return "Libra"
    elif mes == 11:
        if dia >= 23:
            return "Sagitario"
        else:
            return "Escorpio"
    elif mes == 12:
        if dia >= 22:
            return "Capricornio"
        else:
            return "Sagitario"


print(astro(5, 6), astro(29, 12), astro(23, 2),
      astro(15, 4), astro(29, 5), astro(13, 5))
