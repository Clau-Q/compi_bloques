"""
Este archivo define los errores compartidos entre las fases lexico y sintactico.
Sirve para reportar fallos de forma clara cuando el analizador encuentra
simbolos invalidos o estructuras mal formadas.
"""

class ErrorTraductor(Exception):
    """Error base del traductor."""


class ErrorLexico(ErrorTraductor):
    """Error de analisis lexico."""


class ErrorSintactico(ErrorTraductor):
    """Error de analisis sintactico."""
