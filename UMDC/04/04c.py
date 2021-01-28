"""
c) Escribir una función que reciba dos vectores y devuelva si son paralelos o no.

>>> parallel((3, -1), (-9, 3))
True
>>> parallel((2, 2, -1), (4, 4, -2))
True
>>> parallel((2, 2, -1), (4, 4, 1))
False
"""


def parallel(x, y):
    k = x[0]/y[0]
    for i in range(1, len(x)):
        if k != x[i]/y[i]:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
