from __future__ import annotations

"""
Este archivo representa el codigo fuente como objeto.
Sirve para recuperar lineas concretas del texto y apoyar al escaner
cuando necesita ubicar errores o mostrar contexto.
"""


class CodigoFuente:
    def __init__(self, texto: str) -> None:
        self.texto = texto
        self.lineas = texto.splitlines() or [""]

    @classmethod
    def desde_archivo(cls, ruta_archivo: str) -> "CodigoFuente":
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            return cls(archivo.read())

    def obtener_linea(self, numero_linea: int) -> str:
        if 1 <= numero_linea <= len(self.lineas):
            return self.lineas[numero_linea - 1]
        return ""
