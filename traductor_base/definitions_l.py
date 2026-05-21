"""
Este archivo concentra las definiciones formales del lenguaje.
Contiene los lexemas, las etiquetas academicas, el mapeo entre ambos y
los conjuntos de primeros que sirven como apoyo teorico para la exposicion.
"""

class LexemasInfantiles:
    DECLARAR = "declarar"
    MOSTRAR = "mostrar"
    SI = "si"
    ENTONCES = "entonces"
    SINO = "sino"
    REPETIR = "repetir"
    VECES = "veces"
    VERDADERO = "verdadero"
    FALSO = "falso"
    SALTO_LINEA = "\n"
    LLAVE_IZQ = "{"
    LLAVE_DER = "}"
    PAREN_IZQ = "("
    PAREN_DER = ")"
    COMA = ","
    MAS = "+"
    MENOS = "-"
    MULTIPLICA = "*"
    DIVIDE = "/"
    ASIGNA = "="
    MAYOR = ">"
    MENOR = "<"
    IGUAL = "=="
    DIFERENTE = "!="
    MAYOR_IGUAL = ">="
    MENOR_IGUAL = "<="
    Y = "&&"
    O = "||"
    NUMERO = "numero"
    FLOTANTE = "flotante"
    CADENA = "cadena"
    BOOLEANO = "booleano"
    ID = "id"


class EtiquetasInfantiles:
    DECLARACION = "DECLARACION"
    IMPRESION = "IMPRESION"
    CONDICION_SI = "CONDICION_SI"
    CONDICION_SINO = "CONDICION_SINO"
    REPETICION = "REPETICION"
    VECES = "VECES"
    TRUE = "TRUE"
    FALSE = "FALSE"
    SALTO_LINEA = "SALTO_LINEA"
    LLAVE_IZQ = "LLAVE_IZQ"
    LLAVE_DER = "LLAVE_DER"
    PAREN_IZQ = "PAREN_IZQ"
    PAREN_DER = "PAREN_DER"
    COMA = "COMA"
    SUMA = "SUMA"
    RESTA = "RESTA"
    MULTIPLICA = "MULTIPLICA"
    DIVIDE = "DIVIDE"
    ASIGNACION = "ASIGNACION"
    MAYOR = "MAYOR"
    MENOR = "MENOR"
    IGUAL = "IGUAL"
    DIFERENTE = "DIFERENTE"
    MAYOR_IGUAL = "MAYOR_IGUAL"
    MENOR_IGUAL = "MENOR_IGUAL"
    Y = "OPERADOR_Y"
    O = "OPERADOR_O"
    PROGRAMA = "PROGRAMA"
    BLOQUE = "BLOQUE"
    NUMERO = "NUMERO"
    FLOTANTE = "FLOTANTE"
    CADENA = "CADENA"
    BOOLEANO = "BOOLEANO"
    ID = "ID"


lexema_a_etiqueta = {
    LexemasInfantiles.DECLARAR: EtiquetasInfantiles.DECLARACION,
    LexemasInfantiles.MOSTRAR: EtiquetasInfantiles.IMPRESION,
    LexemasInfantiles.SI: EtiquetasInfantiles.CONDICION_SI,
    LexemasInfantiles.ENTONCES: "ENTONCES",
    LexemasInfantiles.SINO: EtiquetasInfantiles.CONDICION_SINO,
    LexemasInfantiles.REPETIR: EtiquetasInfantiles.REPETICION,
    LexemasInfantiles.VECES: EtiquetasInfantiles.VECES,
    LexemasInfantiles.VERDADERO: EtiquetasInfantiles.TRUE,
    LexemasInfantiles.FALSO: EtiquetasInfantiles.FALSE,
    LexemasInfantiles.SALTO_LINEA: EtiquetasInfantiles.SALTO_LINEA,
    LexemasInfantiles.LLAVE_IZQ: EtiquetasInfantiles.LLAVE_IZQ,
    LexemasInfantiles.LLAVE_DER: EtiquetasInfantiles.LLAVE_DER,
    LexemasInfantiles.PAREN_IZQ: EtiquetasInfantiles.PAREN_IZQ,
    LexemasInfantiles.PAREN_DER: EtiquetasInfantiles.PAREN_DER,
    LexemasInfantiles.COMA: EtiquetasInfantiles.COMA,
    LexemasInfantiles.MAS: EtiquetasInfantiles.SUMA,
    LexemasInfantiles.MENOS: EtiquetasInfantiles.RESTA,
    LexemasInfantiles.MULTIPLICA: EtiquetasInfantiles.MULTIPLICA,
    LexemasInfantiles.DIVIDE: EtiquetasInfantiles.DIVIDE,
    LexemasInfantiles.ASIGNA: EtiquetasInfantiles.ASIGNACION,
    LexemasInfantiles.MAYOR: EtiquetasInfantiles.MAYOR,
    LexemasInfantiles.MENOR: EtiquetasInfantiles.MENOR,
    LexemasInfantiles.IGUAL: EtiquetasInfantiles.IGUAL,
    LexemasInfantiles.DIFERENTE: EtiquetasInfantiles.DIFERENTE,
    LexemasInfantiles.MAYOR_IGUAL: EtiquetasInfantiles.MAYOR_IGUAL,
    LexemasInfantiles.MENOR_IGUAL: EtiquetasInfantiles.MENOR_IGUAL,
    LexemasInfantiles.Y: EtiquetasInfantiles.Y,
    LexemasInfantiles.O: EtiquetasInfantiles.O,
}


simbolos_compuestos = {
    LexemasInfantiles.IGUAL: EtiquetasInfantiles.IGUAL,
    LexemasInfantiles.DIFERENTE: EtiquetasInfantiles.DIFERENTE,
    LexemasInfantiles.MENOR_IGUAL: EtiquetasInfantiles.MENOR_IGUAL,
    LexemasInfantiles.MAYOR_IGUAL: EtiquetasInfantiles.MAYOR_IGUAL,
    LexemasInfantiles.Y: EtiquetasInfantiles.Y,
    LexemasInfantiles.O: EtiquetasInfantiles.O,
}


primeros = {
    "Programa": [EtiquetasInfantiles.DECLARACION, EtiquetasInfantiles.IMPRESION, EtiquetasInfantiles.REPETICION, EtiquetasInfantiles.CONDICION_SI, EtiquetasInfantiles.ID],
    "Sentencia": [EtiquetasInfantiles.DECLARACION, EtiquetasInfantiles.IMPRESION, EtiquetasInfantiles.REPETICION, EtiquetasInfantiles.CONDICION_SI, EtiquetasInfantiles.ID],
    "Declaracion": [EtiquetasInfantiles.DECLARACION],
    "Asignacion": [EtiquetasInfantiles.ID],
    "Impresion": [EtiquetasInfantiles.IMPRESION],
    "Repeticion": [EtiquetasInfantiles.REPETICION],
    "Condicional": [EtiquetasInfantiles.CONDICION_SI],
    "Bloque": [EtiquetasInfantiles.LLAVE_IZQ],
    "Expresion": [
        EtiquetasInfantiles.PAREN_IZQ,
        EtiquetasInfantiles.ID,
        EtiquetasInfantiles.NUMERO,
        EtiquetasInfantiles.FLOTANTE,
        EtiquetasInfantiles.CADENA,
        EtiquetasInfantiles.TRUE,
        EtiquetasInfantiles.FALSE,
    ],
}
