class Partida():
    def __init__(self, obj_jugador, obj_modo,col_preguntas) -> None:
        self.__jugador = obj_jugador
        self.__modo = obj_modo
        self.__col_preguntas = col_preguntas
        self.__marcador = 0 
    
    def iniciar(self):
        print(self.__jugador)
        print(self.__modo)
        print(self.__col_preguntas)
        print(self.__col_preguntas[0].respuestas)
        print(self.__marcador)

    def finalizar(self):
        pass

    def barajar(self):
        pass

    def comprobar_resp(self, id_pregunta, id_respuesta):
        pass
    
    def actualizar_puntos(self):
        # if comprobar_resp()
        # self.__jugador.resultado += 1
        pass
