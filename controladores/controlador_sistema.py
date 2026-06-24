# controladores/controlador_sistema.py

import pickle
import os
from limites.tela_sistema import TelaSistema
from controladores.controlador_login import ControladorLogin
from controladores.controlador_reservas import ControladorReservas
from controladores.controlador_denuncias import ControladorDenuncias
from controladores.controlador_atleticas import ControladorAtleticas
from controladores.controlador_membros import ControladorMembros
from entidades.gestor_geral import GestorGeral
from entidades.gestor_atletica import GestorAtletica
from dados_teste import carregar_dados_iniciais

from dados_teste import carregar_dados_iniciais

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__arquivo_dados = "dados_sgla.pkl" # Nome do arquivo que vai guardar tudo
        
        self.__carregar_dados()
        
        # Inicializa os Controladores Secundários
        self.__controlador_login = ControladorLogin(self.__usuarios)
        self.__controlador_reservas = ControladorReservas(self.__ginasios)
        self.__controlador_denuncias = ControladorDenuncias(self.__atleticas)
        self.__controlador_atleticas = ControladorAtleticas(self.__atleticas, self.__usuarios)
        self.__controlador_membros = ControladorMembros(self.__usuarios)

    def __carregar_dados(self):
        """Lê o arquivo congelado. Se não existir, gera os dados de teste."""
        if os.path.exists(self.__arquivo_dados):
            with open(self.__arquivo_dados, 'rb') as arquivo:
                dados = pickle.load(arquivo)
                self.__atleticas = dados['atleticas']
                self.__usuarios = dados['usuarios']
                self.__ginasios = dados['ginasios']
        else:
            # Se é a primeira vez rodando, pega os dados do dados_teste.py
            self.__atleticas, self.__usuarios, self.__ginasios = carregar_dados_iniciais()
            self.__salvar_dados() # Já cria o arquivo inicial

    def __salvar_dados(self):
        """Congela todas as listas e salva no arquivo .pkl"""
        with open(self.__arquivo_dados, 'wb') as arquivo:
            dados = {
                'atleticas': self.__atleticas,
                'usuarios': self.__usuarios,
                'ginasios': self.__ginasios
            }
            pickle.dump(dados, arquivo)

    def iniciar(self):
        # Laço principal do sistema
        while True:
            opcao = self.__tela_sistema.tela_opcoes_iniciais()
            
            if opcao == 1:
                usuario_logado = self.__controlador_login.realizar_login()
                if usuario_logado:
                    self.__redirecionar_usuario(usuario_logado)
            elif opcao == 0:
                self.__salvar_dados() 
                self.__tela_sistema.mostrar_mensagem("Dados salvos com sucesso! Encerrando o SGLA-UFSC. Até logo!")
                break

    def __redirecionar_usuario(self, usuario):
        if isinstance(usuario, GestorGeral):
            self.__loop_gestor(usuario)
        elif isinstance(usuario, GestorAtletica):
            self.__loop_gestor_atletica(usuario)
        else:
            self.__loop_membro(usuario)

    def __loop_membro(self, usuario):
        while True:
            opcao = self.__tela_sistema.tela_opcoes_membro()
            
            if opcao == 1:
                self.__controlador_reservas.solicitar_reserva(usuario.atletica)
            elif opcao == 2:
                self.__controlador_reservas.cancelar_reserva(usuario.atletica)
            elif opcao == 3:
                self.__controlador_reservas.visualizar_disponibilidade()
            elif opcao == 4:
                self.__controlador_denuncias.registrar_denuncia(usuario.atletica)
            elif opcao == 0:
                self.__controlador_login.realizar_logout()
                break
    
    def __loop_gestor_atletica(self, usuario):
        while True:
            opcao = self.__tela_sistema.tela_opcoes_gestor_atletica()
            if opcao == 1: self.__controlador_reservas.solicitar_reserva(usuario.atletica)
            elif opcao == 2: self.__controlador_reservas.cancelar_reserva(usuario.atletica)
            elif opcao == 3: self.__controlador_reservas.visualizar_disponibilidade()
            elif opcao == 4: self.__controlador_denuncias.registrar_denuncia(usuario.atletica)
            elif opcao == 5: self.__controlador_membros.cadastrar_membro(usuario.atletica)
            elif opcao == 0: 
                self.__controlador_login.realizar_logout()
                break

    def __loop_gestor(self, usuario):
        while True:
            opcao = self.__tela_sistema.tela_opcoes_gestor()
            
            if opcao == 1:
                self.__controlador_denuncias.avaliar_denuncias(usuario)
            elif opcao == 2:
                self.__controlador_reservas.visualizar_disponibilidade()
            elif opcao == 3:
                self.__controlador_atleticas.abrir_menu()
            elif opcao == 0:
                self.__controlador_login.realizar_logout()
                break