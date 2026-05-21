# Bloques Espanol Fase 1

Fase 1 del proyecto enfocada solo en:

- analisis lexico
- analisis sintactico
- gramatica
- lexemas, tokens e identificadores

Esta version ya usa el vocabulario infantil acordado para el proyecto:

- `crear_cajita`
- `guardar`
- `mostrar`
- `preguntar`
- `si_pasa`
- `si_no_pasa`
- `repetir`
- `fin`

## Sufijos usados

- `_l`: archivo orientado a la fase lexico
- `_s`: archivo orientado a la fase sintactica
- `_ls`: archivo compartido entre ambas fases

## Archivos que debes presentar

- `lexemas_l.md`: tabla de palabras reservadas y patrones del lenguaje infantil
- `gramatica_s.ebnf`: gramatica formal del lenguaje infantil
- `traductor_base/definitions_l.py`: definiciones de lexemas, etiquetas, tipos de token e identificadores
- `traductor_base/lexer_l.py`: analizador lexico
- `traductor_base/scanner_l.py`: escaner academico por etiquetas
- `traductor_base/parser_s.py`: analizador sintactico
- `traductor_base/ast_nodes_s.py`: estructura del arbol sintactico
- `traductor_base/errors_ls.py`: errores compartidos
- `examples/programa.tb`: programa de ejemplo

## Nombres internos

En esta fase el codigo usa nombres alineados al lenguaje infantil, por ejemplo:

- `CrearCajita`
- `Guardar`
- `Mostrar`
- `Preguntar`
- `Repetir`
- `SiPasa`
- `AnalizadorSintactico`
- `Escaner`
- `CodigoFuente`
- `ErrorLexico`
- `ErrorSintactico`

## Donde esta el identificador

El identificador del lenguaje esta definido principalmente en:

- `lexemas_l.md`
- `traductor_base/lexer_l.py`
- `traductor_base/definitions_l.py`

Patron base:

```text
[A-Za-z_][A-Za-z0-9_]*
```

## Comandos de prueba

Ubicate en:

```powershell
cd C:\Users\Asus\Documents\Playground\bloques-espanol-fase1
```

### Ver tokens del analizador lexico

```powershell
python -m traductor_base lex .\examples\programa.tb
```

### Ver lexemas y etiquetas del scanner

```powershell
python -m traductor_base scan .\examples\programa.tb
```

### Ver estructura sintactica

```powershell
python -m traductor_base parse .\examples\programa.tb
```

## Que debes presentar ahora

1. Tabla de lexemas y tokens.
2. Regla del identificador.
3. Gramatica del lenguaje.
4. Salida del analizador lexico.
5. Salida del scanner por etiquetas.
6. Salida del analizador sintactico.

La semantica, Python, frontend y backend quedaron fuera de esta fase.
