class Pregunta():
    def __init__(self,cuerpo,id,dificultad=0,tematica='general') -> None:
        self.__id = id
        self.__cuerpo = cuerpo
        self.__dificultad = dificultad
        self.__tematica = tematica
        self.respuesta = [] # Colección de objetos respuesta

    @property
    def id(self):
        return self.__id

    @property
    def cuerpo(self):
        return self.__cuerpo
        
    @property
    def dificultad(self):
        return self.__dificultad
        
    @property
    def tematica(self):
        return self.__tematica
