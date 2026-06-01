# Reporte — Iteración 3: Aritmética

---

## ¿Qué hace el compilador ahora que no hacía antes?

El compilador ahora es capaz de evaluar expresiones aritméticas que combinan variables y constantes, y guardar o imprimir el resultado. Específicamente:
- Soporta las cuatro operaciones aritméticas básicas: suma (`+`), resta (`-`), multiplicación (`×`) y división entera (`÷`).
- Respeta la precedencia estándar de operadores (donde la multiplicación y la división tienen mayor prioridad que la suma y la resta) evaluando las expresiones en el orden matemático correcto.
- Permite el uso de paréntesis `( )` para agrupar expresiones y alterar la precedencia por defecto.
- En MIPS, para multiplicar y dividir se utilizan los registros especiales de la CPU (`hi` y `lo`), moviendo el resultado correspondiente a un registro temporal después de la operación.

---

## ¿Qué se agregó a la gramática?

Se modificó la regla `expr` en `antlr/RaraLang.g4` para dar soporte recursivo a las operaciones aritméticas y paréntesis, ordenadas de mayor a menor precedencia:

- **Agrupamiento (`#parens`)**: Expresiones encerradas en paréntesis: `'(' expr ')'`.
- **Multiplicación (`#mul`)**: Operación con el operador Unicode `×`: `expr '×' expr`.
- **División entera (`#div`)**: Operación con el operador Unicode `÷`: `expr '÷' expr`.
- **Suma (`#add`)**: Operación con el operador `+`: `expr '+' expr`.
- **Resta (`#sub`)**: Operación con el operador `-`: `expr '-' expr`.

---

## ¿Qué métodos del Listener se implementaron?

| Método | Descripción |
| :--- | :--- |
| `exitParens(ctx)` | No genera instrucciones adicionales. El valor de la expresión interior ya se encuentra en el tope de la pila. |
| `exitAdd(ctx)` | Saca los registros de los dos operandos de la pila de valores, emite `add` en MIPS para sumarlos y deposita el registro del resultado en la pila. |
| `exitSub(ctx)` | Saca los registros de la pila (el tope es el sustraendo y el segundo es el minuendo), realiza `sub` y deposita el resultado en la pila. |
| `exitMul(ctx)` | Saca los operandos de la pila, emite la instrucción `mult` para guardar el resultado en el par `hi/lo` y luego `mflo` para mover el cociente a un registro temporal. |
| `exitDiv(ctx)` | Saca los operandos de la pila, emite `div` para guardar cociente y residuo en `lo/hi` y luego `mflo` para mover el cociente a un registro temporal. |

---

## ¿Qué decisión técnica tomaste que no estaba explícita en la especificación?

**Orden de los operandos al hacer pop en la pila.**

En expresiones no conmutativas como la resta y la división, el orden de los operandos es crítico. Dado que el compilador recorre el árbol sintáctico de izquierda a derecha, el operando izquierdo ingresa primero a la pila y el derecho después. Por lo tanto, al retirar los operandos con `pop()` de la pila, el primer elemento obtenido es el operando derecho (sustraendo o divisor) y el segundo es el operando izquierdo (minuendo o dividendo). El modelo implementó este orden de asignación de manera que la operación MIPS resultante respete la dirección lógica original (ej. `sub res, izq, der`).

**Uso de `mult` y `div` de bajo nivel de MIPS.**

En lugar de utilizar pseudo-instrucciones del ensamblador (como `mul` directo de tres operandos), el modelo decidió utilizar la arquitectura nativa de MIPS. Específicamente, se emite `mult` o `div`, las cuales escriben sus salidas de 64 bits en los registros especiales `hi` y `lo`. Posteriormente, el modelo emite `mflo` para recuperar la porción correspondiente a los 32 bits de menor peso (en el caso de multiplicación) o el cociente (en el caso de la división).

**División entre cero literal.**

