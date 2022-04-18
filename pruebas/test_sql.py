import unittest
from sql import Sqlite,sqlite3

class Testsqlite(unittest.TestCase):

    def test_exitencia(self):
        mi_bd = Sqlite('/home/alan/Documentos/GitHub/web_1/personas.db')
        cnx = mi_bd.conectar()
        self.assertIsNotNone(cnx)

    def test_seleccionar(self):
        mi_bd = Sqlite('/home/alan/Documentos/GitHub/web_1/personas.db')
        resultado = mi_bd.seleccionar()
        print(resultado)
        self.assertIsNotNone(resultado)
