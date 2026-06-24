# entidades/lista_espera.py

class ListaEspera:
    def __init__(self, posicao_lista: int):
        self.__posicao_lista = posicao_lista

    @property
    def posicao_lista(self):
        return self.__posicao_lista

    @posicao_lista.setter
    def posicao_lista(self, nova_posicao):
        self.__posicao_lista = nova_posicao