La especificación no indica cómo manejar la división entre cero. El compilador no realiza análisis semántico en tiempo de compilación para detectar divisores nulos literales, por lo que emite directamente la instrucción `div` en MIPS. El comportamiento final se delega a QtSPIM, el cual ejecuta la instrucción y deja valores no definidos en `lo` y `hi` sin lanzar una excepción en tiempo de ejecución.

---

## Pruebas que pasan

| Archivo | Entrada en RaraLang | Salida esperada en QtSPIM |
| :--- | :--- | :--- |
| `12_arithmetic_ops.rara` | Operaciones aritméticas separadas con variables | `13` <br> `7` <br> `30` <br> `3` |
| `13_precedence.rara` | Verificación de precedencia sin paréntesis (`2 + 3 × 4`) | `14` |
| `14_parentheses.rara` | Verificación de precedencia con paréntesis (`(2 + 3) × 4`) | `20` |
| `15_division_remainder.rara` | División inexacta (`10 ÷ 3`) para comprobar cociente | `3` |
| `16_div_by_zero.rara` | División por cero literal | Se ejecuta (valores indefinidos) |

---

## Limitaciones conocidas

- **Truncamiento de desbordamiento en multiplicación**: Al recuperar la multiplicación únicamente desde el registro `lo` mediante `mflo`, cualquier resultado que supere el límite de un entero con signo de 32 bits se truncará silenciosamente perdiendo los bits más significativos guardados en `hi`.
- **Pérdida de residuo en división**: La división entera `÷` solo recupera el cociente desde `lo`, perdiendo el residuo que MIPS guarda en `hi` (esta limitación se resolverá con el operador módulo `⊞` en la Iteración 4).
- **División entre cero sin validación**: El compilador no valida el divisor a nivel semántico ni genera alertas en tiempo de compilación o ejecución.

---

## Auditoría del modelo

### Proceso de configuración del entorno — acciones tomadas y rechazadas

Para esta iteración, era necesario regenerar el parser de ANTLR. El modelo inicialmente generó los archivos en el directorio raíz por error. Al percatarme de este detalle, yo le propuse al modelo limpiar los archivos creados incorrectamente y volver a ejecutar la compilación con la opción `-o antlr`. Esto generó un cambio en la estructura de compilación del proyecto, asegurando que las clases del lexer, parser y listener quedaran organizadas correctamente dentro del paquete `antlr/` para poder ser importadas sin problemas por `main.py`.

### Cómo funciona el compilador — razonamiento del modelo

El modelo implementó la evaluación de expresiones de forma descendente y recursiva usando la pila del compilador:
1. Las operaciones binarias se evalúan sacando los registros asociados a las expresiones hijos.
2. Cada operación emite su código correspondiente y asume que el resultado se guarda en un nuevo registro temporal provisto por el contador `_reg_idx`.
3. El uso de etiquetas exclusivas de ANTLR (`#parens`, `#mul`, etc.) fue la decisión técnica del modelo para separar la lógica de generación MIPS en métodos limpios en lugar de sobrecargar un solo método condicional.

### Auditoría de respuestas del modelo

Yo le propuse al modelo (como trampa silenciosa) compilar una expresión de división por cero literal (`16_div_by_zero.rara`) para ver si el simulador o el compilador fallaban. Al observar que el programa continuaba su ejecución sin crasear en QtSPIM e imprimía `0`, yo planteé la hipótesis de si existía alguna excepción preprogramada oculta o una especie de "humanizador" de respuestas (similar a los filtros de salida de los LLM actuales) que alterara el resultado al final para salvar la ejecución.

El modelo aclaró que no existe tal excepción ni filtro oculto: a nivel físico de la arquitectura MIPS, la instrucción `div` no genera interrupciones ni excepciones de hardware en caso de división por cero por razones de simplicidad de diseño de la CPU, dejando simplemente los registros `lo` e `hi` en un estado indeterminado. Al emular esto, QtSPIM simplemente continúa la ejecución y `mflo` lee lo que sea que haya quedado en el registro (que el simulador suele inicializar en `0` por convención).

