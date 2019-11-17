"""
Ejercicio 05

Escribir un programa que imprima todos los números pares entre dos números que
se le pidan al usuario.
"""


leyendo = True
while leyendo:
    try:
        inicial = int(input("Introduzca valor inicial: "))
        final = int(input("Introduzca valor final  : "))
        leyendo = False
    except ValueError:
        print("Introduzca solo valores numéricos enteros\n")

# Asegura que se comienza con un número par
inicial += inicial % 2
for i in range(inicial, final+1, 2):
    print(i)
