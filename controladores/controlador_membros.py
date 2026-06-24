# controladores/controlador_membros.py
from entidades.membro_atletica import MembroAtletica

class ControladorMembros:
    def __init__(self, lista_usuarios):
        self.__usuarios = lista_usuarios

    def cadastrar_membro(self, atletica_do_gestor):
        print("\n--- Cadastro de Novo Membro ---")
        nome = input("Nome: ").strip()
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        tel = input("Telefone: ").strip()
        cargo = input("Cargo (Ex: Diretor de Esportes): ").strip()

        novo_membro = MembroAtletica(nome, email, senha, tel, atletica_do_gestor, cargo)
        
        self.__usuarios.append(novo_membro) # Permite que faça login
        atletica_do_gestor.membros.append(novo_membro) # Guarda na atlética
        
        print("\nSucesso! Novo membro cadastrado e já pode fazer login no SGLA.")
        input("Pressione ENTER para continuar...")