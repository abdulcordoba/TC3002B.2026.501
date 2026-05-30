# Reporte de iteraciones - RaraLang Compiler

**Integrantes:** Marcela Hernandez Ramirez (A01658023) y Mariana Fernandez De la Torre (A01657317).

**Modelos usados:** principalmente Codex con GPT-5.5 (default). En las iteraciones
2 y 4 tambien probamos Claude Code (CLI de Anthropic) con Claude Haiku 4.5
(`claude-haiku-4-5-20251001`) para contrastar resultados; las reflexiones
detalladas de esas dos iteraciones quedaron en `doc/it2-variables.md` y
`doc/it4-unicode-ops.md`.

Cada iteracion la trabajamos asi: leiamos la guia, le armabamos un prompt al modelo
(a partir del template), revisabamos el codigo que devolvia y lo probabamos con
nuestros propios `.rara` antes de pasarlo a SPIM. Casi siempre algo se tenia que
ajustar a mano, y eso es lo que esta documentado en cada seccion bajo "donde se
equivoco el modelo". Cuando el modelo acerto a la primera tambien lo dejamos dicho.

## Iteracion 1 - Literales y print

**Que hace ahora:** el compilador agarra un `print` con un entero, una cadena o un
literal en otra base y lo convierte a MIPS que corre en SPIM. Las cadenas se
guardan en `.data` con etiquetas `str_0`, `str_1`, etc., y se imprimen con la
syscall 4.

**Gramatica:** se aceptan `INT`, `BASED_INT` (`[digitos:base]`), `STRING` y la
regla `printArg`.

**Listener/generador:** `visitPrintStat`, `visitLiteralExpr`, `_emit_print_int`,
`_emit_print_string`, `_parse_int_literal`.

**Decision auditada:** `[FF:16]` se convierte a decimal en Python al momento de
compilar, asi que el MIPS resultante es identico al de `print 255`. Esto es comodo
porque no hay que escribir conversion en MIPS, pero significa que cualquier base
rara tiene que validarse en el compilador, no en el simulador.

**Donde se equivoco el modelo:** la primera version aceptaba cualquier base que
`int(s, base)` pudiera procesar, hasta base 36. Lo vimos cuando probamos `[ZZ:36]`
y el programa lo compilaba sin chistar. Le pusimos un whitelist `(2, 8, 10, 16)`
en `_parse_int_literal` y dejamos el caso de base invalida como prueba de
iteracion 8.

**Pruebas:** `01_01_int_literal` imprime `42`, `0`, `100`; `01_03_hex_vs_decimal`
imprime `255` dos veces (uno desde decimal, otro desde hex); `01_05_string`
imprime `hola mundo`.

**Limitaciones:** no hay concatenacion ni lectura de entrada (no era requisito).

*Revisado por Marcela y Mariana. Correcciones: acotamos las bases validas y movimos el caso de base invalida a la iteracion 8.*

## Iteracion 2 - Variables

**Que hace ahora:** ya se pueden declarar variables enteras con `x <-- 10` y
leerlas en expresiones o `print`. Cada variable se reserva en `.data` la primera
vez que se asigna.

**Gramatica:** se agrego `ID ASSIGN expr` con el operador `<--` y `ID` como
expresion valida.

**Listener/generador:** `visitAssignStat`, `visitVarExpr`, `_ensure_variable`.

**Decision auditada:** todas las etiquetas en `.data` llevan prefijo `var_`. Asi
una variable llamada `add` se vuelve `var_add` en MIPS y no choca con el
mnemonico `add`. Suena obvio pero el modelo no lo hizo solo.

**Donde se equivoco el modelo:** la version inicial usaba el nombre crudo como
etiqueta (`add: .word 0`). SPIM no tira error al ensamblar, pero las instrucciones
que mencionaban `add` empezaban a ambiguar. Lo cazamos con `02_nombre_mips.rara`
(donde usamos variables llamadas `add`, `sub`, `div`) y forzamos el prefijo.

**Pruebas:** `02_asignar_e_imprimir` imprime `42`; `02_dos_variables` imprime
`10` y `3`; `02_nombre_mips` imprime `100`, `200`, `300`; `02_reasignacion`
imprime `5` y luego `99`.

