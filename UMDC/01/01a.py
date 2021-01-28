"""
Ejercicio 01a.

a) Escribir un ciclo definido para imprimir por pantalla todos los números
entre 10 y 20.

>>> for number in range(10,21):
...     print(number)
10
11
12
13
14
15
16
17
18
19
20
"""
import doctest

for n in range(10, 21):
    print(n)


doctest.testmod()
