from __future__ import annotations

"""
Este archivo implementa el analizador sintactico.
Toma los tokens del lenguaje infantil, verifica que respeten la
gramatica y construye el arbol sintactico del programa.
"""

from .ast_nodes_s import (
    Booleano,
    CrearCajita,
    Guardar,
    Identificador,
    Mostrar,
    Negacion,
    Numero,
    OperacionBinaria,
    Preguntar,
    Programa,
    Repetir,
    SiPasa,
    Texto,
)
from .definitions_l import TipoToken, Token
from .errors_ls import ErrorSintactico
from .lexer_l import analizar_archivo_lexico, analizar_lexicamente


TIPOS_RELACIONALES = {
    TipoToken.MAYOR_QUE,
    TipoToken.MENOR_QUE,
    TipoToken.IGUAL_A,
    TipoToken.DIFERENTE_DE,
    TipoToken.MAYOR_O_IGUAL,
    TipoToken.MENOR_O_IGUAL,
}


TIPOS_DE_CAJITA = {
    TipoToken.TIPO_NUMERO,
    TipoToken.TIPO_DECIMAL,
    TipoToken.TIPO_TEXTO,
    TipoToken.TIPO_SI_NO,
}


class AnalizadorSintactico:
    """Valida la secuencia de tokens y construye un Programa infantil."""

    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.posicion_actual = 0

    def analizar(self) -> Programa:
        self._omitir_saltos_de_linea()
        sentencias = self._lista_de_sentencias({TipoToken.FIN_ARCHIVO})
        return Programa(sentencias=sentencias)

    def _lista_de_sentencias(self, tokens_de_cierre: set[TipoToken]) -> list:
        sentencias = []
        while not self._verificar(*tokens_de_cierre):
            if self._verificar(TipoToken.FIN_ARCHIVO):
                esperado = ", ".join(token.name for token in tokens_de_cierre)
                raise ErrorSintactico(
                    f"El bloque termino antes de encontrar {esperado.lower()}."
                )
            sentencias.append(self._sentencia())
            self._omitir_saltos_de_linea()
        return sentencias

    def _sentencia(self):
        if self._coincide(TipoToken.CREAR_CAJITA):
            nombre = self._consumir(
                TipoToken.ID, "Falta el nombre de la cajita despues de 'crear_cajita'."
            )
            self._consumir(
                TipoToken.COMO,
                "Falta la palabra 'como' para indicar que tipo de cajita vas a crear.",
            )
            tipo = self._consumir_tipo_de_cajita()
            return CrearCajita(nombre=nombre.lexema, tipo_cajita=tipo.lexema)

        if self._coincide(TipoToken.GUARDAR):
            nombre = self._consumir(
                TipoToken.ID, "Falta decir en que cajita quieres guardar."
            )
            self._consumir(
                TipoToken.CON,
                "Falta la palabra 'con' para indicar lo que vas a guardar.",
            )
            return Guardar(nombre=nombre.lexema, valor=self._expresion())

        if self._coincide(TipoToken.MOSTRAR):
            return Mostrar(valor=self._expresion())

        if self._coincide(TipoToken.PREGUNTAR):
            mensaje = self._consumir(
                TipoToken.CADENA,
                "Falta el texto de la pregunta entre comillas.",
            )
            self._consumir(
                TipoToken.GUARDAR_EN,
                "Falta la frase 'guardar_en' para decir donde guardar la respuesta.",
            )
            nombre = self._consumir(
                TipoToken.ID, "Falta el nombre de la cajita donde guardar la respuesta."
            )
            return Preguntar(mensaje=mensaje.lexema, guardar_en=nombre.lexema)

        if self._coincide(TipoToken.REPETIR):
            veces = self._expresion()
            self._consumir(TipoToken.VECES, "Falta la palabra 'veces'.")
            self._omitir_saltos_de_linea()
            cuerpo = self._lista_de_sentencias({TipoToken.FIN})
            self._consumir(TipoToken.FIN, "Falta 'fin' para cerrar el bloque de repetir.")
            return Repetir(veces=veces, cuerpo=cuerpo)

        if self._coincide(TipoToken.SI_PASA):
            condicion = self._condicion()
            self._consumir(TipoToken.ENTONCES, "Falta la palabra 'entonces'.")
            self._omitir_saltos_de_linea()
            cuerpo_si = self._lista_de_sentencias({TipoToken.SI_NO_PASA, TipoToken.FIN})
            cuerpo_sino = []
            if self._coincide(TipoToken.SI_NO_PASA):
                self._omitir_saltos_de_linea()
                cuerpo_sino = self._lista_de_sentencias({TipoToken.FIN})
            self._consumir(TipoToken.FIN, "Falta 'fin' para cerrar el bloque de si_pasa.")
            return SiPasa(condicion=condicion, cuerpo_si=cuerpo_si, cuerpo_sino=cuerpo_sino)

        token = self._token_actual()
        raise ErrorSintactico(
            f"La sentencia cerca de '{token.lexema}' no pertenece al lenguaje infantil esperado."
        )

    def _consumir_tipo_de_cajita(self) -> Token:
        if self._verificar(*TIPOS_DE_CAJITA):
            return self._avanzar()
        token = self._token_actual()
        raise ErrorSintactico(
            f"Falta el tipo de la cajita. Usa numero, decimal, texto o si_no. Linea {token.linea}."
        )

    def _condicion(self):
        return self._condicion_o()

    def _condicion_o(self):
        expresion = self._condicion_y()
        while self._coincide(TipoToken.O):
            operador = self._token_anterior().lexema
            derecha = self._condicion_y()
            expresion = OperacionBinaria(izquierda=expresion, operador=operador, derecha=derecha)
        return expresion

    def _condicion_y(self):
        expresion = self._condicion_no()
        while self._coincide(TipoToken.Y):
            operador = self._token_anterior().lexema
            derecha = self._condicion_no()
            expresion = OperacionBinaria(izquierda=expresion, operador=operador, derecha=derecha)
        return expresion

    def _condicion_no(self):
        if self._coincide(TipoToken.NO):
            return Negacion(expresion=self._condicion_no())
        return self._comparacion()

    def _comparacion(self):
        izquierda = self._expresion()
        if self._coincide(*TIPOS_RELACIONALES):
            operador = self._token_anterior().lexema
            derecha = self._expresion()
            return OperacionBinaria(izquierda=izquierda, operador=operador, derecha=derecha)
        return izquierda

    def _expresion(self):
        expresion = self._termino()
        while self._coincide(TipoToken.SUMA, TipoToken.RESTA):
            operador = self._token_anterior().lexema
            derecha = self._termino()
            expresion = OperacionBinaria(izquierda=expresion, operador=operador, derecha=derecha)
        return expresion

    def _termino(self):
        expresion = self._factor()
        while self._coincide(TipoToken.MULT, TipoToken.DIV):
            operador = self._token_anterior().lexema
            derecha = self._factor()
            expresion = OperacionBinaria(izquierda=expresion, operador=operador, derecha=derecha)
        return expresion

    def _factor(self):
        if self._coincide(TipoToken.NUMERO):
            lexema = self._token_anterior().lexema
            valor = float(lexema) if "." in lexema else int(lexema)
            return Numero(valor=valor)

        if self._coincide(TipoToken.CADENA):
            return Texto(valor=self._token_anterior().lexema)

        if self._coincide(TipoToken.VERDADERO):
            return Booleano(valor=True)

        if self._coincide(TipoToken.FALSO):
            return Booleano(valor=False)

        if self._coincide(TipoToken.ID):
            return Identificador(nombre=self._token_anterior().lexema)

        token = self._token_actual()
        raise ErrorSintactico(
            f"La expresion cerca de '{token.lexema}' no es valida en este lenguaje."
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
