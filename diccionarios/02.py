"""
Ejercicio 02

Escribe un programa que contabilice cada mensaje de correo electrónico
por el día de la semana en que se envió. El proceso buscará líneas que
comiencen con "From" mirarán la tercera palabra de la línea y registrará
la cuenta para cada día de la semana. Al final del programa visualizar
los totales de cada día.
"""
try:
    fhandle = open(input("Introduzca el nombre del fichero: "))
except IOError:
    print("El fichero no existe")
    exit()
days_of_the_week = dict()
for line in fhandle:
    if line.startswith("From "):
        day = line.split()[2]
        days_of_the_week[day] = days_of_the_week.get(day, 0) + 1
day_es = ["Lunes    ", "Martes   ", "Miércoles", "Jueves   "
          , "Viernes  ", "Sábado   ", "Domingo  "]
day_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in range(7):
    if day_en[day] in days_of_the_week:
        print("%s : %3d" % (day_es[day], days_of_the_week[day_en[day]]))