**Limitaciones:** las variables son globales. Leer una que no se asigno antes
ahora es error semantico (lo endurecimos en la iteracion 8 para evitar un cero
silencioso).

*Revisado por Marcela y Mariana. Correcciones: prefijo `var_` en todas las etiquetas y endurecimos el caso de variable no asignada.*

## Iteracion 3 - Aritmetica

**Que hace ahora:** suma, resta, multiplicacion entera, division entera y
parentesis. Tambien detecta division entre cero cuando el divisor es una
constante literal.

**Gramatica:** se agregaron `+`, `-`, `×`, `÷` y la regla de expresion
parentizada.

**Listener/generador:** `visitAddSubExpr`, `visitMulDivExpr`, `visitParenExpr`.

**Decision auditada:** `×` y `÷` tienen mayor precedencia que `+` y `-` porque
asi quedaron en la gramatica (las alternativas de `expr` se evaluan en orden). Lo
verificamos con `2 + 3 × 4` que da `14`, no `20`.

**Donde se equivoco el modelo:** la primera version emitia `div $t0, $t1` y
luego `move $a0, $t0` sin acordarse de `mflo`. El cociente se quedaba en HI/LO y
imprimia basura. Lo vimos porque `print 9 ÷ 3` no daba `3`. Le agregamos `mflo`
inmediatamente despues del `div`.

**Pruebas:** `03_01_aritmetica` imprime `13, 7, 30, 3, 24, 14, 20`;
`03_03_parentesis_variables` imprime `35, 3, 8`; `03_02_division_cero` esta
hecho para FALLAR al compilar con el mensaje `Division entre cero en una
expresion constante`.

**Limitaciones:** no se detecta overflow.

*Revisado por Marcela y Mariana. Correcciones: agregamos `mflo` despues de cada `div` y la prueba de division entre cero.*

## Iteracion 4 - Operadores Unicode

**Que hace ahora:** funcionan los cuatro operadores raros del lenguaje: modulo
`⊞`, doble mas `⊠`, promedio entero `≈` y negacion unaria `±`.

**Gramatica:** cuatro reglas mas sobre `expr`, una por operador.

**Listener/generador:** `visitModExpr`, `visitDoublePlusExpr`, `visitAvgExpr`,
`visitNegExpr`.

**Decision auditada:** `⊠` se implemento como `2a + b` (`sll left, left, 1; add
left, left, right`), NO como multiplicacion. Para `≈` usamos `sra` (shift
aritmetico) porque en negativos redondea hacia menos infinito, que es lo que
queda mas natural para "promedio entero".

**Donde se equivoco el modelo:** esta fue la iteracion donde el modelo mas se
confundio. La primera version de `⊠` lo trataba como sinonimo de `×` (suponemos
que se contamino con LaTeX, donde `\boxtimes` se ve como multiplicacion). Daba
`4 ⊠ 5 = 20` en vez de `13`. Releimos la guia, le aclaramos en el prompt que
`⊠` es `2a+b` y verificamos a mano con `0 ⊠ 7 = 7` y `4 ⊠ 5 = 13`. Lo mismo
revisamos con `≈` en negativos: `±3 ≈ ±2` deberia dar `-3` (no `-2`), porque
floor((-5)/2) = -3. `sra` da exactamente eso.

**Pruebas:** `04_modulo` imprime `1, 2`; `04_doble_mas` imprime `13, 7`;
`04_promedio` imprime `5, -2, -3`; `04_negacion` imprime `-8, 5`; `04_mixto`
imprime `12` (sirve para ver la precedencia: `2 + 3 ⊠ 4` = `2 + (2*3+4)` = `12`).

**Limitaciones:** la precedencia entre `⊠`, `⊞` y `≈` no esta dictada por
ninguna convencion externa, asi que la elegimos nosotros en la gramatica. No es
estandar, es lo que escogimos.

*Revisado por Marcela y Mariana. Correcciones: reimplementamos `⊠` como `2a+b` y verificamos a mano el redondeo de `≈` en negativos.*

## Iteracion 5 - If/else

**Que hace ahora:** condicionales con bloque obligatorio entre llaves, con
`else` opcional. Tambien las seis comparaciones (`==`, `!=`, `<`, `>`, `<=`,
`>=`) que devuelven `1` o `0` y se pueden usar directo en el `if`.

