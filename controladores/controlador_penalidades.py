# controladores/controlador_penalidades.py
from limites.tela_penalidade import TelaPenalidade

class ControladorPenalidades:
    # Inicializa a tela e recebe a lista de atléticas do sistema
    def __init__(self, lista_de_atleticas):
        self.__tela = TelaPenalidade()
        self.__atleticas = lista_de_atleticas

    def obter_todas_atleticas(self):
        return self.__atleticas

    def procurar_atletica_nome(self, nome):
        for atletica in self.__atleticas:
            if atletica.nome.lower() == nome.lower():
                return atletica
        return None

    def processar_selecao(self):
        continuar = True
        while continuar:
            opcao = self.__tela.mensagem_solicita_filtro()
            
            if opcao == 1: # Todas as atléticas (ficou meio contraintuitivo, mas no diagrama fiz assim já)
                lista = self.obter_todas_atleticas()
                self.__tela.exibe_resultado(lista)
                
            elif opcao == 2: # Apenas uma atlética
                nome = self.__tela.solicita_nome()
                atletica_existente = self.procurar_atletica_nome(nome)
                
                if atletica_existente:
                    self.__tela.exibe_resultado_atletica(atletica_existente.penalidades)
                else:
                    self.__tela.exibe_erro("Atlética não existente!")
                    
            elif opcao == 0:
                continuar = False
            else:
                self.__tela.exibe_erro("Opção inválida!")