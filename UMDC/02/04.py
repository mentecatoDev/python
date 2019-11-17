"""
Ejercicio 04
Área de un triángulo en base a sus puntos

a) Escribir una función que dado un vector al origen (definido por sus puntos
x, y), devuelva la norma del vector, dada por (x^2 + y^2) ^ 1/2
http://www.ub.edu/glossarimateco/content/norma-de-un-vector
"""


def norma(x, y):
    return (x*x + y*y)**(1/2)


"""
2) Escribir una función que dados dos puntos en el plano (x1, y1 y x2, y2),
devuelva la resta de ambos (debe devolver un par de valores).
"""


def resta(x1, y1, x2, y2):
    return (x1-x2, y1-y2)


"""
3) Utilizando las funciones anteriores, escribir una función que dados dos
puntos en el plano (x1, y1 x2, y2), devuelva la distancia entre ambos.
"""


def distancia(x1, y1, x2, y2):
    (x, y) = resta(x1, y1, x2, y2)
    return norma(x, y)


"""
4) Escribir una función que reciba un vector al origen (definido por sus
puntos x, y) y devuelva un vector equivalente, normalizado (debe devolver
un par de valores).
https://es.wikipedia.org/wiki/Vector_unitario
"""


def vector_unitario(x, y):
    n = norma(x, y)
    return (x/n, y/n)


"""
5) Utilizando las funciones anteriores ( 2) y 4) ), escribir una función que
dados dos puntos en el plano (x1, y1 y x2, y2), devuelva el vector dirección
unitario correspondiente a la recta que los une.
"""


def vector_unitario2(x1, y1, x2, y2):
    (x, y) = resta(x2, y2, x1, y1)
    return vector_unitario(x, y)


"""
6) Escribir una función que reciba un punto (x, y), una dirección unitaria de
una recta (dx, dy) y un punto perteneciente a esa recta (cx, cy) y devuelva
la proyección del punto sobre la recta.
(Notas.- Una recta puede estar definida por dos puntos o bien por un vector y
un punto de la misma)

Diseño del algoritmo:
Al punto a proyectar (x, y) restarle el punto de la recta (cx, cy)
Obtener la matriz de proyección P, dada por:
    p11 = dx^2, p12 = p21 = dx * dy, p22 = dy^2
Multiplicar la matriz P por el punto obtenido en el paso 1:
    rx = p11 * x + p12 * y, ry = p21 * x + p22 * y
Al resultado obtenido sumar el punto restado en el paso 1, y devolverlo.
"""


def proyeccion(x, y, dx, dy, cx, cy):
    (t1, t2) = resta(x, y, cx, cy)
    p11 = dx*dx
    p12 = dx*dy
    p21 = p12
    p22 = dy*dy
    rx = p11*t1 + p12*t2
    ry = p21*t1 + p22*t2
    rx += cx
    ry += cy
    return (rx, ry)


"""
7) Escribir una función que calcule el área de un triángulo a partir de su
base y su altura.
"""


def area_triangulo(b, h):
    return b*h/2


"""
8) Utilizando las funciones anteriores escribir una función que reciba tres
puntos en el plano (x1, y1, x2, y2 y x3, y3) y devuelva el área del
triángulo correspondiente.
"""


def area_vectorial(x1, y1, x2, y2, x3, y3):
    (dos_uno_x, dos_uno_y) = resta(x2, y2, x1, y1)
    (dos_tres_x, dos_tres_y) = resta(x3, y3, x1, y1)
    area = dos_uno_x*dos_tres_y - dos_uno_y*dos_tres_x
    if area < 0:
        area = -area
    return area/2


def area_proyeccion(x1, y1, x2, y2, x3, y3):
    base = distancia(x1, y1, x3, y3)
    (dx, dy) = vector_unitario2(x1, y1, x3, y3)
    (px, py) = proyeccion(x2, y2, dx, dy, x3, y3)
    altura = distancia(x2, y2, px, py)
    return area_triangulo(base, altura)
