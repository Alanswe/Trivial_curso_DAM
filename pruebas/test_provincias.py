import unittest
from sql import Sqlite,sqlite3

class Test_provicias(unittest.TestCase):

    def test_exitencia(self):
        mi_bd = Sqlite('/home/alan/Documentos/Trivial_curso_DAM/personas.db')
        cnx = mi_bd.conectar()
        self.assertIsNotNone(cnx)
        