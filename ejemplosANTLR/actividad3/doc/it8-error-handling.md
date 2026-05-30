---
iteracion: 8
tema: Manejo de errores
---

# Iteracion 8 - Error handling

## Que se implemento

El compilador ahora reporta errores semanticos con mensajes claros:

- Division constante entre cero.
- Modulo constante entre cero.
- Funcion no definida.
- Funcion duplicada.
- Funcion sin `return`.
- `return` fuera de funcion.
- Variable leida antes de asignarse.
- Bases no soportadas en literales `[digitos:base]`.

Ademas, cuando el divisor es una variable y no se sabe en compilacion si vale cero,
el ASM generado incluye un guard en runtime que imprime un mensaje y termina.

## Auditoria

La especificacion inicial permitia reservar variables automaticamente en `.data`,
pero eso hacia que `print x` imprimiera `0` aunque el programador nunca asignara
`x`. Se cambio a error semantico porque es mas facil de defender en una entrega:
evita fallos silenciosos y obliga a que el programa RaraLang sea explicito.

Tambien se corrigio el manejo de bases: aunque Python acepta varias bases con `int`,
RaraLang solo documenta 2, 8, 10 y 16. Por eso `[12:3]` falla con un mensaje del
compilador.

## Pruebas

- `tests/08_iteracion_8/08_01_guard_division_runtime.rara` genera ASM que imprime `ERROR: division entre cero`.
- `tests/08_iteracion_8/08_02_funcion_no_definida.rara` falla al compilar con `Funcion no definida: fantasma`.
- `tests/08_iteracion_8/08_03_variable_no_asignada.rara` falla al compilar con `Variable no asignada: x`.
- `tests/08_iteracion_8/08_04_base_invalida.rara` falla al compilar con `Base no soportada: 3`.

## Limitaciones

No hay recuperacion de errores para continuar compilando despues del primer error.
El compilador detiene la compilacion en el primer problema encontrado, lo cual es
suficiente para una herramienta pequena y evita generar MIPS inconsistente.

*Revisado por Abdul. Correcciones: se cambiaron fallos silenciosos por errores explicitos y guardias de runtime.*
