# controladores/controlador_atleticas.py
from limites.tela_atletica import TelaAtletica
from entidades.atletica import Atletica
from entidades.gestor_atletica import GestorAtletica # <--- IMPORT NOVO

class ControladorAtleticas:
    def __init__(self, lista_atleticas, lista_usuarios):
        self.__tela_atletica = TelaAtletica()
        self.__atleticas = lista_atleticas
        self.__usuarios = lista_usuarios

    def abrir_menu(self):
        while True:
            opcao = self.__tela_atletica.tela_opcoes()
            if opcao == 1:
                self.cadastrar_atletica()
            elif opcao == 2:
                self.listar_atleticas()
            elif opcao == 0:
                break

    def cadastrar_atletica(self):
        dados = self.__tela_atletica.obter_dados_atletica()
        
        # Cria a atlética
        nova_atletica = Atletica(dados["nome_atl"])
        self.__atleticas.append(nova_atletica)
        
        # Cria o Gestor e adiciona à lista de login do sistema
        novo_gestor = GestorAtletica(
            nome=dados["nome_gestor"], 
            email=dados["email"], 
            senha=dados["senha"], 
            telefone=dados["telefone"], 
            atletica=nova_atletica, 
            cargo="Gestor de Atlética"
        )
        self.__usuarios.append(novo_gestor)
        
        self.__tela_atletica.mostrar_mensagem(f"Sucesso! Atlética '{nova_atletica.nome}' e o Gestor '{novo_gestor.nome}' foram cadastrados!")

    def listar_atleticas(self):
        self.__tela_atletica.mostrar_atleticas(self.__atleticas)