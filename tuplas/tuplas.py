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
        mails[line[1]] = mails.get(line[1],0) + 1
mails_list = []
for mail, count in list(mails.items()):
    mails_list += [(count, mail)]
mails_list.sort(reverse=True)
print("El correo con mayor número de envíos fue", mails_list[0][1])
Ejercicio 2
Escribir un programa que cuente la distribución horaria para el conjunto de los mensajes. Se debe extraer la hora desde la línea "From" buscando la cadena de tiempos y separándola en partes usando el caracter ":". Una vez que se hayan acumulado la cuenta para cada hora, visualizar el resultado, una por cada línea, ordenada por hora como se muestra a continuación:

Introduzca el nombre del fichero: mbox-short.txt
04 6
06 2
07 2
09 4
10 6
11 12
14 2
15 4
16 8
17 4
18 2
19 2

#pylint: disable = i0011, c0103
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
Ejercicio 3
Escribir un programa que lea un archivo e imprima las letras en orden decreciente de frecuencia de aparición. El programa debería convertir toda la entrada a minúsculas y solo contar las letras a-z (excluir la "ñ"). No se debeen contar espacios, dígitos, signos de puntuación o cualquier otro carácter. Buscar textos en diferentes lenguas y ver cómo la frecuencia de las letras varían entre lenguajes. Comparar los resultados con las tablas que se puede encontrar en wikipedia.org/wiki/Letter_frequencies.

#pylint: disable = i0011, c0103
"""
Ejercicio 3
===========
Escribir un programa que lea un archivo e imprima las letras en orden decreciente de
frecuencia de aparición. El programa debería convertir toda la entrada a minúsculas
y solo contar las letras a-z (excluir la "ñ"). No se debeen contar espacios, dígitos,
signos de puntuación o cualquier otro carácter. Buscar textos en diferentes lenguas y
ver cómo la frecuencia de las letras varían entre lenguajes. Comparar los resultados
con las tablas que se puede encontrar en wikipedia.org/wiki/Letter_frequencies.
"""
import string
try:
    fhandle = open(input("Introduzca el nombre del fichero: "))
except IOError:
    print("El fichero no existe")
    exit()
full_string = fhandle.read()
alphabet = dict()
for letter in full_string:
    letter = letter.lower()
    if letter in string.ascii_lowercase:
        alphabet[letter] = alphabet.get(letter, 0) + 1
total = 0
ordered_list = []
for key, value in alphabet.items():  
    total += alphabet[key]
    ordered_list += [(value, key)]
ordered_list.sort(reverse=True)
for tupla in ordered_list:
    print("%s %.2f%%" % (tupla[1], tupla[0]*100/total))
    
Introduzca el nombre del fichero: words.txt
o 9.57%
e 9.52%
t 8.62%
n 7.57%
a 7.52%
r 6.20%
s 6.10%
i 5.99%
u 4.73%
l 4.21%
h 3.73%
m 3.15%
d 3.15%
w 3.05%
g 2.94%
p 2.42%
c 2.37%
f 2.31%
y 2.21%
k 1.68%
v 1.37%
b 1.16%
x 0.32%
q 0.11%