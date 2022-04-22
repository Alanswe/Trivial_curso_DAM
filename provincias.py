from sql import Sqlite
from settings import BD


class Provincia():
    tabla = 'T_provincias'
    def __init__(self,codigo,descripcion, id=None) -> None:
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__id = id

    # def insertar(self):
    #     # obsoleto
    #     manejador = Sqlite(BD)
    #     campos = 'codigo,descripcion'
    #     valores = f'{self.__codigo},{self.__descripcion}'
    #     nuevo_id = manejador.insertar(Provincia.tabla,campos,valores)
    #     return nuevo_id

    def guardar(self):
        manejador = Sqlite(BD)
        campos = 'codigo,descripcion'
        valores = f'{self.__codigo},{self.__descripcion}'
        if self.__id:
            nuevo_id = manejador.actualizar(Provincia.tabla,campos,valores,self.__id)
            return nuevo_id
        else:
            nuevo_id = manejador.insertar(Provincia.tabla,campos,valores)
            return nuevo_id

    def leer_por_id(self,id_privincia):
        manejador = Sqlite(BD)
        lista = manejador.seleccionar(f'select * from T_provincias where id = {id_privincia}') # NO HACER ASI POR SEGURIDAD, SOLO ES UN EJEMPLO
        if lista:
            return Provincia(lista[0][1],lista[0][2],lista[0][0])
        else:
            return None

    def borrar(self,id_provincia):
        manejador = Sqlite(BD)
        resp = manejador.borrar(Provincia.tabla,'id',id_provincia)
        return resp
        