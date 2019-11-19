"""
Ejercicio 7a

Escribir funciones que dadas dos cadenas de caracteres:

b) Devuelva la que sea anterior en orden alfábetico. Por ejemplo, si recibe
"kde" y "gnome" debe devolver "gnome".
"""


def alfa(cad1, cad2):
    if cad1 < cad2:
        return cad1
    else:
        return cad2


print(alfa("kde", "gnome"))
