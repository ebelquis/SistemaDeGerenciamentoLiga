# limites/tela_reserva.py
from entidades.enums import Semana, Modalidades

class TelaReserva:
    
    def selecionar_dia(self, dias_disponiveis):
        print("\n--- Solicitação de Reserva (Treinos 22h às 00h) ---")
        print("\nEscolha o dia da semana:")
        for i, dia in enumerate(dias_disponiveis, start=1):
            print(f"{i} - {dia.value}")
            
        escolha = self.__ler_opcao_valida(len(dias_disponiveis))
        return dias_disponiveis[escolha - 1]

    def selecionar_modalidade(self, modalidades_disponiveis):
        print("\nEscolha a modalidade disponível para este dia:")
        for i, mod in enumerate(modalidades_disponiveis, start=1):
            print(f"{i} - {mod.value}")
            
        escolha = self.__ler_opcao_valida(len(modalidades_disponiveis))
        return modalidades_disponiveis[escolha - 1]

    def selecionar_naipe(self, naipes_disponiveis):
        print("\nEscolha o naipe disponível:")
        for i, naipe in enumerate(naipes_disponiveis, start=1):
            print(f"{i} - {naipe}")
            
        escolha = self.__ler_opcao_valida(len(naipes_disponiveis))
        return naipes_disponiveis[escolha - 1]

    def __ler_opcao_valida(self, max_opcoes, aceita_zero=False):
        min_val = 0 if aceita_zero else 1
        while True:
            try:
                opcao = int(input("Digite o número correspondente: "))
                if min_val <= opcao <= max_opcoes:
                    return opcao
                else:
                    print(f"Opção inválida. Digite um número entre {min_val} e {max_opcoes}.")
            except ValueError:
                print("Erro: Por favor, digite apenas números inteiros.")

    def mostrar_mensagem(self, mensagem):
        print(f"\n{mensagem}")


    def listar_e_selecionar_reserva(self, reservas_atletica):
        print("\n--- Cancelamento de Reserva ---")
        if not reservas_atletica:
            print("A sua atlética não possui reservas ativas para cancelar.")
            return None

        print("Escolha a reserva que deseja cancelar:")
        for i, reserva in enumerate(reservas_atletica, start=1):
            print(f"{i} - {reserva.semana.value} | {reserva.modalidade.value} {reserva.naipe}")
        
        print("0 - Voltar")
        
        escolha = self.__ler_opcao_valida(len(reservas_atletica), aceita_zero=True)
        if escolha == 0:
            return None
            
        return reservas_atletica[escolha - 1]

    def solicitar_aceite_vaga(self, nome_atletica, dia, modalidade):
        print(f"\n[NOTIFICAÇÃO SISTEMA] Atlética {nome_atletica}, uma vaga abriu para {modalidade} na {dia}!")
        resposta = input("Deseja aceitar a vaga? (1 - Sim / 2 - Não): ").strip()
        return resposta == "1"

    def mostrar_disponibilidade(self, cronograma_formatado):
        print("\n" + "="*60)
        print("--- CRONOGRAMA E DISPONIBILIDADE DE QUADRAS (CDS) ---")
        print("Horário Fixo: 22h às 00h")
        print("="*60)
        
        ordem_dias = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira"]
        
        for dia in ordem_dias:
            if dia in cronograma_formatado:
                print(f"\n[ {dia.upper()} ]")
                for linha in cronograma_formatado[dia]:
                    print(linha)
            else:
                print(f"\n[ {dia.upper()} ]")
                print("- Nenhuma modalidade configurada para este dia.")
        
        print("\n" + "="*60)