"""
Ejercicio 04

Escribir una función que reciba un número entero k e imprima su
descomposición en factores primos.

>>> fact_primos(24)
1
2
2
2
3

>>> fact_primos(100)
1
2
2
5
5

>>> fact_primos(12)
1
2
2
3

>>> fact_primos(11)
1
11

>>> fact_primos(1)
1

>>> fact_primos(0)
1

"""


def fact_primos(n):
    if n < 2:
        print(1)
    else:
        i = 2
        print(1)
        while (n/2 + 1) > i:
            if n % i == 0:
                print(i)
                n //= i
            else:
                i += 1
        print(n)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
