from __future__ import annotations

"""
Este archivo implementa un escaner academico por etiquetas.
Su funcion es recorrer el texto y devolver lexemas con etiquetas del
lenguaje infantil para apoyar la exposicion teorica.
"""

import re

from .definitions_l import (
    CodigoFuente,
    EtiquetasInfantiles,
    LexemasInfantiles,
    RegistroToken,
    lexema_a_etiqueta,
)


class Escaner:
    """Recorre el codigo fuente y genera registros etiquetados."""

    def __init__(self, codigo_fuente: CodigoFuente):
        self.codigo = codigo_fuente.texto
        self.codigo_fuente = codigo_fuente
        self.numero_linea = 1
        self.caracter_actual = ""
        self.indice = 0
        self.tokens: list[RegistroToken] = []
        self.errores: list[dict[str, str | int]] = []

    def __obtener_siguiente_caracter(self):
        if self.indice < len(self.codigo):
            self.caracter_actual = self.codigo[self.indice]
            self.indice += 1
            return self.caracter_actual
        self.caracter_actual = None
        return None

    def __obtener_contenido_linea_actual(self):
        return self.codigo_fuente.obtener_linea(self.numero_linea)

    def __omitir_comentario_de_linea(self):
        while self.__obtener_siguiente_caracter() is not None and self.caracter_actual != "\n":
            continue
        if self.caracter_actual == "\n":
            self.tokens.append(
                RegistroToken(
                    "\n",
                    EtiquetasInfantiles.SALTO_LINEA,
                    self.numero_linea,
                    self.indice - 1,
                )
            )
            self.numero_linea += 1

    def __leer_cadena(self):
        indice_inicio = self.indice - 1
        lexema = ""
        while (
            self.__obtener_siguiente_caracter()
            and self.caracter_actual != '"'
            and self.caracter_actual != "\n"
        ):
            lexema += self.caracter_actual
        if self.caracter_actual != '"':
            self.errores.append(
                {
                    "mensaje": "El texto no se cerro.",
                    "linea": self.numero_linea,
                    "contenido": self.__obtener_contenido_linea_actual(),
                }
            )
            return None
        return RegistroToken(lexema, EtiquetasInfantiles.CADENA, self.numero_linea, indice_inicio)

    def __leer_numero(self):
        indice_inicio = self.indice - 1
        lexema = self.caracter_actual
        cantidad_puntos = 0
        while self.__obtener_siguiente_caracter() and (
            self.caracter_actual.isdigit() or self.caracter_actual == "."
        ):
            if self.caracter_actual == ".":
                cantidad_puntos += 1
                if cantidad_puntos > 1:
                    self.errores.append(
                        {
                            "mensaje": "El numero decimal tiene demasiados puntos.",
                            "linea": self.numero_linea,
                            "contenido": self.__obtener_contenido_linea_actual(),
                        }
                    )
                    return None
            lexema += self.caracter_actual
        if self.caracter_actual and not self.caracter_actual.isspace() and self.caracter_actual not in "+-*/":
            while self.caracter_actual and re.match(r"[A-Za-z_]", self.caracter_actual):
                lexema += self.caracter_actual
                self.__obtener_siguiente_caracter()
            self.errores.append(
                {
                    "mensaje": "Un numero no puede seguir pegado a una palabra.",
                    "linea": self.numero_linea,
                    "contenido": self.__obtener_contenido_linea_actual(),
                }
            )
            return None
        if self.caracter_actual:
            self.indice -= 1
        return RegistroToken(lexema, EtiquetasInfantiles.NUMERO, self.numero_linea, indice_inicio)

    def __leer_palabra(self):
        indice_inicio = self.indice - 1
        lexema = self.caracter_actual
        while self.__obtener_siguiente_caracter() and (
            self.caracter_actual.isalnum() or self.caracter_actual == "_"
        ):
            lexema += self.caracter_actual
        if self.caracter_actual:
            self.indice -= 1
        etiqueta = lexema_a_etiqueta.get(lexema, EtiquetasInfantiles.ID)
        return RegistroToken(lexema, etiqueta, self.numero_linea, indice_inicio)

    def __leer_simbolo(self):
        indice_inicio = self.indice - 1
        lexema = self.caracter_actual
        if lexema in lexema_a_etiqueta:
            return RegistroToken(lexema, lexema_a_etiqueta[lexema], self.numero_linea, indice_inicio)
        self.errores.append(
            {
                "mensaje": "Caracter no reconocido.",
                "linea": self.numero_linea,
                "contenido": self.__obtener_contenido_linea_actual(),
            }
        )
        return None

    def tokenizar(self) -> list[RegistroToken]:
        while self.__obtener_siguiente_caracter() is not None:
            if self.caracter_actual in " \t\r":
                continue
            if self.caracter_actual == "\n":
                self.tokens.append(
                    RegistroToken(
                        "\n",
                        EtiquetasInfantiles.SALTO_LINEA,
                        self.numero_linea,
                        self.indice - 1,
                    )
                )
                self.numero_linea += 1
                continue
            if self.caracter_actual == "#":
                self.__omitir_comentario_de_linea()
                continue
            if self.caracter_actual == '"':
                token = self.__leer_cadena()
                if token:
                    self.tokens.append(token)
                continue
            if self.caracter_actual.isdigit():
                token = self.__leer_numero()
                if token:
                    self.tokens.append(token)
                continue
            if self.caracter_actual.isalpha() or self.caracter_actual == "_":
                token = self.__leer_palabra()
                if token:
                    self.tokens.append(token)
                continue
            if self.caracter_actual in {
                LexemasInfantiles.MAS,
                LexemasInfantiles.MENOS,
                LexemasInfantiles.MULTIPLICA,
                LexemasInfantiles.DIVIDE,
            }:
                token = self.__leer_simbolo()
                if token:
                    self.tokens.append(token)
                continue
            self.errores.append(
                {
                    "mensaje": "Caracter no reconocido.",
                    "linea": self.numero_linea,
                    "contenido": self.__obtener_contenido_linea_actual(),
                }
            )
        return self.tokens


def escanear_archivo(ruta_archivo: str) -> tuple[list[RegistroToken], list[dict[str, str | int]]]:
    """Abre un archivo y devuelve sus tokens etiquetados junto a errores."""
    codigo_fuente = CodigoFuente.desde_archivo(ruta_archivo)
    escaner = Escaner(codigo_fuente)
    tokens = escaner.tokenizar()
    return tokens, escaner.errores
