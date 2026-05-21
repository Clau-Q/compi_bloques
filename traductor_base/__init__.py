"""
Este archivo expone las funciones principales del modulo.
Sirve para importar de forma simple el analisis lexico, el escaneo y el
analisis sintactico desde otros archivos o desde pruebas.
"""

from .lexer_l import analizar_archivo_lexico, analizar_lexicamente
from .parser_s import analizar_archivo_sintactico, analizar_sintaxis
from .scanner_l import escanear_archivo

__all__ = [
    "analizar_lexicamente",
    "analizar_archivo_lexico",
    "analizar_sintaxis",
    "analizar_archivo_sintactico",
    "escanear_archivo",
]
