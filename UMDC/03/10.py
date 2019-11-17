"""
Ejercicio 10

Escribir un programa que le pida al usuario que ingrese una sucesión de
números naturales (primero uno, luego otro, y así hasta que el usuario
ingrese -1 como condición de salida). Al final, el programa debe imprimir
cuántos números fueron ingresados, la suma total de los valores y el
promedio.
"""

i = 0
total = 0
while True:
    leyendo = True
    while leyendo:
        try:
            n = float(input("Introduzca un número :"))
            leyendo = False
        except ValueError:
            print("Introduzca un valor numérico")
    if n == -1:
        break
    else:
        total += n
        i += 1
print("Se ingresaron", i, "números que suman", total)
print("El promedio es de: ", total / i)
