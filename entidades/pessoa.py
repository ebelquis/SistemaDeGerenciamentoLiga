#import bcrypt
from abc import ABC, abstractmethod
from controladores.controlador_penalidades import ControladorPenalidades

class Pessoa(ABC):
    def __init__ (self, nome, email, senha, telefone):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def login(self, email, senha):
        if email == self.email and senha == self.senha:
            return True

    def consultar_disponibilidade(self):
        #consultar todas as quadras/ginasios
        return
    
    def consultar_penalidades(self, lista_atleticas):
        # Cria o controlador passando a "base de dados" de atléticas
        controlador = ControladorPenalidades(lista_atleticas)

        controlador.processar_selecao()