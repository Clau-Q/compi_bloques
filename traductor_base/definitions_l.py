from __future__ import annotations

"""
Este archivo concentra la base formal de la fase lexico.
Contiene los lexemas infantiles del lenguaje, sus etiquetas academicas,
los tipos de token y las estructuras que usan el lexer y el scanner.
"""

from dataclasses import dataclass
from enum import Enum, auto


class TipoToken(Enum):
    CREAR_CAJITA = auto()
    GUARDAR = auto()
    COMO = auto()
    CON = auto()
    MOSTRAR = auto()
    PREGUNTAR = auto()
    GUARDAR_EN = auto()
    SI_PASA = auto()
    SI_NO_PASA = auto()
    ENTONCES = auto()
    REPETIR = auto()
    VECES = auto()
    FIN = auto()
    TIPO_NUMERO = auto()
    TIPO_DECIMAL = auto()
    TIPO_TEXTO = auto()
    TIPO_SI_NO = auto()
    VERDADERO = auto()
    FALSO = auto()
    MAYOR_QUE = auto()
    MENOR_QUE = auto()
    IGUAL_A = auto()
    DIFERENTE_DE = auto()
    MAYOR_O_IGUAL = auto()
    MENOR_O_IGUAL = auto()
    Y = auto()
    O = auto()
    NO = auto()
    ID = auto()
    NUMERO = auto()
    CADENA = auto()
    SUMA = auto()
    RESTA = auto()
    MULT = auto()
    DIV = auto()
    SALTO_LINEA = auto()
    FIN_ARCHIVO = auto()


@dataclass(frozen=True)
class Token:
    tipo: TipoToken
    lexema: str
    linea: int
    columna: int


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


PALABRAS_RESERVADAS = {
    "crear_cajita": TipoToken.CREAR_CAJITA,
    "guardar": TipoToken.GUARDAR,
    "como": TipoToken.COMO,
    "con": TipoToken.CON,
    "mostrar": TipoToken.MOSTRAR,
    "preguntar": TipoToken.PREGUNTAR,
    "guardar_en": TipoToken.GUARDAR_EN,
    "si_pasa": TipoToken.SI_PASA,
    "si_no_pasa": TipoToken.SI_NO_PASA,
    "entonces": TipoToken.ENTONCES,
    "repetir": TipoToken.REPETIR,
    "veces": TipoToken.VECES,
    "fin": TipoToken.FIN,
    "numero": TipoToken.TIPO_NUMERO,
    "decimal": TipoToken.TIPO_DECIMAL,
    "texto": TipoToken.TIPO_TEXTO,
    "si_no": TipoToken.TIPO_SI_NO,
    "verdadero": TipoToken.VERDADERO,
    "falso": TipoToken.FALSO,
    "mayor_que": TipoToken.MAYOR_QUE,
    "menor_que": TipoToken.MENOR_QUE,
    "igual_a": TipoToken.IGUAL_A,
    "diferente_de": TipoToken.DIFERENTE_DE,
    "mayor_o_igual": TipoToken.MAYOR_O_IGUAL,
    "menor_o_igual": TipoToken.MENOR_O_IGUAL,
    "y": TipoToken.Y,
    "o": TipoToken.O,
    "no": TipoToken.NO,
}


class LexemasInfantiles:
    CREAR_CAJITA = "crear_cajita"
    GUARDAR = "guardar"
    COMO = "como"
    CON = "con"
    MOSTRAR = "mostrar"
    PREGUNTAR = "preguntar"
    GUARDAR_EN = "guardar_en"
    SI_PASA = "si_pasa"
    SI_NO_PASA = "si_no_pasa"
    ENTONCES = "entonces"
    REPETIR = "repetir"
    VECES = "veces"
    FIN = "fin"
    TIPO_NUMERO = "numero"
    TIPO_DECIMAL = "decimal"
    TIPO_TEXTO = "texto"
    TIPO_SI_NO = "si_no"
    VERDADERO = "verdadero"
    FALSO = "falso"
    MAYOR_QUE = "mayor_que"
    MENOR_QUE = "menor_que"
    IGUAL_A = "igual_a"
    DIFERENTE_DE = "diferente_de"
    MAYOR_O_IGUAL = "mayor_o_igual"
    MENOR_O_IGUAL = "menor_o_igual"
    Y = "y"
    O = "o"
    NO = "no"
    SALTO_LINEA = "\n"
    MAS = "+"
    MENOS = "-"
    MULTIPLICA = "*"
    DIVIDE = "/"
    ID = "id"


