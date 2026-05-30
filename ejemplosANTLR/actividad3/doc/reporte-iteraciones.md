# Reporte de iteraciones - RaraLang Compiler

## Iteracion 1 - Literales y print

**Que hace ahora:** compila `print` de enteros decimales, literales con base y strings.
Los strings se guardan en `.data` con etiquetas `str_N` y se imprimen con syscall 4.

**Gramatica:** se aceptan `INT`, `BASED_INT`, `STRING` y `printArg`.

**Listener/generador:** `visitPrintStat`, `visitLiteralExpr`, `_emit_print_int`,
`_emit_print_string`, `_parse_int_literal`.

**Decision auditada:** `[FF:16]` se convierte a decimal en Python durante compilacion,
por eso genera el mismo MIPS que `255`. Se restringieron bases a 2, 8, 10 y 16.

**Pruebas:** `01_01_int_literal` imprime `42`, `0`, `100`; `01_03_hex_vs_decimal`
imprime `255`, `255`; `01_05_string` imprime `hola mundo`.

**Limitaciones:** no hay concatenacion ni lectura de entrada.

*Revisado por Abdul. Correcciones: se documento el caso de base invalida como error de iteracion 8.*

## Iteracion 2 - Variables

**Que hace ahora:** permite asignar enteros a variables y leerlas en expresiones.

**Gramatica:** se agrego `ID ASSIGN expr` con el operador `<--` y `ID` como expresion.

**Listener/generador:** `visitAssignStat`, `visitVarExpr`, `_ensure_variable`.

**Decision auditada:** las etiquetas MIPS se generan como `var_nombre`, por eso una
variable llamada `add` no choca con la instruccion MIPS `add`.

**Pruebas:** `02_asignar_e_imprimir` imprime `42`; `02_dos_variables` imprime `10`,
`3`; `02_nombre_mips` imprime `100`, `200`, `300`; `02_reasignacion` imprime `5`,
`99`.

**Limitaciones:** las variables son globales. Leer una variable sin asignarla ahora
es error semantico para evitar un `0` silencioso.

*Revisado por Abdul. Correcciones: se endurecio el caso de variable no asignada.*

## Iteracion 3 - Aritmetica

**Que hace ahora:** compila suma, resta, multiplicacion, division entera y parentesis.

**Gramatica:** se agregaron `+`, `-`, `×`, `÷` y expresiones parentizadas.

**Listener/generador:** `visitAddSubExpr`, `visitMulDivExpr`, `visitParenExpr`.

**Decision auditada:** `×` y `÷` tienen mayor precedencia que `+` y `-`; `2 + 3 × 4`
genera resultado esperado `14`. La division constante entre cero detiene la
compilacion.

**Pruebas:** `03_01_aritmetica` imprime `13`, `7`, `30`, `3`, `24`, `14`, `20`;
`03_03_parentesis_variables` imprime `35`, `3`, `8`; `03_02_division_cero` falla
correctamente con `Division entre cero en una expresion constante`.

**Limitaciones:** no se detecta overflow aritmetico.

*Revisado por Abdul. Correcciones: se agrego una tercera prueba valida para cumplir la entrega.*

## Iteracion 4 - Operadores Unicode

**Que hace ahora:** compila modulo `⊞`, doble mas `⊠`, promedio entero `≈` y negacion
unaria `±`.

**Gramatica:** se agregaron cuatro operadores Unicode sobre `expr`.

**Listener/generador:** `visitModExpr`, `visitDoublePlusExpr`, `visitAvgExpr`,
`visitNegExpr`.

**Decision auditada:** `⊠` se implemento como `2a + b`, no como multiplicacion. Para
`≈` se usa `sra`, que en negativos redondea hacia abajo para division entre 2.

**Pruebas:** `04_modulo` imprime `1`, `2`; `04_doble_mas` imprime `13`, `7`;
`04_promedio` imprime `5`, `-2`, `-3`; `04_negacion` imprime `-8`, `5`;
`04_mixto` imprime `12`.

