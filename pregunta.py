class Pregunta():
    def __init__(self,cuerpo,id,dificultad=0,tematica='general') -> None:
        self.__id = id
        self.__cuerpo = cuerpo
        self.__dificultad = dificultad
        self.__tematica = tematica