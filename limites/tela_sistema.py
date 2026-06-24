# limites/tela_sistema.py

class TelaSistema:
    def tela_opcoes_iniciais(self):
        print("\n" + "="*40)
        print("    SGLA - UFSC (Menu Inicial)    ")
        print("="*40)
        print("1 - Fazer Login")
        print("0 - Encerrar Sistema")
        return self.__ler_opcao(1)

    def tela_opcoes_membro(self):
        print("\n" + "="*40)
        print("    PAINEL DA ATLÉTICA    ")
        print("="*40)
        print("1 - Solicitar Reserva de Quadra")
        print("2 - Cancelar Reserva Ativa")
        print("3 - Visualizar Disponibilidade (Cronograma)")
        print("4 - Denunciar Não Comparecimento")
        print("0 - Fazer Logout")
        return self.__ler_opcao(4)
    
    def tela_opcoes_gestor_atletica(self):
        print("\n" + "="*40)
        print("    PAINEL DO GESTOR DA ATLÉTICA    ")
        print("="*40)
        print("1 - Solicitar Reserva de Quadra")
        print("2 - Cancelar Reserva Ativa")
        print("3 - Visualizar Disponibilidade (Cronograma)")
        print("4 - Denunciar Não Comparecimento")
        print("5 - Cadastrar Novo Membro na Atlética") # <--- EXCLUSIVO DELE
        print("0 - Fazer Logout")
        return self.__ler_opcao(5)

    def tela_opcoes_gestor(self):
        print("\n" + "="*40)
        print("    PAINEL DO GESTOR GERAL    ")
        print("="*40)
        print("1 - Avaliar Denúncias Pendentes")
        print("2 - Visualizar Disponibilidade (Cronograma)")
        print("3 - Gerenciar Atléticas (CRUD)") 
        print("0 - Fazer Logout")
        return self.__ler_opcao(3) 

    def mostrar_mensagem(self, mensagem):
        print(f"\n{mensagem}")

    def __ler_opcao(self, max_opcoes):
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if 0 <= opcao <= max_opcoes:
                    return opcao
                print(f"Opção inválida. Escolha entre 0 e {max_opcoes}.")
            except ValueError:
                print("Erro: Digite um número válido.")