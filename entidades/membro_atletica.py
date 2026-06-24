from entidades.pessoa import Pessoa
from entidades.atletica import Atletica

class MembroAtletica(Pessoa):
    def __init__(self, nome, email, senha, telefone, atletica: Atletica, cargo: str):
        super().__init__(nome, email, senha, telefone)
        self.__atletica = atletica
        self.__cargo = cargo

    @property
    def atletica(self):
        return self.__atletica
    @atletica.setter
    def atletica(self, valor):
        self.__atletica = valor

    @property
    def cargo(self): 
        return self.__cargo
    @cargo.setter
    def cargo(self, valor):
        self.__cargo = valor

    def cancelar_reserva(self, reserva):
        """Atende ao RF06: Cancelamento de reservas"""
        pass

    def confirmar_interesse_lista(self):
        """Atende ao RF07: Aceite de redistribuição de horários"""
        pass

    def denunciar(self, atletica, data, ocorrido: str):
        """Atende ao RF14: Denúncias sobre não comparecimento"""
        pass

    def responder_notificacao_selecao(self):
        """Atende ao RF12: Notificações sobre lista de espera"""
        pass

    def sair_lista(self, lista_espera):
        """Lógica para remover a atlética da fila de espera"""
        pass

    def solicitar_reserva(self, modalidade, naipe: str):
        """Atende ao RF03: Solicitação de reserva de quadras"""
        pass