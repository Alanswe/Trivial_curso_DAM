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

    #TODO: hacerlos con un Try

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


    def borrar(self,tabla,camo_id,valor_id): # Para no dar por supuesto que tenga un campo id
        consulta = f"delete from {tabla} where {camo_id} = {valor_id}"
        cnx = self.conectar()
        cnx.execute(consulta)
        cnx.commit()
        cnx.close()

    def insertar(self,tabla, lista_campos, lista_valores):
        """
            Añade un nuevo registro a la tabla pasada como parámetro.
            La lista de cmapos debe tener el mismo número de elementos que la de valores.
        """
        cnx = self.conectar()
        lista_comillas = []
        for val in lista_valores.split(','):
            lista_comillas.append("'"+ val + "'")

        tmp = ','.join(lista_comillas)

        consulta = f"insert into {tabla}({lista_campos}) values({tmp})"
        cursor = cnx.cursor()
        cursor.execute(consulta)
        cnx.commit()
        salida = cursor.lastrowid
        cnx.close()
        return salida

    def actualizar(self,tabla, lista_campos, lista_valores, valor_id):
        cnx = self.conectar()
        consulta = f"update {tabla} set "

        """
        UPDATE persona SET nombre='Alansitod' WHERE id=1;
        """
        tmp = ''
        campos = lista_campos.split(',')
        valores = lista_valores.split(',')
        for i in range(len(valores)):
            tmp += f"{campos[i]}='{valores[i]}',"

        consulta += tmp[:-1]
        consulta += f'where id={valor_id};'


        cursor = cnx.cursor()
        cursor.execute(consulta)
        cnx.commit()
        salida = cursor.rowcount
        cnx.close()

        return salida
