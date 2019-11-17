"""
Ejercicio 16c

Escribir funciones que permitan encontrar:

c) La intersección de dos rectas (dadas las pendientes y ordenada al origen
de cada recta). Nota: validar que no sean dos rectas con la misma pendiente,
antes de efectuar la operación.
"""


def raices(a, b, c):
    h = b*b - 4*a*c
    if h < 0:
        imaginaria = True
        h = -h
    else:
        imaginaria = False
    rh = h ** (1/2)
    if imaginaria:
        r1r = -b/(2*a)
        r1i = rh/(2*a)
        r2r = r1r
        r2i = -r1i
    else:
        r1r = (-b + rh)/(2*a)
        r1i = 0
        r2r = (-b - rh)/(2*a)
        r2i = 0
    return (r1r, r1i, r2r, r2i)


print(raices(1, -5, 6))
