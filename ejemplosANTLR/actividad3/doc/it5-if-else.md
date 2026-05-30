---
iteracion: 5
tema: Condicionales if/else y comparaciones
---

# Iteracion 5 - Condicionales

## Que se implemento

El compilador acepta sentencias `if` con bloque obligatorio y `else` opcional:

```
if x {
    print 1
} else {
    print 0
}
```

Tambien acepta comparaciones enteras como expresiones:

- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>=`

Una comparacion produce `1` si es verdadera y `0` si es falsa. Esto permite usarla
en `if`, `while`, asignaciones o `print`.

## Auditoria

La decision importante fue no inventar palabras como `then` o `endif`. Se eligieron
bloques con `{ ... }` porque la gramatica previa no conservaba saltos de linea como
tokens; sin delimitadores, seria ambiguo decidir donde termina el cuerpo del `if`.

Tambien se decidio que cualquier entero distinto de cero cuenta como verdadero y `0`
como falso. Esa regla es compatible con MIPS porque los saltos pueden comparar contra
`$zero` directamente.

## Pruebas

- `tests/05_iteracion_5/05_01_if_then.rara` imprime `10`, `99`.
- `tests/05_iteracion_5/05_02_if_else.rara` imprime `22`.
- `tests/05_iteracion_5/05_03_comparaciones.rara` imprime `1`, `2`, `3`.

## Limitaciones

No hay operadores booleanos `and`/`or`. Si se necesitan condiciones compuestas, se
pueden expresar con variables temporales o con comparaciones separadas.

*Revisado por Abdul. Correcciones: se agregaron bloques explicitos y comparaciones para evitar una sintaxis ambigua.*
