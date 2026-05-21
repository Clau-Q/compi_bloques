from __future__ import annotations

"""
Este archivo implementa el analizador lexico.
Lee el codigo fuente infantil caracter por caracter y lo transforma en
una lista de tokens para el analizador sintactico.
"""

from .definitions_l import PALABRAS_RESERVADAS, TipoToken, Token, simbolos_simples
from .errors_ls import ErrorLexico


def analizar_lexicamente(texto_fuente: str) -> list[Token]:
    """Convierte el texto fuente en tokens del lenguaje infantil."""
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

        if caracter in simbolos_simples:
            lista_tokens.append(
                Token(simbolos_simples[caracter], avanzar(), linea_inicio, columna_inicio)
            )
            continue

        if caracter == '"':
            avanzar()
            caracteres_texto: list[str] = []
            while indice < longitud and texto_fuente[indice] != '"':
                if texto_fuente[indice] == "\n":
                    raise ErrorLexico(
                        f"El texto comenzo en la linea {linea_inicio}, pero nunca se cerro."
                    )
                caracteres_texto.append(avanzar())
            if indice >= longitud:
                raise ErrorLexico(
                    f"El texto comenzo en la linea {linea_inicio}, pero nunca se cerro."
                )
            avanzar()
            lista_tokens.append(
                Token(
                    TipoToken.CADENA,
                    "".join(caracteres_texto),
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
            partes_palabra = [avanzar()]
            while indice < longitud and (
                texto_fuente[indice].isalnum() or texto_fuente[indice] == "_"
            ):
                partes_palabra.append(avanzar())
            lexema = "".join(partes_palabra)
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
