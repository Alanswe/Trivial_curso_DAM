class Respuesta():
    def __init__(self,id,cuerpo,correcto=False) -> None:
        self.__id = id
        self.__cuerpo = cuerpo
        self.__correcto = correcto

    @property
    def id(self):
        return self.__id

    @property
    def cuerpo(self):
        return self.__cuerpo
        
    @property
    def correcto(self):
        return self.__correcto
