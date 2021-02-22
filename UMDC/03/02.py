"""
Ejercicio 02

Escribir una implementación propia de la función abs, que devuelva el valor
absoluto de cualquier valor que reciba.




"""


def abs(n):
    """
    TEST:
    
    >>> abs(5)
    5

    >>> abs(-5)
    5

    >>> abs(0)
    0
    """
    
    if n < 0:
        n = -n
    return n

if __name__ == '__main__':
    import doctest
    doctest.testmod()