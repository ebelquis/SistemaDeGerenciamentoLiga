from entidades.atletica import Atletica
from entidades.gestor_geral import GestorGeral
from datetime import date

atletica1 = Atletica("A5")
atletica1.penalidades = 2

atletica2 = Atletica("ATM")
atletica2.penalidades = 1

atletica3 = Atletica("ATCTC")
atletica3.penalidades = 0

gestor = GestorGeral("Kayo", "kayo@gmail.com", "senha", 48999999999)

lista_atleticas = [atletica1, atletica2, atletica3]

def menu_principal():
    continuar = True
    
    while continuar:
        print("\n" + "="*35)
        print("SISTEMA DE GERENCIAMENTO DA LIGA")
        print("="*35)
        print("Olá,", gestor.nome)
        print("1 - Consultar Penalidades")
        print("2 - Analisar denúncia")
        print("0 - Sair do Sistema")
        print("="*35)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Aqui chamamos o método que criámos na classe Pessoa!
            gestor.consultar_penalidades(lista_atleticas)

        elif opcao == "2":
            gestor.analisar_denuncia(atletica1, atletica2, date.today(), "ATM não compareceu com os atletas no Vôlei Feminino")
            
        elif opcao == "0":
            print("\nA sair do sistema... Até logo!")
            continuar = False # Isto quebra o loop 'while' e encerra o programa
            
        else:
            print("\nErro: Opção inválida! Tente novamente.")

# Executa o menu quando o ficheiro rodar
if __name__ == "__main__":
    menu_principal()
    