**Gramatica:** se agregaron `if`, `else`, `{}`, y los seis comparadores.

**Listener/generador:** `visitIfStat`, `visitCompareExpr`, `visitBlock`.

**Decision auditada:** llaves obligatorias, no `then`/`endif`. Como los saltos
de linea se ignoran (van como whitespace), no podiamos delimitar bloques por
indentacion o por newline, asi que las llaves quedan como la opcion mas
explicita. Tambien decidimos que cualquier entero distinto de cero cuenta como
verdadero, porque combina con `beq ..., $zero, ...` en MIPS sin pasos extra.

**Donde se equivoco el modelo:** `<=` y `>=` los implemento como dos `slt`
seguidos de un `or`, lo cual esta MAL: `a <= b` no es lo mismo que `a < b OR b
< a`. La prueba `05_03_comparaciones` con `b >= a` daba `0` cuando debia dar
`1`. Lo reescribimos como `slt + xori 1` (la negacion logica de "estrictamente
opuesto"), que sale en dos instrucciones limpias.

**Pruebas:** `05_01_if_then` imprime `10, 99`; `05_02_if_else` imprime `22`;
`05_03_comparaciones` imprime `1, 2, 3`.

**Limitaciones:** no hay `and`/`or` booleanos. Si hace falta una condicion
compuesta hay que usar dos `if` separados.

*Revisado por Marcela y Mariana. Correcciones: reescribimos `<=` y `>=` con `slt + xori`, y agregamos comparaciones distintas a 0/1 en la prueba.*

## Iteracion 6 - While/bloques

**Que hace ahora:** ciclos `while expr block` con evaluacion al inicio. El
cuerpo puede tener cualquier statement, incluyendo otros `while` o `if`.

**Gramatica:** una sola regla nueva: `WHILE expr block`.

**Listener/generador:** `visitWhileStat` reutilizando `visitBlock`.

**Decision auditada:** dos etiquetas por ciclo: una al principio para volver a
evaluar la condicion, y otra al final para salir. Esto garantiza que si la
condicion es falsa desde el inicio, el cuerpo NO se ejecuta ni una vez. Es uno
de los casos borde que pide la rubrica.

**Donde se equivoco el modelo:** primero genero un esquema tipo `do-while`
(condicion al final del cuerpo). Lo descubrimos rapido con
`06_02_while_falso_inicio.rara`: deberia imprimir solo `7`, pero imprimia `999`
antes. Movimos la evaluacion al inicio y revisamos a mano el `.asm` para
confirmar que el `beq ..., $zero, endwhile_X` aparece ANTES de las
instrucciones del cuerpo.

**Pruebas:** `06_01_while_cuenta` imprime `3, 2, 1`; `06_02_while_falso_inicio`
imprime `7` (no entra al ciclo); `06_03_while_con_if` imprime `1, 2, 20, 3`
(ciclo con `if` adentro).

**Limitaciones:** no hay `break` ni `continue`. Para terminar un ciclo hay que
modificar la variable de la condicion.

*Revisado por Marcela y Mariana. Correcciones: cambio de do-while a while real, y prueba especifica para condicion falsa de inicio.*

## Iteracion 7 - Funciones

**Que hace ahora:** se pueden definir funciones sin parametros con `func nombre()
{ ... return expr }`, llamarlas con `nombre()` y usar el retorno dentro de
expresiones (`print x + nombre()`).

**Gramatica:** `funcDef` con `FUNC ID '(' ')' block`, `return expr`, y `ID '('
')'` como expresion (`CallExpr`).

**Listener/generador:** `visitCallExpr`, `visitReturnStat`, `_compile_function`.
El valor de retorno viaja en `$v0`.

**Decision auditada:** antes de cada `jal` guardamos `$ra` en la pila y lo
restauramos despues. Ademas, antes de cada llamada dentro de una expresion,
empujamos los registros temporales que estan vivos (`_live_registers`) para que
no se pierdan los operandos parciales.

**Donde se equivoco el modelo:** AQUI fue donde mas tuvimos que pelearle. La
primera version emitia `jal func_X` sin guardar `$ra`. En
`07_02_funcion_llama_funcion` la funcion `doble_mas_cinco` llama a `cinco()` dos
veces; al regresar de la primera llamada, `$ra` apuntaba a un lugar incorrecto y
SPIM se quedaba en loop. Lo arreglamos con el push/pop de `$ra` alrededor del
`jal`. Despues encontramos un segundo bug con `07_03_funcion_en_expresion`: la
expresion `x + siete() + cinco()` perdia el valor de `x`. El modelo no estaba
guardando los `$tN` vivos durante el `jal`. Agregamos `_live_registers` y el
push/pop correspondiente y ya quedo.

**Pruebas:** `07_01_funcion_simple` imprime `42`; `07_02_funcion_llama_funcion`
imprime `15` (`cinco() ⊠ cinco()` = `2*5 + 5`); `07_03_funcion_en_expresion`
imprime `22` (`10 + 7 + 5`).

**Limitaciones:** no hay parametros ni variables locales. Las variables siguen
siendo globales. Asumimos que cada funcion declarada va a tener al menos un
`return` alcanzable (no validamos si esta dentro de un `if`).

*Revisado por Marcela y Mariana. Correcciones: preservacion de `$ra` y de los temporales vivos.*

## Iteracion 8 - Error handling

**Que hace ahora:** el compilador detecta y reporta varios errores semanticos
en vez de generar MIPS roto o silencioso:

- division o modulo constante entre cero (en compilacion);
- funcion no definida, funcion duplicada, funcion sin `return`, `return` fuera
  de funcion;
- variable leida antes de asignar;
- bases no soportadas en literales `[d:base]`.

Cuando el divisor es una variable (no se sabe en compilacion si vale cero), el
ASM generado incluye un guard de runtime que imprime un mensaje y termina con
`syscall 10`.

**Listener/generador:** `CompileError`, `_emit_division_guard`, validaciones
distribuidas en `visitCallExpr`, `visitReturnStat`, `_parse_int_literal` y
`_ensure_variable`. En `main.py` agregamos un `ThrowingErrorListener` para
convertir errores de sintaxis en `CompileError` con linea y columna.

**Decision auditada:** detenemos la compilacion al primer error. No intentamos
recuperar para reportar varios a la vez, porque eso solo tiene sentido en
herramientas grandes y para esta entrega es preferible no producir MIPS
inconsistente.

**Donde se equivoco el modelo:** la version original reservaba en `.data`
cualquier variable mencionada en un `print`, aunque nunca se hubiera asignado.
Asi que `print x` (sin haber hecho `x <-- algo` antes) imprimia `0` sin avisar.
Cambiamos `_ensure_variable` para que sea error semantico cuando se lee una
variable que no esta en `assigned_variables`. Un cero silencioso es justo el
tipo de bug que la rubrica penaliza.

**Pruebas:** `08_01_guard_division_runtime` genera ASM y, al correrlo en SPIM,
imprime `ERROR: division entre cero` y termina. Las otras tres
(`08_02_funcion_no_definida`, `08_03_variable_no_asignada`,
`08_04_base_invalida`) NO generan `.asm`: estan hechas para que el compilador
falle. Los mensajes esperados son `Funcion no definida: fantasma`, `Variable no
asignada: x` y `Base no soportada: 3`.

**Limitaciones:** no hay recuperacion multiple. Tampoco detectamos llamadas
mutuamente recursivas porque las funciones se guardan en un dict antes de
visitarlas, asi que se permite cualquier orden de definicion.

*Revisado por Marcela y Mariana. Correcciones: reemplazamos fallos silenciosos por mensajes explicitos y agregamos el guard de runtime.*

## Explicacion del MIPS generado: `07_03_funcion_en_expresion.asm`

Este es el `.asm` mas interesante de la suite porque mezcla casi todo: una
asignacion, dos llamadas a funcion dentro de una expresion, preservacion de
`$ra` y push/pop de temporales vivos. Lo explicamos linea por linea para dejar
claro por que cada instruccion esta donde esta.

**Codigo fuente (`07_03_funcion_en_expresion.rara`):**

```
x <-- 10
print x + siete() + cinco()

func siete() { return 7 }
func cinco() { return 5 }
```

**MIPS generado (anotado):**

```mips
.data
var_x: .word 0              # reserva 4 bytes para x, inicializado en 0
.text
.globl main
main:
    li $t0, 10              # cargar el literal 10 en un temporal
    sw $t0, var_x           # guardar 10 en la direccion de x  ->  x <-- 10
    lw $t0, var_x           # leer x para empezar la expresion x + siete() + cinco()
                            # $t0 ahora vale 10 y queda VIVO durante la llamada

    # --- primera llamada: siete() ---
    addiu $sp, $sp, -4
    sw $t0, 0($sp)          # PUSH $t0 (=x=10): lo salvamos porque jal lo puede tocar
    addiu $sp, $sp, -4
    sw $ra, 0($sp)          # PUSH $ra: estamos en main, pero la convencion es siempre salvar
    jal func_siete          # llamar; al regresar $v0=7
    lw $ra, 0($sp)
    addiu $sp, $sp, 4       # POP $ra
    lw $t0, 0($sp)
    addiu $sp, $sp, 4       # POP $t0 (=10) restaurado

    move $t1, $v0           # mover el retorno (7) a un temporal nuevo, $t1
    add $t0, $t0, $t1       # $t0 = x + siete() = 10 + 7 = 17

    # --- segunda llamada: cinco() ---
    # Ahora $t0 (=17) esta vivo. $t1 ya fue liberado, asi que se reusa abajo.
    addiu $sp, $sp, -4
    sw $t0, 0($sp)          # PUSH $t0 (=17): vivo, hay que protegerlo
    addiu $sp, $sp, -4
    sw $ra, 0($sp)          # PUSH $ra otra vez
    jal func_cinco          # al regresar $v0=5
    lw $ra, 0($sp)
    addiu $sp, $sp, 4       # POP $ra
    lw $t0, 0($sp)
    addiu $sp, $sp, 4       # POP $t0 (=17)

    move $t1, $v0           # $t1 = 5
    add $t0, $t0, $t1       # $t0 = 17 + 5 = 22

    # --- print del resultado ---
    move $a0, $t0           # argumento de syscall: el entero a imprimir
    li $v0, 1               # syscall 1 = print_int
    syscall
    li $a0, 10              # caracter '\n'
    li $v0, 11              # syscall 11 = print_char
    syscall

    li $v0, 10              # syscall 10 = exit
    syscall

# ---- definicion de funciones (despues del exit de main) ----
func_siete:
    li $t0, 7
    move $v0, $t0           # convencion MIPS: el retorno va en $v0
    j return_siete_0
return_siete_0:
    jr $ra                  # regresar a la instruccion despues del jal

func_cinco:
    li $t0, 5
    move $v0, $t0
    j return_cinco_1
return_cinco_1:
    jr $ra
```

**Por que esta organizado asi:**

- **Las funciones quedan despues del `syscall 10` de main** para que la
  ejecucion natural de main termine y no caiga "por accidente" al codigo de
  las funciones.
- **Se salva `$ra` antes de cada `jal`** porque `jal` sobreescribe `$ra` con la
  direccion de retorno nueva. Si no lo salvaramos, al regresar de una funcion
  anidada perderiamos el `$ra` del caller. En este programa main no tiene un
  `$ra` que importe (no lo llamo nadie), pero el generador lo emite uniforme
  para que el mismo patron funcione cuando la llamada esta dentro de otra
  funcion (caso de `07_02`).
- **Se salvan los temporales vivos (`$t0` aqui)** porque la convencion MIPS
  marca a `$t0`-`$t9` como caller-saved: la funcion llamada los puede
  sobreescribir. `siete()` y `cinco()` aqui no los tocan, pero el generador no
  asume eso y emite el push/pop por defecto.
- **El retorno se mueve a un temporal nuevo (`$t1`)** en vez de reusar `$t0`
  para no pisar el operando izquierdo de la suma antes de tiempo. Despues de
  cada `add`, `$t1` se libera y el siguiente alloc lo reusa.
- **`var_x: .word 0`** sale en `.data` porque las variables de RaraLang son
  globales (no hay variables locales en esta iteracion).

## Nota de verificacion

Generamos el ASM de las pruebas compilables y lo corrimos con `spim` 9.1.24
desde la terminal el 2026-05-30 en macOS (Darwin 25.0.0). Las salidas
observadas coinciden con los outputs esperados de cada iteracion, incluyendo el
guard de runtime. El log completo, junto con los errores esperados de
compilacion, esta en `doc/verificacion-spim.md`.
