# limites/tela_atletica.py

class TelaAtletica:
    def tela_opcoes(self):
        print("\n" + "="*40)
        print("    GERENCIAR ATLÉTICAS    ")
        print("="*40)
        print("1 - Cadastrar Nova Atlética")
        print("2 - Listar Atléticas Cadastradas")
        print("0 - Voltar ao Menu Anterior")
        
        while True:
            try:
                opcao = int(input("Escolha uma opção: "))
                if 0 <= opcao <= 2:
                    return opcao
                print("Opção inválida.")
            except ValueError:
                print("Erro: Digite um número válido.")

    def obter_dados_atletica(self):
        print("\n--- Cadastro de Atlética e Gestor ---")
        nome_atl = input("Nome da nova atlética: ").strip()
        print("\n-- Dados do Gestor da Atlética --")
        nome_gestor = input("Nome do Gestor: ").strip()
        email = input("Email de acesso: ").strip()
        senha = input("Senha de acesso: ").strip()
        telefone = input("Telefone: ").strip()
        
        return {"nome_atl": nome_atl, "nome_gestor": nome_gestor, "email": email, "senha": senha, "telefone": telefone}

    def mostrar_atleticas(self, atleticas):
        print("\n--- Lista de Atléticas ---")
        if not atleticas:
            print("Nenhuma atlética cadastrada no sistema.")
            return
            
        for i, atl in enumerate(atleticas, start=1):
            print(f"{i} - {atl.nome} (Penalidades: {atl.penalidades})")

    def mostrar_mensagem(self, mensagem):
        print(f"\n{mensagem}")