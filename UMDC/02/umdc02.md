## Un mundo de código 02



**Ejercicio 01.10.** Escribir dos funciones que permitan calcular:

- La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
- La cantidad de horas, minutos y segundos de un tiempo dado en segundos.

**Ejercicio 01.11.** Usando las funciones del ejercicio anterior, escribir un programa que lea de  teclado dos tiempos expresados en horas, minutos y segundos; las sume y  muestre el resultado en horas, minutos y segundos por pantalla.

**Ejercicio 01.12.** Escribir una función que dados cuatro números, devuelva el mayor producto de dos de ellos. Por ejemplo, si recibe los números `1`, `5`, `-2`, `-4` debe devolver `8`, que es el producto más grande que se puede obtener entre ellos.

**Ejercicio 01.13** Área de un triángulo en base a sus puntos:

1) Escribir una función que dado un vector al origen (definido por sus puntos `x`, `y`), devuelva la norma del vector, dada por `(x^2 + y^2) ^ 1/2`

2) Escribir una función que dados dos puntos en el plano (`x1`, `y1` y `x2`, `y2`), devuelva la resta de ambos (debe devolver un par de valores).

3) Utilizando las funciones anteriores, escribir una función que dados dos puntos en el plano (`x1`, `y1` y`x2`, `y2`), devuelva la distancia entre ambos.

4) Escribir una función que reciba un vector al origen (definido por sus puntos `x`, `y`) y devuelva un vector equivalente, normalizado (debe devolver un par de valores).

5) Utilizando las funciones anteriores (`b` y `d`), escribir una función que dados dos puntos en el plano (`x1`, `y1` y `x2`, `y2`), devuelva el vector dirección unitario correspondiente a la recta que los une.

6) Escribir una función que reciba un punto `(x, y)`, una dirección unitaria de una recta `(dx, dy)` y un punto perteneciente a esa recta `(cx, cy)` y devuelva la proyección del punto sobre la recta.

**Diseño del algoritmo:**

1. Al punto a proyectar `(x, y)` restarle el punto de la recta `(cx, cy)`
2. Obtener la matriz de proyección `P`, dada por: `p11 = dx^2`, `p12 = p21 = dx * dy`, `p22 = dy^2`.
3. Multiplicar la matriz `P` por el punto obtenido en el paso 1: `rx = p11 * x + p12 * y`, `ry = p21 * x + p22 * y`.
4. Al resultado obtenido sumar el punto restado en el paso 1, y devolverlo.

7) Escribir una función que calcule el área de un triángulo a partir de su base y su altura.

8) Utilizando las funciones anteriores escribir una función que reciba tres puntos en el plano (`x1`, `y1`,`x2`, `y2` y `x3`, `y3`) y devuelva el área del triángulo correspondiente.