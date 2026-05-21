# Lexemas del Traductor Infantil

Este archivo resume los lexemas del lenguaje infantil.
Sirve para mostrar, en la fase lexico, que palabras cercanas al niño
reconoce el analizador.

## Palabras reservadas

| Token | Lexema |
|---|---|
| `CREAR_CAJITA` | `crear_cajita` |
| `GUARDAR` | `guardar` |
| `COMO` | `como` |
| `CON` | `con` |
| `MOSTRAR` | `mostrar` |
| `PREGUNTAR` | `preguntar` |
| `GUARDAR_EN` | `guardar_en` |
| `SI_PASA` | `si_pasa` |
| `SI_NO_PASA` | `si_no_pasa` |
| `ENTONCES` | `entonces` |
| `REPETIR` | `repetir` |
| `VECES` | `veces` |
| `FIN` | `fin` |
| `TIPO_NUMERO` | `numero` |
| `TIPO_DECIMAL` | `decimal` |
| `TIPO_TEXTO` | `texto` |
| `TIPO_SI_NO` | `si_no` |
| `VERDADERO` | `verdadero` |
| `FALSO` | `falso` |
| `MAYOR_QUE` | `mayor_que` |
| `MENOR_QUE` | `menor_que` |
| `IGUAL_A` | `igual_a` |
| `DIFERENTE_DE` | `diferente_de` |
| `MAYOR_O_IGUAL` | `mayor_o_igual` |
| `MENOR_O_IGUAL` | `menor_o_igual` |
| `Y` | `y` |
| `O` | `o` |
| `NO` | `no` |

## Operadores aritmeticos

| Token | Lexema |
|---|---|
| `SUMA` | `+` |
| `RESTA` | `-` |
| `MULT` | `*` |
| `DIV` | `/` |

## Patrones

| Token | Patron |
|---|---|
| `ID` | `[A-Za-z_][A-Za-z0-9_]*` |
| `NUMERO` | `[0-9]+(\.[0-9]+)?` |
| `CADENA` | `"[^"]*"` |
| `SALTO_LINEA` | `\n+` |

## Nota

- El lexer agrega ademas el token `FIN_ARCHIVO` al final de la entrada.
- En este lenguaje infantil, `fin` reemplaza cierres tecnicos como `}`.
