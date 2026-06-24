# entidades/denuncia.py
from entidades.atletica import Atletica

class Denuncia:
    def __init__(self, denunciante: Atletica, infratora: Atletica, dia: str, motivo: str):
        self.__denunciante = denunciante
        self.__infratora = infratora
        self.__dia = dia
        self.__motivo = motivo
        self.__status = "Pendente" # Pode ser "Pendente", "Aprovada" ou "Rejeitada"

    @property
    def denunciante(self):
        return self.__denunciante
    
    @property
    def infratora(self):
        return self.__infratora
    
    @property
    def dia(self):
        return self.__dia
    
    @property
    def motivo(self):
        return self.__motivo
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, valor): self.__status = valor