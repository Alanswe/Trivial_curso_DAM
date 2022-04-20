from sql import Sqlite
from settings import BD

class Provincia():
    tabla = 'T_provincias'
    def __init__(self,codigo,descripcion, id=None) -> None:
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__id = id

    def insertar(self):
        manejador = Sqlite(BD)
        campos = 'codigo,descripcion'
        valores = f'{self.__codigo},{self.__descripcion}'
        nuevo_id = manejador.insertar(Provincia.tabla,campos,valores)
