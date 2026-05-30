# Verificacion con SPIM

**Fecha de ejecucion:** 2026-05-30.
**Sistema:** macOS (Darwin 25.0.0).
**Simulador:** `spim` 9.1.24 instalado por Homebrew.
**Python:** 3.x con `antlr4-python3-runtime`.

## Comando para compilar todos los `.rara`

```bash
cd ejemplosANTLR/actividad3
for f in tests/*/*.rara; do
    echo "===== $f"
    python3 main.py "$f"
done
```

## Comando para ejecutar todos los `.asm` en SPIM

```bash
cd ejemplosANTLR/actividad3
for f in tests/*/*.asm; do
    echo "--- $f"
    spim -file "$f" 2>&1 | sed '/^Loaded:/d'
done
```

## Salidas observadas en SPIM

```text
--- tests/01_iteracion_1/01_01_int_literal.asm
42
0
100
--- tests/01_iteracion_1/01_02_int_grande.asm
1000
--- tests/01_iteracion_1/01_03_hex_vs_decimal.asm
255
255
--- tests/01_iteracion_1/01_04_base2.asm
10
--- tests/01_iteracion_1/01_05_string.asm
hola mundo
--- tests/01_iteracion_1/01_06_varios_print.asm
5
1000
255
10
hola mundo
--- tests/02_iteracion_2/02_asignar_e_imprimir.asm
42
--- tests/02_iteracion_2/02_dos_variables.asm
10
3
--- tests/02_iteracion_2/02_nombre_mips.asm
100
200
300
--- tests/02_iteracion_2/02_reasignacion.asm
5
99
--- tests/03_iteracion_3/03_01_aritmetica.asm
13
7
30
3
24
14
20
--- tests/03_iteracion_3/03_03_parentesis_variables.asm
35
3
8
--- tests/04_iteracion_4/04_doble_mas.asm
13
7
--- tests/04_iteracion_4/04_mixto.asm
12
--- tests/04_iteracion_4/04_modulo.asm
1
2
--- tests/04_iteracion_4/04_negacion.asm
-8
5
--- tests/04_iteracion_4/04_promedio.asm
5
-2
-3
--- tests/05_iteracion_5/05_01_if_then.asm
10
99
--- tests/05_iteracion_5/05_02_if_else.asm
22
--- tests/05_iteracion_5/05_03_comparaciones.asm
1
2
3
--- tests/06_iteracion_6/06_01_while_cuenta.asm
3
2
1
--- tests/06_iteracion_6/06_02_while_falso_inicio.asm
7
--- tests/06_iteracion_6/06_03_while_con_if.asm
1
2
20
3
--- tests/07_iteracion_7/07_01_funcion_simple.asm
42
--- tests/07_iteracion_7/07_02_funcion_llama_funcion.asm
15
--- tests/07_iteracion_7/07_03_funcion_en_expresion.asm
22
--- tests/08_iteracion_8/08_01_guard_division_runtime.asm
ERROR: division entre cero
```

## Errores de compilacion esperados (iteraciones 3 y 8)

Estos archivos NO generan `.asm` porque su proposito es validar que el compilador
detecta el error y se detiene. Salida observada en `stderr`:

```text
--- tests/03_iteracion_3/03_02_division_cero.rara
ERROR: Division entre cero en una expresion constante
--- tests/08_iteracion_8/08_02_funcion_no_definida.rara
ERROR: Funcion no definida: fantasma
--- tests/08_iteracion_8/08_03_variable_no_asignada.rara
ERROR: Variable no asignada: x
--- tests/08_iteracion_8/08_04_base_invalida.rara
ERROR: Base no soportada: 3
```

Comando usado para verificar los errores:

```bash
for f in tests/03_iteracion_3/03_02_division_cero.rara \
         tests/08_iteracion_8/08_02_funcion_no_definida.rara \
         tests/08_iteracion_8/08_03_variable_no_asignada.rara \
         tests/08_iteracion_8/08_04_base_invalida.rara; do
    echo "--- $f"
    python3 main.py "$f" 2>&1 >/dev/null
done
```
