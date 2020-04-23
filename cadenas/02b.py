"""
Ejercicio 02b

Escribir funciones que dada una cadena y un carácter:

b) Reemplace todos los espacios por el carácter. Ej: mi archivo de texto.txt y
_ debería devolver mi_archivo_de_texto.txt

### TESTS

>>> cad = 'En un lugar de la Mancha'
>>> cambiar(cad, "_")
'En_un_lugar_de_la_Mancha'

>>> cambiar2(cad, "_", 0)
'En un lugar de la Mancha'

>>> cambiar2(cad, "_", 100)
'En_un_lugar_de_la_Mancha'

>>> cambiar2(cad, "_", 2)
'En_un_lugar de la Mancha'

"""


def cambiar(cad, car):
    salida = ""
    for letra in cad:
        if letra == " ":
            salida += car
        else:
            salida += letra
    return salida


def cambiar2(cad, car, rmax):
    if rmax == 0:
        return cad
    salida = ""
    rep = 0
    long = len(cad)
    for i in range(long):
        if cad[i] == " ":
            salida += car
            rep += 1
            if rep == rmax:
                salida += cad[i+1:]
                break
        else:
            salida += cad[i]
    return salida


if __name__ == '__main__':
    import doctest
    doctest.testmod()
