"""
Ejercicio 03

Escribir un programa que lea un log de correo construya un histograma usando
un diccionario para contar cuántos mensajes se recibieron de cada dirección
de correo electrónico y visualice los resultados.
"""

try:
    fhandle = open(input("Introduzca el nombre del fichero: "))
except IOError:
    print("El fichero no existe")
    exit()
mails = dict()
for line in fhandle:
    if line.startswith("From "):
        line = line.split()
        mails[line[1]] = mails.get(line[1],0) + 1
for mail in mails:
    print(mail, mails[mail])
