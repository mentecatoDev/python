"""
Ejercicio 1
Revisar un programa previo de la siguiente forma: Leer y analizar
las líneas "From" y extraer las direcciones de la línea. Contar el
número de mensajes de cada persona usando un diccionario. Después
de leer todos los datos, crear una lista de tuplas de la forma
(contador, correo) desde el diccionario, ordenarla en orden inverso
y mostrar la persona con mayor número de envíos.
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
        mails[line[1]] = mails.get(line[1], 0) + 1
mails_list = []
for mail, count in list(mails.items()):
    mails_list += [(count, mail)]
mails_list.sort(reverse=True)
print("El correo con mayor número de envíos fue", mails_list[0][1])