class EtiquetasInfantiles:
    CREAR_CAJITA = "CREAR_CAJITA"
    GUARDAR = "GUARDAR"
    COMO = "COMO"
    CON = "CON"
    MOSTRAR = "MOSTRAR"
    PREGUNTAR = "PREGUNTAR"
    GUARDAR_EN = "GUARDAR_EN"
    SI_PASA = "SI_PASA"
    SI_NO_PASA = "SI_NO_PASA"
    ENTONCES = "ENTONCES"
    REPETIR = "REPETIR"
    VECES = "VECES"
    FIN = "FIN"
    TIPO_NUMERO = "TIPO_NUMERO"
    TIPO_DECIMAL = "TIPO_DECIMAL"
    TIPO_TEXTO = "TIPO_TEXTO"
    TIPO_SI_NO = "TIPO_SI_NO"
    VERDADERO = "VERDADERO"
    FALSO = "FALSO"
    MAYOR_QUE = "MAYOR_QUE"
    MENOR_QUE = "MENOR_QUE"
    IGUAL_A = "IGUAL_A"
    DIFERENTE_DE = "DIFERENTE_DE"
    MAYOR_O_IGUAL = "MAYOR_O_IGUAL"
    MENOR_O_IGUAL = "MENOR_O_IGUAL"
    Y = "OPERADOR_Y"
    O = "OPERADOR_O"
    NO = "OPERADOR_NO"
    SALTO_LINEA = "SALTO_LINEA"
    SUMA = "SUMA"
    RESTA = "RESTA"
    MULTIPLICA = "MULTIPLICA"
    DIVIDE = "DIVIDE"
    NUMERO = "NUMERO"
    CADENA = "CADENA"
    ID = "ID"


lexema_a_etiqueta = {
    LexemasInfantiles.CREAR_CAJITA: EtiquetasInfantiles.CREAR_CAJITA,
    LexemasInfantiles.GUARDAR: EtiquetasInfantiles.GUARDAR,
    LexemasInfantiles.COMO: EtiquetasInfantiles.COMO,
    LexemasInfantiles.CON: EtiquetasInfantiles.CON,
    LexemasInfantiles.MOSTRAR: EtiquetasInfantiles.MOSTRAR,
    LexemasInfantiles.PREGUNTAR: EtiquetasInfantiles.PREGUNTAR,
    LexemasInfantiles.GUARDAR_EN: EtiquetasInfantiles.GUARDAR_EN,
    LexemasInfantiles.SI_PASA: EtiquetasInfantiles.SI_PASA,
    LexemasInfantiles.SI_NO_PASA: EtiquetasInfantiles.SI_NO_PASA,
    LexemasInfantiles.ENTONCES: EtiquetasInfantiles.ENTONCES,
    LexemasInfantiles.REPETIR: EtiquetasInfantiles.REPETIR,
    LexemasInfantiles.VECES: EtiquetasInfantiles.VECES,
    LexemasInfantiles.FIN: EtiquetasInfantiles.FIN,
    LexemasInfantiles.TIPO_NUMERO: EtiquetasInfantiles.TIPO_NUMERO,
    LexemasInfantiles.TIPO_DECIMAL: EtiquetasInfantiles.TIPO_DECIMAL,
    LexemasInfantiles.TIPO_TEXTO: EtiquetasInfantiles.TIPO_TEXTO,
    LexemasInfantiles.TIPO_SI_NO: EtiquetasInfantiles.TIPO_SI_NO,
    LexemasInfantiles.VERDADERO: EtiquetasInfantiles.VERDADERO,
    LexemasInfantiles.FALSO: EtiquetasInfantiles.FALSO,
    LexemasInfantiles.MAYOR_QUE: EtiquetasInfantiles.MAYOR_QUE,
    LexemasInfantiles.MENOR_QUE: EtiquetasInfantiles.MENOR_QUE,
    LexemasInfantiles.IGUAL_A: EtiquetasInfantiles.IGUAL_A,
    LexemasInfantiles.DIFERENTE_DE: EtiquetasInfantiles.DIFERENTE_DE,
    LexemasInfantiles.MAYOR_O_IGUAL: EtiquetasInfantiles.MAYOR_O_IGUAL,
    LexemasInfantiles.MENOR_O_IGUAL: EtiquetasInfantiles.MENOR_O_IGUAL,
    LexemasInfantiles.Y: EtiquetasInfantiles.Y,
    LexemasInfantiles.O: EtiquetasInfantiles.O,
    LexemasInfantiles.NO: EtiquetasInfantiles.NO,
    LexemasInfantiles.SALTO_LINEA: EtiquetasInfantiles.SALTO_LINEA,
    LexemasInfantiles.MAS: EtiquetasInfantiles.SUMA,
    LexemasInfantiles.MENOS: EtiquetasInfantiles.RESTA,
    LexemasInfantiles.MULTIPLICA: EtiquetasInfantiles.MULTIPLICA,
    LexemasInfantiles.DIVIDE: EtiquetasInfantiles.DIVIDE,
}


