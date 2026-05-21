from __future__ import annotations

"""
Este archivo implementa el analizador lexico.
Lee el codigo fuente caracter por caracter y lo transforma en una lista
de tokens que luego usa el analizador sintactico.
"""

from .errors_ls import ErrorLexico
from .tokens_l import PALABRAS_RESERVADAS, TipoToken, Token


def analizar_lexicamente(texto_fuente: str) -> list[Token]:
    """Convierte el texto fuente en tokens del lenguaje."""
    lista_tokens: list[Token] = []
    indice = 0
    linea = 1
    columna = 1
    longitud = len(texto_fuente)

    def avanzar(cantidad: int = 1) -> str:
        nonlocal indice, linea, columna
        fragmento = texto_fuente[indice:indice + cantidad]
        for caracter in fragmento:
            if caracter == "\n":
                linea += 1
                columna = 1
            else:
                columna += 1
        indice += cantidad
        return fragmento

    while indice < longitud:
        caracter = texto_fuente[indice]
        linea_inicio = linea
        columna_inicio = columna

        if caracter in " \t\r":
            avanzar()
            continue

        if caracter == "\n":
            lexema = avanzar()
            lista_tokens.append(Token(TipoToken.SALTO_LINEA, lexema, linea_inicio, columna_inicio))
            continue

        dos_caracteres = texto_fuente[indice:indice + 2]
        if dos_caracteres in {">=", "<=", "==", "!="}:
            tipo_token = {
                ">=": TipoToken.MAYOR_IGUAL,
                "<=": TipoToken.MENOR_IGUAL,
                "==": TipoToken.IGUAL_IGUAL,
                "!=": TipoToken.DIFERENTE,
            }[dos_caracteres]
            lista_tokens.append(Token(tipo_token, avanzar(2), linea_inicio, columna_inicio))
            continue

        mapa_simbolo_simple = {
            "=": TipoToken.ASIGNAR,
            "+": TipoToken.SUMA,
            "-": TipoToken.RESTA,
            "*": TipoToken.MULT,
            "/": TipoToken.DIV,
            ">": TipoToken.MAYOR,
            "<": TipoToken.MENOR,
            "{": TipoToken.LLAVE_IZQ,
            "}": TipoToken.LLAVE_DER,
            "(": TipoToken.PAREN_IZQ,
            ")": TipoToken.PAREN_DER,
        }
        if caracter in mapa_simbolo_simple:
            lista_tokens.append(
                Token(mapa_simbolo_simple[caracter], avanzar(), linea_inicio, columna_inicio)
            )
            continue

        if caracter == '"':
            avanzar()
            caracteres_cadena: list[str] = []
            while indice < longitud and texto_fuente[indice] != '"':
                if texto_fuente[indice] == "\n":
                    raise ErrorLexico(
                        f"Cadena sin cerrar en linea {linea_inicio}, columna {columna_inicio}."
                    )
                caracteres_cadena.append(avanzar())
            if indice >= longitud:
                raise ErrorLexico(
                    f"Cadena sin cerrar en linea {linea_inicio}, columna {columna_inicio}."
                )
            avanzar()
            lista_tokens.append(
                Token(
                    TipoToken.CADENA,
                    "".join(caracteres_cadena),
                    linea_inicio,
                    columna_inicio,
                )
            )
            continue

        if caracter.isdigit():
            partes_numero = [avanzar()]
            tiene_punto = False
            while indice < longitud:
                caracter_actual = texto_fuente[indice]
                if caracter_actual.isdigit():
                    partes_numero.append(avanzar())
                elif caracter_actual == "." and not tiene_punto:
                    tiene_punto = True
                    partes_numero.append(avanzar())
                else:
                    break
            lista_tokens.append(
                Token(
                    TipoToken.NUMERO,
                    "".join(partes_numero),
                    linea_inicio,
                    columna_inicio,
                )
            )
            continue

        if caracter.isalpha() or caracter == "_":
            partes_identificador = [avanzar()]
            while indice < longitud and (
                texto_fuente[indice].isalnum() or texto_fuente[indice] == "_"
            ):
                partes_identificador.append(avanzar())
            lexema = "".join(partes_identificador)
            tipo_token = PALABRAS_RESERVADAS.get(lexema, TipoToken.ID)
            lista_tokens.append(Token(tipo_token, lexema, linea_inicio, columna_inicio))
            continue

        raise ErrorLexico(
            f"Caracter inesperado {caracter!r} en linea {linea_inicio}, columna {columna_inicio}."
        )

    lista_tokens.append(Token(TipoToken.FIN_ARCHIVO, "", linea, columna))
    return lista_tokens


def analizar_archivo_lexico(ruta: str) -> list[Token]:
    """Abre un archivo y ejecuta sobre el el analisis lexico."""
    with open(ruta, "r", encoding="utf-8") as archivo:
        return analizar_lexicamente(archivo.read())
