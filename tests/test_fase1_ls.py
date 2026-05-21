"""
Este archivo contiene pruebas basicas de la fase 1.
Sirve para comprobar que el lexer reconoce identificadores, que el
escaner genera etiquetas y que el parser construye un programa valido.
"""

import unittest

from traductor_base.lexer_l import analizar_lexicamente
from traductor_base.parser_s import analizar_sintaxis
from traductor_base.scanner_l import Escaner
from traductor_base.sourcecode_l import CodigoFuente


class Fase1Tests(unittest.TestCase):
    def test_lexer_reconoce_identificador(self):
        tokens = analizar_lexicamente("declarar contador = 3\n")
        self.assertEqual(tokens[1].tipo.name, "ID")
        self.assertEqual(tokens[1].lexema, "contador")

    def test_scanner_genera_etiquetas(self):
        scanner = Escaner(CodigoFuente("mostrar contador\n"))
        tokens = scanner.tokenizar()
        self.assertEqual(tokens[0].etiqueta, "IMPRESION")
        self.assertEqual(tokens[1].etiqueta, "ID")

    def test_parser_construye_programa(self):
        program = analizar_sintaxis("declarar contador = 0\nmostrar contador\n")
        self.assertEqual(program.__class__.__name__, "Programa")
        self.assertEqual(len(program.sentencias), 2)


if __name__ == "__main__":
    unittest.main()
