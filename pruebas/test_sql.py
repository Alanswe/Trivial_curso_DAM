import unittest
from sql import Sqlite,sqlite3

class Testsqlite(unittest.TestCase):

    def test_exitencia(self):
        mi_bd = Sqlite('/home/alan/Documentos/Trivial_curso_DAM/personas.db')
        cnx = mi_bd.conectar()
        self.assertIsNotNone(cnx)

    def test_seleccionar(self):
        mi_bd = Sqlite('/home/alan/Documentos/Trivial_curso_DAM/personas.db')
        resultado = mi_bd.seleccionar()
        self.assertIsNotNone(resultado)

    def test_borrar(self):
        mi_bd = Sqlite('/home/alan/Documentos/Trivial_curso_DAM/personas.db')
        resultado = mi_bd.borrar('articulos','id','46')
        self.assertIsNone(resultado)

    def test_insertion_articulo(self):
        mi_bd = Sqlite('/home/alan/Documentos/Trivial_curso_DAM/personas.db')
        campos = 'codigo, descripcion, precio'
        valores = '"234234","Nada","123"'
        resultado = mi_bd.insertar('articulos',campos,valores)
        self.assertIsNotNone(resultado)

    def test_update(self):
        mi_bd = Sqlite('/home/alan/Documentos/Trivial_curso_DAM/personas.db')
        campos = 'codigo, descripcion, precio'
        valores = '234234,Algo,123'
        resultado = mi_bd.actualizar('articulos',campos,valores,48)
        self.assertEqual(resultado,1)
