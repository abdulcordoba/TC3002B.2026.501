# RaraLang Compiler

**Integrantes**

- Marcela Hernandez Ramirez - A01658023
- Mariana Fernandez De la Torre - A01657317

## De que va esto

RaraLang es el lenguaje "raro" que armamos para la clase de compiladores. Tiene
sintaxis sencilla pero con operadores Unicode poco comunes (`×`, `÷`, `⊞`, `⊠`,
`≈`, `±`) y literales en bases no convencionales del estilo `[FF:16]`. La
gracia de la rareza es que el modelo de IA no tiene ejemplos previos del
lenguaje, asi que tiene que razonar desde la guia y a veces se equivoca, que
es justo lo que queriamos auditar.

Este compilador toma archivos `.rara`, los pasa por un parser de ANTLR4 y
genera codigo MIPS (`.asm`) que se puede correr en SPIM o QtSPIM.

**Modelo que usamos:** Codex con GPT-5.5 en su configuracion default. En el
reporte de iteraciones documentamos donde nos sirvio y donde tuvimos que
corregirle a mano.

## Donde esta lo importante

El entregable principal vive en `ejemplosANTLR/actividad3/`. Los archivos
relevantes son:

- `RaraLang.g4` - la gramatica del lenguaje.
- `MIPSListener.py` - el compilador (genera el MIPS).
- `main.py` - el comando para compilar un `.rara` y dejar el `.asm` al lado.
- `tests/` - una carpeta por iteracion con los archivos de prueba.
- `doc/reporte-iteraciones.md` - el reporte con auditoria y reflexion.
- `doc/verificacion-spim.md` - el log de las corridas en SPIM.

## Iteraciones que terminamos

| # | Tema                                            | Tests                              | Guia                            |
|---|-------------------------------------------------|------------------------------------|---------------------------------|
| 1 | Literales, bases raras, strings, `print`        | `tests/01_iteracion_1/` (6 `.rara`) | `doc/it1-literales-print.md`    |
| 2 | Variables y asignacion con `<--`                | `tests/02_iteracion_2/` (4 `.rara`) | `doc/it2-variables.md`          |
| 3 | Aritmetica `+`, `-`, `×`, `÷` y parentesis      | `tests/03_iteracion_3/` (3 `.rara`) | `doc/it3-aritmetica.md`         |
| 4 | Operadores Unicode `⊞`, `⊠`, `≈`, `±`            | `tests/04_iteracion_4/` (5 `.rara`) | `doc/it4-unicode-ops.md`        |
| 5 | Condicionales `if/else` y comparaciones         | `tests/05_iteracion_5/` (3 `.rara`) | `doc/it5-if-else.md`            |
| 6 | Ciclos `while` y bloques                        | `tests/06_iteracion_6/` (3 `.rara`) | `doc/it6-while-bloques.md`      |
| 7 | Funciones sin parametros y `return`             | `tests/07_iteracion_7/` (3 `.rara`) | `doc/it7-funciones.md`          |
| 8 | Manejo de errores                               | `tests/08_iteracion_8/` (4 `.rara`) | `doc/it8-error-handling.md`     |

Todas las iteraciones quedaron compilando y todas las pruebas que deben pasar
corren en SPIM con el resultado esperado.

## Como correrlo

Necesitas:

- Python 3.10+
- `antlr4-python3-runtime` (esta en `ejemplosANTLR/actividad3/requirements.txt`)
- `spim` o `QtSPIM` para ejecutar el MIPS

```bash
pip install -r ejemplosANTLR/actividad3/requirements.txt
```

Para compilar un archivo:

```bash
cd ejemplosANTLR/actividad3
python3 main.py tests/01_iteracion_1/01_01_int_literal.rara
```

Eso te deja el `.asm` al lado del `.rara` y tambien te imprime el MIPS en la
terminal.

Para compilar TODA la suite de un jalon:

```bash
cd ejemplosANTLR/actividad3
for f in tests/*/*.rara; do
    echo "===== $f"
    python3 main.py "$f"
done
```

## Como correr el MIPS

Uno por uno:

```bash
spim -file tests/01_iteracion_1/01_01_int_literal.asm
```

O la suite completa con el mismo formato que aparece en `doc/verificacion-spim.md`:

```bash
cd ejemplosANTLR/actividad3
for f in tests/*/*.asm; do
    echo "--- $f"
    spim -file "$f" 2>&1 | sed '/^Loaded:/d'
done
```

Cualquier `.asm` tambien se puede abrir directo en QtSPIM si prefieres la
interfaz grafica.

## Sobre las pruebas

Cada carpeta dentro de `tests/` es una iteracion. Hay minimo 3 archivos `.rara`
por iteracion y al menos un `.asm` generado.

**Ojo:** algunas pruebas estan hechas para FALLAR a proposito. Son cuatro
casos trampa que verifican que el compilador detecta errores:

- `tests/03_iteracion_3/03_02_division_cero.rara` - division entre cero
  constante.
- `tests/08_iteracion_8/08_02_funcion_no_definida.rara` - llama a una funcion
  que no existe.
- `tests/08_iteracion_8/08_03_variable_no_asignada.rara` - lee una variable
  antes de asignarla.
- `tests/08_iteracion_8/08_04_base_invalida.rara` - usa base 3 (no soportada).

Estos casos no producen `.asm`. La salida esperada del compilador para cada
uno esta en `doc/verificacion-spim.md`.

## Verificacion

Corrimos la suite con `spim` 9.1.24 el 2026-05-30 en macOS (Darwin 25.0.0).
Todas las salidas coinciden con lo que documentamos en:

```text
ejemplosANTLR/actividad3/doc/verificacion-spim.md
```