**Limitaciones:** la precedencia de operadores Unicode esta definida por la gramatica,
no por una convencion externa conocida.

*Revisado por Abdul. Correcciones: se verifico que `⊠` no se confundiera con `×`.*

## Iteracion 5 - If/else

**Que hace ahora:** compila condicionales con bloque y comparaciones.

**Gramatica:** se agregaron `if`, `else`, `{}`, y comparadores `==`, `!=`, `<`, `>`,
`<=`, `>=`.

**Listener/generador:** `visitIfStat`, `visitCompareExpr`, `visitBlock`.

**Decision auditada:** se eligieron bloques con llaves para que el final del cuerpo
sea explicito, ya que los saltos de linea se ignoran como whitespace.

**Pruebas:** `05_01_if_then` imprime `10`, `99`; `05_02_if_else` imprime `22`;
`05_03_comparaciones` imprime `1`, `2`, `3`.

**Limitaciones:** no hay `and`/`or`.

*Revisado por Abdul. Correcciones: se agregaron comparaciones para no depender solo de enteros 0/1.*

## Iteracion 6 - While/bloques

**Que hace ahora:** compila ciclos `while` y bloques anidados.

**Gramatica:** se agrego `while expr block`.

**Listener/generador:** `visitWhileStat`, `visitBlock`.

**Decision auditada:** el while evalua la condicion antes de entrar al cuerpo. Esto
se revisa con `06_02_while_falso_inicio`, que no imprime el valor dentro del ciclo.

**Pruebas:** `06_01_while_cuenta` imprime `3`, `2`, `1`; `06_02_while_falso_inicio`
imprime `7`; `06_03_while_con_if` imprime `1`, `2`, `20`, `3`.

**Limitaciones:** no hay `break` ni `continue`.

*Revisado por Abdul. Correcciones: se agrego prueba especifica para condicion falsa desde el inicio.*

## Iteracion 7 - Funciones

**Que hace ahora:** compila funciones sin parametros, `return` y llamadas dentro de
expresiones.

**Gramatica:** se agregaron `func ID() block`, `return expr` y `ID()`.

**Listener/generador:** `visitCallExpr`, `visitReturnStat`, `_compile_function`.

**Decision auditada:** cada llamada guarda y restaura `$ra`. Ademas, las llamadas
dentro de expresiones preservan registros temporales vivos para no perder operandos.

**Pruebas:** `07_01_funcion_simple` imprime `42`; `07_02_funcion_llama_funcion`
imprime `15`; `07_03_funcion_en_expresion` imprime `22`.

**Limitaciones:** no hay parametros ni variables locales.

*Revisado por Abdul. Correcciones: se corrigio el riesgo del bug de `$ra` en llamadas anidadas.*

## Iteracion 8 - Error handling

**Que hace ahora:** reporta errores semanticos claros y genera guardias de runtime
para division/modulo por cero cuando el divisor no es constante.

**Gramatica:** no depende solo de gramatica; se agrego validacion en el generador y
un error listener en `main.py`.

**Listener/generador:** `CompileError`, `_emit_division_guard`, validaciones en
`visitCallExpr`, `visitReturnStat`, `_parse_int_literal`, `_ensure_variable`.

**Decision auditada:** el compilador detiene la compilacion en el primer error para
no producir ASM inconsistente. Las variables no asignadas ahora son error.

**Pruebas:** `08_01_guard_division_runtime` genera ASM con mensaje `ERROR: division
entre cero`; `08_02_funcion_no_definida` falla con `Funcion no definida: fantasma`;
`08_03_variable_no_asignada` falla con `Variable no asignada: x`; `08_04_base_invalida`
falla con `Base no soportada: 3`.

**Limitaciones:** no hay recuperacion multiple de errores.

*Revisado por Abdul. Correcciones: se reemplazaron fallos silenciosos por mensajes defendibles.*

## Nota de verificacion

Se genero ASM para las pruebas compilables y se ejecuto con `spim` 9.1.24 desde la
terminal. Las salidas observadas coinciden con los outputs esperados listados en
este reporte, incluyendo el guard de runtime para division entre cero.