simbolos_simples = {
    LexemasInfantiles.MAS: TipoToken.SUMA,
    LexemasInfantiles.MENOS: TipoToken.RESTA,
    LexemasInfantiles.MULTIPLICA: TipoToken.MULT,
    LexemasInfantiles.DIVIDE: TipoToken.DIV,
}


primeros = {
    "Programa": [
        EtiquetasInfantiles.CREAR_CAJITA,
        EtiquetasInfantiles.GUARDAR,
        EtiquetasInfantiles.MOSTRAR,
        EtiquetasInfantiles.PREGUNTAR,
        EtiquetasInfantiles.REPETIR,
        EtiquetasInfantiles.SI_PASA,
    ],
    "Sentencia": [
        EtiquetasInfantiles.CREAR_CAJITA,
        EtiquetasInfantiles.GUARDAR,
        EtiquetasInfantiles.MOSTRAR,
        EtiquetasInfantiles.PREGUNTAR,
        EtiquetasInfantiles.REPETIR,
        EtiquetasInfantiles.SI_PASA,
    ],
    "CrearCajita": [EtiquetasInfantiles.CREAR_CAJITA],
    "Guardar": [EtiquetasInfantiles.GUARDAR],
    "Mostrar": [EtiquetasInfantiles.MOSTRAR],
    "Preguntar": [EtiquetasInfantiles.PREGUNTAR],
    "Repetir": [EtiquetasInfantiles.REPETIR],
    "SiPasa": [EtiquetasInfantiles.SI_PASA],
    "Bloque": [
        EtiquetasInfantiles.CREAR_CAJITA,
        EtiquetasInfantiles.GUARDAR,
        EtiquetasInfantiles.MOSTRAR,
        EtiquetasInfantiles.PREGUNTAR,
        EtiquetasInfantiles.REPETIR,
        EtiquetasInfantiles.SI_PASA,
        EtiquetasInfantiles.FIN,
        EtiquetasInfantiles.SI_NO_PASA,
    ],
    "Expresion": [
        EtiquetasInfantiles.ID,
        EtiquetasInfantiles.NUMERO,
        EtiquetasInfantiles.CADENA,
        EtiquetasInfantiles.VERDADERO,
        EtiquetasInfantiles.FALSO,
        EtiquetasInfantiles.NO,
    ],
}
