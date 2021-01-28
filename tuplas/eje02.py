"""
Ejercicio 2
===========
Escribir un programa que cuente la distribución horaria para el conjunto
de los mensajes. Se debe extraer la hora desde la línea "From" buscando
la cadena de tiempos y separándola en partes usando el caracter ":". Una
vez que se hayan acumulado la cuenta para cada hora, visualizar el
resultado, una por cada línea, ordenada por hora.
"""

try:
    fhandle = open(input("Introduzca el nombre del fichero: "))
except IOError:
    print("El fichero no existe")
    exit()

time = dict()
for line in fhandle:
    if line.startswith("From "):
        hour = line.split()[5].split(":")[0]
        time[hour] = time.get(hour, 0) + 1
hours_list = []
for hour, count in list(time.items()):
    hours_list += [(hour, count)]
hours_list.sort()
for hour, count in hours_list:
    print(hour, count)
