# limites/tela_denuncia.py

class TelaDenuncia:
    def obter_dados_denuncia(self, lista_atleticas):
        print("\n--- Registrar Denúncia de Não Comparecimento ---")
        print("Selecione a atlética infratora:")
        
        for i, atl in enumerate(lista_atleticas, start=1):
            print(f"{i} - {atl.nome}")
        print("0 - Cancelar")

        while True:
            try:
                escolha = int(input("Digite o número da atlética: "))
                if escolha == 0:
                    return None
                if 1 <= escolha <= len(lista_atleticas):
                    infratora = lista_atleticas[escolha - 1]
                    break
                print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")

        dia = input("Qual foi o dia do treino? (ex: Segunda-Feira): ").strip()
        motivo = input("Descreva o ocorrido: ").strip()

        return {"infratora": infratora, "dia": dia, "motivo": motivo}

    def exibir_denuncia_pendente(self, denuncia):
        print("\n" + "="*50)
        print("--- AVALIAÇÃO DE DENÚNCIA (Acesso: Gestor Geral) ---")
        print(f"Denunciante: {denuncia.denunciante.nome}")
        print(f"Infratora: {denuncia.infratora.nome}")
        print(f"Dia do ocorrido: {denuncia.dia}")
        print(f"Relato: {denuncia.motivo}")
        print("="*50)

        print("Deseja confirmar a denúncia e aplicar penalidade de 2 semanas?")
        print("1 - Sim (Aprovar e Punir a Infratora)")
        print("2 - Não (Rejeitar e Arquivar)")

        while True:
            opcao = input("Escolha uma opção: ").strip()
            if opcao in ["1", "2"]:
                return opcao == "1"
            print("Opção inválida. Digite 1 ou 2.")

    def mostrar_mensagem(self, mensagem):
        print(f"\n{mensagem}")