
"""
4.- Vectores

a) Escribir una función que reciba dos vectores y devuelva su
producto escalar.

>>> scalar((1, 4), (6, 2))
14
>>> scalar((1, 4, 5), (6, 2, 3))
29
"""


def scalar(x, y):
    p = list()
    for i in range(len(x)):
        p.append(x[i]*y[i])
    return sum(p)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
