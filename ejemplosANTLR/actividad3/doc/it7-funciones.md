---
iteracion: 7
tema: Funciones sin parametros y return
---

# Iteracion 7 - Funciones

## Que se implemento

El compilador acepta funciones sin parametros:

```
func respuesta() {
    return 42
}

print respuesta()
```

Las llamadas a funcion se pueden usar como expresiones. El valor de retorno viaja en
`$v0`, siguiendo la convencion usual de MIPS.

## Auditoria

El caso critico de esta iteracion es una funcion que llama a otra. Si el compilador
no guarda `$ra`, la llamada interna sobrescribe la direccion de retorno y el programa
regresa al lugar equivocado.

Se corrigio esto guardando `$ra` en el stack antes de cada `jal` y restaurandolo
despues. Tambien se guardan registros temporales vivos (`$t0`-`$t9`) alrededor de
llamadas usadas dentro de expresiones, para que `x + siete()` no pierda el valor de
`x` mientras se ejecuta la funcion.

## Pruebas

- `tests/07_iteracion_7/07_01_funcion_simple.rara` imprime `42`.
- `tests/07_iteracion_7/07_02_funcion_llama_funcion.rara` imprime `15`.
- `tests/07_iteracion_7/07_03_funcion_en_expresion.rara` imprime `22`.

## Limitaciones

Las funciones no tienen parametros ni variables locales. Las variables siguen siendo
globales. Esta decision mantiene el alcance de la iteracion enfocado en llamadas,
`return`, `$v0` y preservacion de `$ra`.

*Revisado por Abdul. Correcciones: se agrego preservacion de `$ra` y de temporales vivos para llamadas anidadas.*
