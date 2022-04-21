import unittest
from provincias import Provincia
#from settings import BD
#'/home/alan/Documentos/Trivial_curso_DAM/personas.db'


class Test_provicias(unittest.TestCase):

    def test_exitencia(self):
        p = Provincia('','')
        self.assertIsNotNone(p)
        
    def test_insert_provincia(self):
        p = Provincia(111,'Pamplona')
        resp = p.insertar()
        self.assertIsNotNone(resp)
