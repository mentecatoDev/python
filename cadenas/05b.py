"""
Ejercicio 5a

Escribir una función que dada una cadena de caracteres, devuelva:

b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por
ejemplo, si recibe 'república argentina' debe devolver 'República Argentina'.

### TESTS

>>> mayus('La confianza pública en ellos tendrá que ser destruida '\
          'completamente para acabar realmente con ellos')
'La Confianza Pública En Ellos Tendrá Que Ser Destruida Completamente\
 Para Acabar Realmente Con Ellos'
"""


def mayus(cad):
    cad = cad.strip() + " "
    sig = ""
    i = cad.find(" ")
    while i != -1:
        if i != 0:
            sig = sig + cad[0:i].capitalize() + " "
        cad = cad[i+1:]
        i = cad.find(" ")
    return sig[:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()