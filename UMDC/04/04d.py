"""
d) Escribir una función que reciba un vector y devuelva su norma.
>>> magnitude((3,4))
5.0
>>> magnitude((3,4,5))
7.0710678118654755
"""


def magnitude(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * x[i]
    return sum ** (1/2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()