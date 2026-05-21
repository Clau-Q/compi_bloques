from __future__ import annotations

"""
Este archivo define los nodos del arbol sintactico.
Sirve para representar en memoria la estructura del programa despues de
que el parser valida la secuencia de tokens.
"""

from dataclasses import dataclass, field


@dataclass
class Nodo:
    pass


@dataclass
class Expresion(Nodo):
    pass


@dataclass
class Numero(Expresion):
    valor: int | float


@dataclass
class Cadena(Expresion):
    valor: str


@dataclass
class Booleano(Expresion):
    valor: bool


@dataclass
class Identificador(Expresion):
    nombre: str


@dataclass
class OperacionBinaria(Expresion):
    izquierda: Expresion
    operador: str
    derecha: Expresion


@dataclass
class Sentencia(Nodo):
    pass


@dataclass
class Declaracion(Sentencia):
    nombre: str
    valor: Expresion


@dataclass
class Asignacion(Sentencia):
    nombre: str
    valor: Expresion


@dataclass
class Mostrar(Sentencia):
    valor: Expresion


@dataclass
class Repetir(Sentencia):
    veces: Expresion
    cuerpo: list[Sentencia] = field(default_factory=list)


@dataclass
class Si(Sentencia):
    condicion: Expresion
    cuerpo_si: list[Sentencia] = field(default_factory=list)
    cuerpo_sino: list[Sentencia] = field(default_factory=list)


@dataclass
class Programa(Nodo):
    sentencias: list[Sentencia] = field(default_factory=list)
