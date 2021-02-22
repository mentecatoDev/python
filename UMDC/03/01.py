"""
3.1. Escribir funciones que resuelvan los siguientes problemas:

    Dado un número entero n, indicar si es o no par.
    Dado un número entero n, indicar si es o no primo.


"""

def par(n):
    """
    >>> par(10)
    True

    >>> par(11)
    False

    >>> par(1)
    False

    >>> par(0)
    True

    >>> par(-10)
    True
    """
    return not(n % 2)

def primo(n):
    """
    >>> primo(10)
    False

    >>> primo(5)
    True
    
    >>> primo(1)
    True
    
    >>> primo(0)
    False
    
    >>> primo(17)
    True
    
    >>> primo(100)
    False
    
    >>> primo(51)
    False

    """

    if not n:
        return False
    prim = True
    for i in range(2, int(n**(1//2))):
        if not(n % i):
            prim = False
    return prim
       

if __name__ == "__main__":
    import doctest
    doctest.testmod()
