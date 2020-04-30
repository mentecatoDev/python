"""
Ejercicio 02a

Escribir funciones que dada una cadena y un carácter:

a) Inserte el carácter entre cada letra de la cadena. Ej: separar y , debería
devolver s,e,p,a,r,a,r

### TESTS

>>> cad = "En un lugar de la Mancha"

>>> separar(cad)
'E,n, ,u,n, ,l,u,g,a,r, ,d,e, ,l,a, ,M,a,n,c,h,a'

>>> separar2(cad, 0)
'En un lugar de la Mancha'

>>> separar2(cad, 24)
'E,n, ,u,n, ,l,u,g,a,r, ,d,e, ,l,a, ,M,a,n,c,h,a'

>>> separar2(cad, 100)
'E,n, ,u,n, ,l,u,g,a,r, ,d,e, ,l,a, ,M,a,n,c,h,a'

>>> separar2("separar", 2)
's,e,parar'
"""


def separar(cad):
    salida = ""
    for letra in cad:
        salida += letra + ","
    return salida[:-1]


def separar2(cad, rmax):
    if rmax == 0:
        return cad
    salida = ""
    rep = 0
    for i in range(len(cad)-1):
        salida = salida + cad[i] + ","
        rep += 1
        if rep == rmax:
            salida = salida + cad[i+1:]
            return salida
    salida += cad[len(cad)-1]
    return salida


if __name__ == '__main__':
    import doctest
    doctest.testmod()
