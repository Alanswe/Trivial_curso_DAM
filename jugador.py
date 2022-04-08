class Jugador():
    def __init__(self, nombre,resultado=0) -> None:
        self.__nombre = nombre
        self.__resultado = resultado
        
    @property
    def nombre(self):
        return self.__nombre

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, res):
        self.__resultado = res

        
