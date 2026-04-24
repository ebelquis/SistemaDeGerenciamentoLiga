class Atletica:
    def __init__(self, nome):
        self.__nome = nome
        self.__penalidades = 0
        self.__membros = []
        self.__reservas = []
        self.__listas_espera = []
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def penalidades(self):
        return self.__penalidades
    
    @penalidades.setter
    def penalidades(self, penalidades):
        self.__penalidades = penalidades
    
    @property
    def membros(self):
        return self.__membros

    @property
    def reservas(self):
        return self.__reservas
    
    @property
    def listas_espera(self):
        return self.__listas_espera
