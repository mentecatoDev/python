"""
Ejercicio 6

Reescribir el programa que solicita al usuario una lista de número y muestra
el valor máximo y mínimo de entre ellos y acaba con la palabra "done". Hacerlo
ahora almacenando los números en una lista y hacer uso de la funciones max() y
min().
"""

numbers_list = list()
done = False
while not done:
    reading = True
    while reading:
        string = input('Introduzca un número ("fin" para terminar):')
        if string == "fin":
            done = True
            break
        try:
            number = float(string)
            reading = False
        except IOError:
            print("Entrada incorrecta, pruebe de nuevo.")
            continue
        numbers_list.append(number)
print("El valor máximo es %.2f y el mínimo %.2f" % (max(numbers_list),
      min(numbers_list)))
