# entidades/ginasio.py
from abc import ABC, abstractmethod

class GinasioBase(ABC):
    def __init__(self, nome: str, modalidades: list):
        self.__nome = nome
        self.__modalidades = modalidades
        self.__encerrou = False

    @property
    def nome(self): return self.__nome

    @abstractmethod
    def obter_quadras_disponiveis(self):
        pass

class GinasioFixo(GinasioBase):
    def __init__(self, nome: str, modalidades: list):
        super().__init__(nome, modalidades)
        self.__quadra_por_dia = [] # Lista de objetos Quadra

    @property
    def quadra_por_dia(self): return self.__quadra_por_dia

    def adicionar_quadra(self, quadra):
        self.__quadra_por_dia.append(quadra)

    def obter_quadras_disponiveis(self):
        return self.__quadra_por_dia