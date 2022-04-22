import unittest
from provincias import Provincia
#from settings import BD
#'/home/alan/Documentos/Trivial_curso_DAM/personas.db'


class Test_provicias(unittest.TestCase):

    def test_exitencia(self):
        p = Provincia('','')
        self.assertIsNotNone(p)
        
    # def test_insert_provincia(self):
    #     p = Provincia(211,'Madrid')
    #     resp = p.insertar()
    #     self.assertIsNotNone(resp)

    def test_guardar_provincia_nueva(self):
        p = Provincia(646,'Francia')
        resp = p.guardar()
        self.assertIsNotNone(resp)

    def test_guardar_provincia_existente(self):
        p = Provincia(888,'Marruecos',5)
        resp = p.guardar()
        self.assertEqual(resp,1)

    def test_leer_por_id_no_existente(self):
        p = Provincia('','')
        resp = p.leer_por_id(199)
        self.assertEqual(resp,'turutu')

    def test_leer_por_id_existente(self):
        p = Provincia('','')
        resp = p.leer_por_id(1) #Huelva
        self.assertEqual(resp,'turutu')

    def test_borrar(self):
        p = Provincia('','')
        resp = p.borrar(7)
        self.assertIsNotNone(resp)
