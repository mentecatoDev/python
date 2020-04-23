"""
Ejercicio 6b

Escribir funciones que dada una cadena de caracteres:

b) Devuelva solamente las letras vocales. Por ejemplo, si recibe "sin
consonantes" debe devolver "i ooae".

### TESTS

>>> vocales("Sin consonantes murciélago Guadalajara San Sebastián")
'i ooae uiéao uaaaaa a eaiá'
"""


def vocales(cad):
    consonantes = ""
    for letra in cad:
        if letra in "aeiouáéíóúAEIOUÁÉÍÓÚ ":
            consonantes += letra
    return consonantes


if __name__ == '__main__':
    import doctest
    doctest.testmod()
