from __future__ import annotations

"""
Este archivo permite ejecutar el proyecto desde la consola.
Sirve para probar rapidamente las tres salidas principales:
analisis lexico, escaneo por etiquetas y analisis sintactico.
"""

import sys

from .lexer_l import analizar_archivo_lexico
from .parser_s import analizar_archivo_sintactico
from .scanner_l import escanear_archivo


def main(argv: list[str] | None = None) -> int:
    """Recibe un comando de consola y ejecuta la fase correspondiente."""
    args = list(sys.argv[1:] if argv is None else argv)

    if len(args) < 2 or args[0] not in {"lex", "scan", "parse"}:
        print("Uso: python -m traductor_base <lex|scan|parse> <archivo.tb>")
        return 1

    comando, ruta = args[0], args[1]

    if comando == "lex":
        for token in analizar_archivo_lexico(ruta):
            print(
                f"{token.tipo.name:<15} {token.lexema!r:<20} "
                f"linea={token.linea} columna={token.columna}"
            )
        return 0

    if comando == "scan":
        tokens, errores = escanear_archivo(ruta)
        for token in tokens:
            print(token)
        if errores:
            print("Errores:")
            for error in errores:
                print(error)
            return 1
        return 0

    if comando == "parse":
        print(analizar_archivo_sintactico(ruta))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
