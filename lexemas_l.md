# Lexemas del Traductor

Este archivo resume los lexemas del lenguaje.
Sirve para mostrar, en la fase lexico, que palabras reservadas, operadores,
delimitadores y patrones reconoce el analizador.

## Palabras reservadas

| Token | Lexema |
|---|---|
| `DECLARAR` | `declarar` |
| `MOSTRAR` | `mostrar` |
| `SI` | `si` |
| `ENTONCES` | `entonces` |
| `SINO` | `sino` |
| `REPETIR` | `repetir` |
| `VECES` | `veces` |
| `VERDADERO` | `verdadero` |
| `FALSO` | `falso` |

## Operadores

| Token | Lexema |
|---|---|
| `ASIGNAR` | `=` |
| `SUMA` | `+` |
| `RESTA` | `-` |
| `MULT` | `*` |
| `DIV` | `/` |
| `MAYOR` | `>` |
| `MENOR` | `<` |
| `MAYOR_IGUAL` | `>=` |
| `MENOR_IGUAL` | `<=` |
| `IGUAL_IGUAL` | `==` |
| `DIFERENTE` | `!=` |

## Delimitadores

| Token | Lexema |
|---|---|
| `LLAVE_IZQ` | `{` |
| `LLAVE_DER` | `}` |
| `PAREN_IZQ` | `(` |
| `PAREN_DER` | `)` |

## Patrones

| Token | Patron |
|---|---|
| `ID` | `[A-Za-z_][A-Za-z0-9_]*` |
| `NUMERO` | `[0-9]+(\.[0-9]+)?` |
| `CADENA` | `"[^"]*"` |
| `SALTO_LINEA` | `\n+` |

## Nota

- El lexer agrega ademas el token `FIN_ARCHIVO` al final de la entrada.
