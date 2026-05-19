---
iteracion: 3
tema: Aritmética básica
tiempo_estimado: 45 min
---

# Iteración 3 — Aritmética

## Meta

Tu compilador puede evaluar expresiones aritméticas y guardar o imprimir el resultado.
Esto debe funcionar:

```
x <-- 10
y <-- 3
print x + y
print x - y
print x × y
print x ÷ y
print (x + 2) × (y - 1)
```

## Lo que se añade a la gramática

- **Suma** con el operador `+`
- **Resta** con el operador `-`
- **Multiplicación** con el carácter `×` (no es `*`, es el símbolo tipográfico)
- **División entera** con el carácter `÷` (no es `/`)
- **Paréntesis** para agrupar expresiones y controlar el orden de evaluación

El orden en que aparecen los operadores en la gramática determina su precedencia.
La gramática puede hacer que `×` tenga más prioridad que `+`, o puede no hacerlo —
eso depende de cómo la escribas. Vale la pena que lo discutas con el modelo.

## Pruebas de aceptación

Genera tus propios programas y córrelos en QtSPIM. Calcula el resultado esperado a mano antes de correr.
Tu suite debe cubrir:

- Las cuatro operaciones con valores conocidos (verifica cada una por separado)
- Una expresión que mezcle suma y multiplicación: ¿tu compilador respeta la precedencia?
  Prueba `print 2 + 3 × 4` — el resultado correcto es 14, no 20
- Expresión con paréntesis que cambie el orden: `print (2 + 3) × 4` debe dar 20
- División donde el resultado no es exacto (ej. `10 ÷ 3`) — ¿qué pasa con el residuo?

**Trampa silenciosa** — pídele al LLM que genere un programa que divida entre cero literal.

## Prompt de ejemplo para el LLM

---

> Tengo un compilador RaraLang → MIPS. Ya funciona print con literales y variables.
> Ahora necesito operaciones aritméticas entre expresiones.
>
> En MIPS, para sumar o restar dos valores que están en registros, existe una instrucción
> directa. Para multiplicar, el resultado puede ser un número grande, así que se guarda
> en registros especiales — hay que moverlo a un registro normal después. Para dividir,
> ocurre algo similar: cociente y residuo quedan en lugares distintos, y hay que elegir
> cuál mover.
>
> El compilador usa una pila de registros temporales. Cuando evalúa `a + b`, primero
> evalúa `a` (deja un registro con el valor), luego evalúa `b` (deja otro), y cuando
> llega al `+` toma los dos del tope de la pila y produce un tercero con el resultado.
> El orden importa: el último en entrar a la pila es el operando derecho.
>
> Los operadores en RaraLang son `+`, `-`, `×` y `÷` (caracteres Unicode).
> La gramática debe expresar que `×` y `÷` tienen mayor precedencia que `+` y `-`.
>

---

## Reflexión (llenar después de terminar esta iteración)

Para esta iteración se usó Codex con el modelo GPT-5.5 en su configuración default.

**¿Qué resultado da `2 + 3 × 4` en tu compilador? ¿Es el que esperabas? ¿Cómo lo verificaste?**

> Da `14`, que sí era lo esperado. El compilador entiende que la multiplicación
> tiene más prioridad que la suma, entonces primero hace `3 × 4`, que da `12`,
> y después suma el `2`. Lo verifiqué con un programa de prueba que incluía
> `print 2 + 3 × 4` y revisando que el código generado siguiera ese orden.

**En la división entera, ¿qué pasa con el residuo? ¿Dónde queda? ¿Se pierde?**

> En una división como `10 ÷ 3`, el compilador se queda con la parte entera, o
> sea `3`. El residuo sería `1`, pero no se imprime ni se guarda como resultado
> principal. En MIPS ese residuo queda en un lugar especial, pero como RaraLang
> está usando división entera, el compilador solo toma el cociente.

**Explica con tus palabras por qué el orden en que se sacan los registros de la pila importa para la resta.**

> Importa porque restar no es igual en ambos sentidos. No es lo mismo `10 - 3`
> que `3 - 10`. Cuando el compilador evalúa una expresión, va guardando los
> valores temporalmente en una pila. El último valor que entra es el primero que
> sale, entonces hay que tener cuidado para no invertir los operandos. Si la
> expresión dice `x - y`, el compilador debe respetar ese orden.
