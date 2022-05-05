
class Modo():
    def __init__(self,num_preguntas=10,num_jugadores=1,tmax_juego=600,tmax_pregunta=600) -> None:
        self.__num_preguntas = num_preguntas
        self.__num_jugadores = num_jugadores
        self.__tmax_juego = tmax_juego
        self.__tmax_pregunta = tmax_pregunta

    @property
    def num_preguntas(self):
        return self.__num_preguntas

    @property
    def num_jugadores(self):
        return self.__num_jugadores
        
    @property
    def tmax_juego(self):
        return self.__tmax_juego

    @property
    def tmax_pregunta(self):
        return self.__tmax_pregunta
