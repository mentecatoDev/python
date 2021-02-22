"""
Ejercicio 6a

Escribir funciones que dada una cadena de caracteres:

a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe
'Algoritmos o logaritmos' debe devolver 'lgrtms  lgrtms'.

### TESTS

>>> consonantes('Algoritmos o logaritmos')
'lgrtms  lgrtms'
"""


def consonantes(cad):
    consonante = ""
    for letra in cad:
        if letra not in "aeiouAEIOUáéíóúÁÉÍÓÚ":
            consonante += letra
    return consonante


if __name__ == '__main__':
    import doctest
    doctest.testmod()
