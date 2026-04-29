from entidades.pessoa import Pessoa
from entidades.atletica import Atletica
from datetime import datetime
#import bcrypt

class GestorGeral(Pessoa):
    def analisar_denuncia(self, denunciante: Atletica, infratora: Atletica, data: datetime, ocorrido: str):
        print("\n---- Analisar denuncia ----\n ")
        print(f"Atletica Infratora: {infratora.nome} \nAtletica Denunciante: {denunciante.nome} \nData: {data} \nDelato do ocorrido: {ocorrido} \nDeseja aceitar denuncia e aplicar penalidade? (1 - Sim / 2 - Não)\n")

        opcao = input()

        if opcao == "1":
            infratora.penalidades += 2
            print(f"\nConcluído \nA atlética infratora, {infratora.nome}, recebeu duas semanas de penalidade\n")
        else:
            print("\nDenúncia rejeitada\n")
    
    def indisponibilizar_quadra(self, quadra, data):
        """Permite marcar quadras como ocupadas para eventos/ feriados."""
        pass

    def set_penalidade_atletica(self, atletica, valor: int):
        """muda punições de atlética"""
        pass


    def CRUD_atletica(self, nome: str):
        """Gerenciamento macro das atléticas vinculadas à UFSC."""
        pass

    def CRUD_gestor_atletica(self, email, nome, senha, tel, atletica, cargo):
        """Atende ao RF11: Gestão de usuários do sistema[cite: 49]."""
        pass