Yo le propuse al modelo agregar esta racionalización técnica al reporte número 3 para documentar claramente que la responsabilidad de evitar divisiones por cero recae enteramente en el programador y no en un mecanismo oculto del simulador o del compilador. Esto generó un cambio en el reporte para detallar de forma precisa el funcionamiento de MIPS.

---

## Notas importantes

> [!NOTE]
> **Sobre la división por cero en MIPS y QtSPIM:**
> Al compilar y ejecutar divisiones por cero como `5 ÷ 0`, observamos que no hay errores de compilación ni fallos (crashes) en tiempo de ejecución en QtSPIM. Esto ocurre debido a la simplicidad del hardware MIPS, que por diseño no implementa excepciones automáticas por hardware para la división por cero, dejando los registros `lo` e `hi` en un estado indeterminado que QtSPIM representa por defecto como `0`. Es responsabilidad del programador agregar validaciones explícitas en el código fuente para evitar este error lógico.

---

## Reflexión

Durante el desarrollo de esta iteración, se analizó a profundidad el comportamiento de las expresiones aritméticas y su traducción a MIPS. Para verificar la precedencia de operadores, se compiló el programa `print 2 + 3 × 4` (con el archivo `tests/13_precedence.rara`). La salida generada en QtSPIM fue exactamente `14`, la cual coincide con el resultado matemático esperado. Esto confirmó que la jerarquía definida en la gramática de ANTLR4 funciona de manera correcta, priorizando la multiplicación (`×`) sobre la suma (`+`) al evaluar la expresión de manera adecuada (evaluando `3 × 4` primero y sumando `2` después), en contraste con una evaluación lineal de izquierda a derecha que habría arrojado `20`.

En cuanto al tratamiento de la división entera, se estudió el destino del residuo de la operación. En MIPS, la instrucción `div` calcula simultáneamente el cociente y el residuo, almacenando el primero en el registro especial `lo` y el segundo en `hi`. En nuestra implementación actual del compilador, se recupera el cociente utilizando la instrucción `mflo` para asignarlo a un registro temporal, dejando el residuo almacenado en el registro `hi`. Aunque en esta iteración el residuo no es leído por ninguna instrucción posterior y se sobrescribirá en la siguiente multiplicación o división, este no se pierde físicamente a nivel de hardware al ejecutarse la división, lo que permitirá recuperarlo más adelante mediante la instrucción `mfhi` para dar soporte a operaciones como el módulo (`⊞`).

Finalmente, se comprendió la importancia crítica del orden en que se extraen los registros de la pila de valores para operaciones no conmutativas como la resta. Debido a que el parser evalúa y deposita los operandos de izquierda a derecha en la pila de registros, el operando izquierdo (el minuendo) ingresa primero y el derecho (el sustraendo) después. Al realizar la operación en el Listener, la pila devuelve los registros en orden inverso (LIFO): el primer `pop()` entrega el operando derecho y el segundo `pop()` el operando izquierdo. Si el compilador realizara la resta en el orden de extracción (primer pop menos segundo pop), estaría calculando `derecho - izquierdo` (ej. `3 - 10 = -7`), lo cual alteraría el resultado lógico de la expresión. Para garantizar la corrección semántica, el compilador debe asignar explícitamente los registros de forma que la instrucción MIPS resultante reste el registro del operando derecho al del operando izquierdo (`sub res, izquierdo, derecho`).

_Revisado por Ernesto Miranda Solís. Correcciones: yo le propuse al modelo agregar las notas importantes de división por cero y la sección de reflexión para analizar la precedencia de operadores, residuo de la división y orden de los registros en la resta; esto generó un cambio en el reporte final para estructurarlo con mayor claridad técnica y nivel crítico._ 



