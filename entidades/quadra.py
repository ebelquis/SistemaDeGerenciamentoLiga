# entidades/quadra.py
from entidades.enums import Semana, Modalidades

class Quadra:
    def __init__(self, semana: Semana, modalidade: Modalidades, naipe: str):
        self.__semana = semana
        self.__modalidade = modalidade
        self.__naipe = naipe
        self.__reservas = []      
        self.__espera = []
        self.__lista_espera = []  # Lista de objetos ListaEspera (Para controle de posição)

    @property
    def semana(self):
        return self.__semana

    @property
    def modalidade(self):
        return self.__modalidade

    @property
    def naipe(self):
        return self.__naipe

    @property
    def reservas(self):
        return self.__reservas

    @property
    def espera(self):
        return self.__espera

    @property
    def lista_espera(self):
        return self.__lista_espera