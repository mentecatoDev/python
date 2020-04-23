Ejercicio 5

En esta ocasión hay que registrar el nombre de dominio (en lugar de la dirección), es decir, desde dónde se enviaron los mensajes en lugar de de quién vino. Al final mostrar el contenido del diccionario.

Introduzca el nombre del fichero: mbox-short.txt iupui.edu 16
gmail.com 2
uct.ac.za 12
media.berkeley.edu 8
caret.cam.ac.uk 2
umich.edu 14

#pylint: disable = i0011, c0103
"""
Ejercicio 5
===========
En esta ocasión hay que registrar el nombre de dominio (en lugar de la
dirección), es decir, desde dónde se enviaron los mensajes en lugar de
de quién vino. Al final mostrar el contenido del diccionario.
"""
try:
    fhandle = open(input("Introduzca el nombre del fichero: "))
except IOError:
    print("El fichero no existe")
    exit()
domains = dict()
for line in fhandle:
    if line.startswith("From "):
        domain = line.split()[1].split("@")[1]
        domains[domain] = domains.get(domain,0) + 1
for line in domains:
    print(line, domains[line])
