import sqlite3

class Sqlite():
    """
    Clase para gestionar el trabajo con la base de datos sqlite.
    - Conectarse a la base de datos
    - Insertar
    - Seleccionar   
    - Actualizar
    - Borrar
    """

    #TODO:  

    def __init__(self,bd) -> None:
        """
        Inicializa la clase con la propiedad nombre de la bd
        """
        self.__base_datos = bd

    def conectar(self):
        """
        Conecta/desconecta el código con la basde de datos
        """
        cnx = sqlite3.connect(self.__base_datos)
        return cnx
        #cnx.close()

    def seleccionar(self):
        """
        Ejecutar la consulta de selección de datos y devuelve el resultado
        """
        consulta = "select * from persona"
        cnx = self.conectar()
        cursor = cnx.cursor()
        cursor.execute(consulta)
        salida = cursor.fetchall
        return salida



    def insertar(self):
        pass

    def actualizar(self):
        pass

    def borrar(self):
        pass
