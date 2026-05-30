---
iteracion: 6
tema: While y bloques
---

# Iteracion 6 - While y bloques

## Que se implemento

El compilador acepta ciclos `while` con bloque:

```
while i <= 3 {
    print i
    i <-- i + 1
}
```

El cuerpo puede contener asignaciones, `print`, `if`, otros `while` y `return` si
esta dentro de una funcion.

## Auditoria

La decision tecnica fue generar dos etiquetas por ciclo: una para volver a evaluar
la condicion y otra para salir. Esto evita ejecutar el cuerpo si la condicion es
falsa desde el inicio, que es uno de los casos borde de la rubrica.

El modelo podia haber generado un esquema tipo `do while` por accidente si ponia la
evaluacion despues del cuerpo. Se audito revisando el ASM de
`06_02_while_falso_inicio.asm`: primero evalua `i`, luego salta al final si es cero.

## Pruebas

- `tests/06_iteracion_6/06_01_while_cuenta.rara` imprime `3`, `2`, `1`.
- `tests/06_iteracion_6/06_02_while_falso_inicio.rara` imprime `7`.
- `tests/06_iteracion_6/06_03_while_con_if.rara` imprime `1`, `2`, `20`, `3`.

## Limitaciones

No existen `break` ni `continue`. Los ciclos deben terminar modificando variables
usadas en la condicion.

*Revisado por Abdul. Correcciones: se agrego una prueba donde el while no debe entrar al cuerpo.*
