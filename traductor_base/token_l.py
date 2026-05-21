from __future__ import annotations

"""
Este archivo define el registro de token usado por el escaner academico.
Sirve para guardar el lexema, su etiqueta y la posicion donde fue hallado.
"""

from dataclasses import dataclass


@dataclass
class RegistroToken:
    lexema: str
    etiqueta: str
    linea: int
    indice: int

    def posicion(self) -> str:
        return f"({self.linea}, {self.indice})"

    def __str__(self) -> str:
        return f"({self.lexema}, {self.etiqueta}, {self.linea}, {self.indice})"
