"""
Ejercicio 8

Escribir una función que reciba una cadena de unos y ceros (es decir, un
número en representación binaria) y devuelva el valor decimal correspondiente.

### TESTS

>>> bin_to_dec("11000100")
196
"""


def bin_to_dec(num):
    dec = 0
    for car in num:
        dec *= 2
        if car == "1":
            dec += 1
    return dec


if __name__ == '__main__':
    import doctest
    doctest.testmod()
