# #### Ejercicio 09
# Modificar el programa anterior para que pueda generar fichas de un juego que puede tener números de 0 a n.

leyendo = True
while leyendo:
    try:
        n = int(input("Introduzca número máximo del dominó: "))
        leyendo = False
    except:
        print("Introduzca solo valores numéricos enteros\n")
for i in range (n+1):
    for j in range (i,n+1):
        print(i,j)

