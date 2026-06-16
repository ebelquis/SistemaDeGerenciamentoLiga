# limites/tela_penalidade.py

class TelaPenalidade:
    def mensagem_solicita_filtro(self):
        print("\n--- Consultar Penalidades ---")
        print("1 - Todas as atléticas")
        print("2 - Apenas uma atlética")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        return int(opcao) if opcao.isnumeric() else 0

    def solicita_nome(self):
        return input("Digite o nome da atlética: ")

    # Exibe de todas as atléticas
    def exibe_resultado(self, lista_atleticas):
        print("\n--- Penalidades de todas as atléticas ---")
        if not lista_atleticas:
            print("Nenhuma atlética cadastrada.")
        for atletica in lista_atleticas:
            print(f"Atlética {atletica.nome}: {atletica.penalidades} penalidade(s).")

    # Exibe da atlética encontrada
    def exibe_resultado_atletica(self, penalidades):
        print(f"\nA atlética possui {penalidades} penalidade(s).")

    def exibe_erro(self, mensagem):
        print(f"\nErro: {mensagem}")