"""
Ejercicio 4
===========
Añadir código al programa anterior para averiguar quién tiene más mensajes en
el fichero.
Después de leer todos los datos y esté creado el diccionario buscar a través
de él, usando un bucle máximo (ver la sección
[https://books.trinket.io/pfe/05-iterations.html] maximumloop) para
encontrar quién tiene más mensajes y mostrar en pantalla cuántos mensajes
tenía esa persona.
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
max = 0
mail = ""
for mail in mails:
    if mails[mail] > max:
        max = mails[mail];
        max_mail = mail;
print(max_mail, mails[max_mail])

