from __future__ import annotations

"""
Este archivo implementa el analizador sintactico.
Toma los tokens producidos por el lexer, verifica que respeten la
gramatica y construye el arbol sintactico del programa.
"""

from .ast_nodes_s import (
    Asignacion,
    Booleano,
    Cadena,
    Declaracion,
    Identificador,
    Mostrar,
    Numero,
    OperacionBinaria,
    Programa,
    Repetir,
    Si,
)
from .errors_ls import ErrorSintactico
from .lexer_l import analizar_archivo_lexico, analizar_lexicamente
from .tokens_l import TipoToken, Token


TIPOS_RELACIONALES = {
    TipoToken.MAYOR,
    TipoToken.MENOR,
    TipoToken.MAYOR_IGUAL,
    TipoToken.MENOR_IGUAL,
    TipoToken.IGUAL_IGUAL,
    TipoToken.DIFERENTE,
}


class AnalizadorSintactico:
    """Valida la secuencia de tokens y construye un Programa."""
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.posicion_actual = 0

    def analizar(self) -> Programa:
        self._omitir_saltos_de_linea()
        sentencias = []
        while not self._verificar(TipoToken.FIN_ARCHIVO):
            sentencias.append(self._sentencia())
            self._omitir_saltos_de_linea()
        return Programa(sentencias=sentencias)

    def _sentencia(self):
        if self._coincide(TipoToken.DECLARAR):
            nombre = self._consumir(
                TipoToken.ID, "Se esperaba un identificador despues de 'declarar'."
            )
            self._consumir(TipoToken.ASIGNAR, "Se esperaba '=' en la declaracion.")
            return Declaracion(nombre=nombre.lexema, valor=self._expresion())

        if self._coincide(TipoToken.MOSTRAR):
            return Mostrar(valor=self._expresion())

        if self._coincide(TipoToken.REPETIR):
            veces = self._expresion()
            self._consumir(TipoToken.VECES, "Se esperaba la palabra 'veces'.")
            cuerpo = self._bloque()
            return Repetir(veces=veces, cuerpo=cuerpo)

        if self._coincide(TipoToken.SI):
            condicion = self._condicion()
            self._consumir(TipoToken.ENTONCES, "Se esperaba la palabra 'entonces'.")
            cuerpo_si = self._bloque()
            cuerpo_sino = []
            if self._coincide(TipoToken.SINO):
                cuerpo_sino = self._bloque()
            return Si(condicion=condicion, cuerpo_si=cuerpo_si, cuerpo_sino=cuerpo_sino)

        if self._verificar(TipoToken.ID) and self._verificar_siguiente(TipoToken.ASIGNAR):
            nombre = self._avanzar()
            self._avanzar()
            return Asignacion(nombre=nombre.lexema, valor=self._expresion())

        token = self._token_actual()
        raise ErrorSintactico(
            f"Sentencia inesperada cerca de '{token.lexema}' en linea {token.linea}, columna {token.columna}."
        )

    def _bloque(self) -> list:
        self._consumir(TipoToken.LLAVE_IZQ, "Se esperaba '{' para iniciar un bloque.")
        self._omitir_saltos_de_linea()
        sentencias = []
        while not self._verificar(TipoToken.LLAVE_DER):
            if self._verificar(TipoToken.FIN_ARCHIVO):
                token = self._token_actual()
                raise ErrorSintactico(
                    f"Bloque sin cerrar en linea {token.linea}, columna {token.columna}."
                )
            sentencias.append(self._sentencia())
            self._omitir_saltos_de_linea()
        self._consumir(TipoToken.LLAVE_DER, "Se esperaba '}' para cerrar el bloque.")
        return sentencias

    def _condicion(self):
        izquierda = self._expresion()
        if self._coincide(*TIPOS_RELACIONALES):
            operador = self._token_anterior().lexema
            derecha = self._expresion()
            return OperacionBinaria(
                izquierda=izquierda, operador=operador, derecha=derecha
            )
        return izquierda

    def _expresion(self):
        expresion = self._termino()
        while self._coincide(TipoToken.SUMA, TipoToken.RESTA):
            operador = self._token_anterior().lexema
            derecha = self._termino()
            expresion = OperacionBinaria(
                izquierda=expresion, operador=operador, derecha=derecha
            )
        return expresion

    def _termino(self):
        expresion = self._factor()
        while self._coincide(TipoToken.MULT, TipoToken.DIV):
            operador = self._token_anterior().lexema
            derecha = self._factor()
            expresion = OperacionBinaria(
                izquierda=expresion, operador=operador, derecha=derecha
            )
        return expresion

    def _factor(self):
        if self._coincide(TipoToken.NUMERO):
            lexema = self._token_anterior().lexema
            valor = float(lexema) if "." in lexema else int(lexema)
            return Numero(valor=valor)

        if self._coincide(TipoToken.CADENA):
            return Cadena(valor=self._token_anterior().lexema)

        if self._coincide(TipoToken.VERDADERO):
            return Booleano(valor=True)

        if self._coincide(TipoToken.FALSO):
            return Booleano(valor=False)

        if self._coincide(TipoToken.ID):
            return Identificador(nombre=self._token_anterior().lexema)

        if self._coincide(TipoToken.PAREN_IZQ):
            expresion = self._expresion()
            self._consumir(
                TipoToken.PAREN_DER, "Se esperaba ')' para cerrar la expresion."
            )
            return expresion

        token = self._token_actual()
        raise ErrorSintactico(
            f"Expresion invalida cerca de '{token.lexema}' en linea {token.linea}, columna {token.columna}."
        )

    def _coincide(self, *tipos: TipoToken) -> bool:
        if self._verificar(*tipos):
            self._avanzar()
            return True
        return False

    def _consumir(self, tipo_token: TipoToken, mensaje: str) -> Token:
        if self._verificar(tipo_token):
            return self._avanzar()
        token = self._token_actual()
        raise ErrorSintactico(f"{mensaje} Linea {token.linea}, columna {token.columna}.")

    def _omitir_saltos_de_linea(self) -> None:
        while self._coincide(TipoToken.SALTO_LINEA):
            pass

    def _verificar(self, *tipos: TipoToken) -> bool:
        if self._esta_al_final():
            return TipoToken.FIN_ARCHIVO in tipos
        return self._token_actual().tipo in tipos

    def _verificar_siguiente(self, tipo_token: TipoToken) -> bool:
        if self.posicion_actual + 1 >= len(self.tokens):
            return False
        return self.tokens[self.posicion_actual + 1].tipo == tipo_token

    def _avanzar(self) -> Token:
        if not self._esta_al_final():
            self.posicion_actual += 1
        return self._token_anterior()

    def _esta_al_final(self) -> bool:
        return self._token_actual().tipo == TipoToken.FIN_ARCHIVO

    def _token_actual(self) -> Token:
        return self.tokens[self.posicion_actual]

    def _token_anterior(self) -> Token:
        return self.tokens[self.posicion_actual - 1]


def analizar_sintaxis(texto_fuente: str) -> Programa:
    """Ejecuta el analisis sintactico a partir de texto fuente."""
    return AnalizadorSintactico(analizar_lexicamente(texto_fuente)).analizar()


def analizar_archivo_sintactico(ruta: str) -> Programa:
    """Abre un archivo y ejecuta sobre el el analisis sintactico."""
    return AnalizadorSintactico(analizar_archivo_lexico(ruta)).analizar()
