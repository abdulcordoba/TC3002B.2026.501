
---
iteracion: 2
tema: Variables enteras y asignación
tiempo_estimado: 30 min
---

# Iteración 2 — Variables

## Meta

Tu compilador puede ahora guardar valores en variables con nombre y recuperarlos.
Un programa como este debe funcionar:

```
x <-- 10
y <-- 3
print x
print y
```

## Lo que se añade a la gramática

- **Nombres de variable**: una secuencia de letras, números y guiones bajos que empieza
  con letra. Por ejemplo: `x`, `contador`, `valor_final`.
- **Sentencia de asignación**: la forma `nombre <-- expresión` guarda un valor en la variable.
  El operador es `<--` (dos guiones, no uno).
- **Variable como expresión**: escribir el nombre de una variable donde va una expresión
  significa "leer el valor de esa variable".

## Pruebas de aceptación

Genera tus propios programas de prueba y córrelos en QtSPIM.
Tu suite debe cubrir:

- Asignar un valor a una variable e imprimirla
- Asignar dos variables distintas, imprimir ambas en orden
- Reasignar una variable y verificar que `print` muestra el nuevo valor
- Una variable cuyo nombre sea una instrucción de MIPS (ej: `add`, `sub`, `div`) — este caso suele romper compiladores ingenuos; verifica que el tuyo lo maneja

**Trampa silenciosa** — pídele al LLM que genere un programa que lea una variable
sin haberla asignado. ¿Qué hace tu compilador? ¿Debería ser un error?

## Prompt de ejemplo para el LLM

---

> Mi compilador ya genera código para `print` con literales. Ahora necesito variables.
>
> En MIPS, las variables enteras se guardan en la sección `.data` como palabras de 32 bits.
> Cuando se asigna un valor a una variable, hay que almacenarlo en esa dirección de memoria.
> Cuando se lee una variable, hay que cargarla desde esa dirección a un registro.
>
> Necesito que el compilador haga esto automáticamente la primera vez que ve cada variable:
> reservar espacio en `.data` con un valor inicial de 0.

---

## Reflexión (llenar después de terminar esta iteración)

**¿Cómo decidió el modelo reservar espacio para la variable? ¿Dónde queda en el archivo `.asm`?**

> El compilador crea una etiqueta `var_nombre` en la sección `.data` con `.word 0` cuando ve una variable por primera vez en una asignación. Queda al inicio del archivo `.asm`, antes de la sección `.text`. Por ejemplo, `x <-- 10` genera `var_x: .word 0` en `.data`.

**Prueba b <-- 5 ¿Qué se genera, qué hace QtSpim?**

> Genera en `.data`: `var_b: .word 0`, y en `.text`: `li $t0, 5` (cargar 5 en temporal), seguido de `sw $t0, var_b` (store word en la dirección). QtSPIM reserva 4 bytes en memoria para `var_b` y guarda el valor 5 ahí.

**¿Qué pasa si asignas una variable dos veces?**

> El compilador no reserva un nuevo espacio. Solo genera dos instrucciones `sw` a la misma etiqueta. El primer `sw` guarda el valor inicial, el segundo sobrescribe la memoria. La variable sigue usando la misma etiqueta `var_nombre`.

---

**Herramientas utilizadas:**
- Claude Code (IDE CLI de Anthropic)
- Modelo: Claude Haiku 4.5 (claude-haiku-4-5-20251001)

> Auditoria, correcciones aplicadas y firma consolidada de esta iteracion: ver
> `doc/reporte-iteraciones.md` (seccion "Iteracion 2 - Variables").
