from __future__ import annotations

"""
Este archivo define los tipos de token de la fase lexico.
Sirve para clasificar cada palabra, numero, operador o delimitador que
reconoce el analizador.
"""

from dataclasses import dataclass
from enum import Enum, auto


class TipoToken(Enum):
    DECLARAR = auto()
    MOSTRAR = auto()
    SI = auto()
    ENTONCES = auto()
    SINO = auto()
    REPETIR = auto()
    VECES = auto()
    VERDADERO = auto()
    FALSO = auto()
    ID = auto()
    NUMERO = auto()
    CADENA = auto()
    ASIGNAR = auto()
    SUMA = auto()
    RESTA = auto()
    MULT = auto()
    DIV = auto()
    MAYOR = auto()
    MENOR = auto()
    MAYOR_IGUAL = auto()
    MENOR_IGUAL = auto()
    IGUAL_IGUAL = auto()
    DIFERENTE = auto()
    LLAVE_IZQ = auto()
    LLAVE_DER = auto()
    PAREN_IZQ = auto()
    PAREN_DER = auto()
    SALTO_LINEA = auto()
    FIN_ARCHIVO = auto()


@dataclass(frozen=True)
class Token:
    tipo: TipoToken
    lexema: str
    linea: int
    columna: int


PALABRAS_RESERVADAS = {
    "declarar": TipoToken.DECLARAR,
    "mostrar": TipoToken.MOSTRAR,
    "si": TipoToken.SI,
    "entonces": TipoToken.ENTONCES,
    "sino": TipoToken.SINO,
    "repetir": TipoToken.REPETIR,
    "veces": TipoToken.VECES,
    "verdadero": TipoToken.VERDADERO,
    "falso": TipoToken.FALSO,
}
