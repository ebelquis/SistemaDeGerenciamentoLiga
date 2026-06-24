# entidades/reserva.py
from entidades.enums import Semana, Modalidades
from entidades.atletica import Atletica
from entidades.quadra import Quadra

class Reserva:
    def __init__(self, atletica: Atletica, modalidade: Modalidades, naipe: str, quadra: Quadra, semana: Semana):
        self.__atletica = atletica
        self.__modalidade = modalidade
        self.__naipe = naipe
        self.__quadra = quadra
        self.__semana = semana

    @property
    def atletica(self): return self.__atletica
    @property
    def modalidade(self): return self.__modalidade
    @property
    def naipe(self): return self.__naipe
    @property
    def quadra(self): return self.__quadra
    @property
    def semana(self): return self.__semana