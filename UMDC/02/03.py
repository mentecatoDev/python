### Ejercicio 03
#
# Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos. Por ejemplo, si 
# recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto más grande que se puede obtener entre 
# ellos.


def mayor_producto(n1,n2,n3,n4):
    mayor = n1 * n2
    n1n3 = n1 * n3
    n1n4 = n1 * n4
    n2n3 = n2 * n3
    n2n4 = n2 * n4
    n3n4 = n3 * n4
    if n1n3 > mayor:
        mayor = n1n3
    if n1n4 > mayor:
        mayor = n1n4
    if n2n3 > mayor:
        mayor = n2n3
    if n2n4 > mayor:
        mayor = n2n4
    if n3n4 > mayor:
        mayor = n3n4
    return mayor


leyendo = True
while leyendo:
    try:
        num1 = int(input ("Introduce número 1 : "))
        num2 = int(input ("Introduce número 2 : "))
        num3 = int(input ("Introduce número 3 : "))
        num4 = int(input ("Introduce número 4 : "))
        leyendo = False
    except:
        print("Error en la introducción de datos\n")

print("El mayor producto entre ellos es: ", mayor_producto(num1,num2,num3,num4))

