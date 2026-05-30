nmms# RaraLang Compiler

**Integrantes**

- Marcela Hernandez Ramirez - A01658023
- Mariana Fernandez De la Torre - A01657317

## Descripcion

Este proyecto es un compilador para **RaraLang**, un lenguaje inventado para la clase
de compiladores. El objetivo fue construir el compilador por iteraciones usando un
agente de IA como apoyo, pero auditando el codigo generado y verificando que el MIPS
funcionara correctamente.

RaraLang tiene una sintaxis sencilla, pero usa operadores Unicode no comunes como
`×`, `÷`, `⊞`, `⊠`, `≈` y `±`. Esto nos obligo a revisar bien la gramatica, la
precedencia de operadores y el codigo MIPS generado.

## Estructura principal

El entregable principal esta en:

```text
ejemplosANTLR/actividad3/
```

Archivos importantes:

- `RaraLang.g4`: gramatica del lenguaje.
- `MIPSListener.py`: compilador/generador de codigo MIPS.
- `main.py`: programa para compilar archivos `.rara` a `.asm`.
- `tests/`: pruebas por iteracion.
- `doc/reporte-iteraciones.md`: reporte con auditoria y reflexion por iteracion.
- `doc/verificacion-spim.md`: evidencia de ejecucion de los `.asm` con SPIM.

## Iteraciones completadas

Se completaron las siguientes iteraciones:

1. Literales, numeros en otras bases, strings y `print`.
2. Variables y asignacion con `<--`.
3. Aritmetica basica con `+`, `-`, `×`, `÷` y parentesis.
4. Operadores Unicode `⊞`, `⊠`, `≈` y `±`.
5. Condicionales `if/else` y comparaciones.
6. Ciclos `while` y bloques.
7. Funciones sin parametros y `return`.
8. Manejo de errores.

## Como correr el compilador

Desde la carpeta del proyecto:

```bash
cd ejemplosANTLR/actividad3
python3 main.py tests/01_iteracion_1/01_01_int_literal.rara
```

Esto genera un archivo `.asm` junto al `.rara` y tambien imprime el MIPS en la
terminal.

## Como correr el MIPS

Se uso `spim` para verificar los archivos `.asm`:

```bash
spim -file tests/01_iteracion_1/01_01_int_literal.asm
```

Tambien se puede correr con QtSPIM abriendo el archivo `.asm` generado.

## Pruebas

Cada carpeta dentro de `tests/` corresponde a una iteracion. Hay al menos tres
archivos `.rara` por iteracion completada, y archivos `.asm` generados para las
pruebas que compilan correctamente.

Ejemplo:

```text
tests/03_iteracion_3/
tests/04_iteracion_4/
tests/05_iteracion_5/
```

Algunas pruebas de la iteracion 8 estan hechas para fallar a proposito, porque
verifican que el compilador detecte errores como variables no asignadas, funciones
no definidas o bases invalidas.

## Verificacion

Se ejecuto la suite de archivos `.asm` con `spim` 9.1.24. Las salidas observadas
coinciden con los resultados esperados documentados en:

```text
ejemplosANTLR/actividad3/doc/verificacion-spim.md
```
