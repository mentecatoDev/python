"""
1.- Escribir una función que reciba una tupla de elementos e indique si se
encuentran ordenados de menor a mayor o no.

>>> tupla1 = (1,2,3,4,5,6,6,7,8,9,10)
>>> test_sorted(tupla1)
True

>>> tupla2 = (1,2,3,5,4,6,7,8,9,10)
>>> test_sorted(tupla2)
False

>>> tupla3 = ()
>>> test_sorted(tupla3)
-1

>>> tupla4 = (5,)
>>> test_sorted(tupla4)
True
"""


def test_sorted(tupla):
    if tupla == ():
        return -1
    previous = tupla[0]
    for item in tupla:
        if previous <= item:
            previous = item
        else:
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
