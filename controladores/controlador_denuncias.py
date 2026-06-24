# controladores/controlador_denuncias.py
from limites.tela_denuncia import TelaDenuncia
from entidades.denuncia import Denuncia

class ControladorDenuncias:
    def __init__(self, lista_atleticas):
        self.__tela_denuncia = TelaDenuncia()
        self.__atleticas = lista_atleticas
        self.__denuncias_pendentes = []

    def registrar_denuncia(self, atletica_denunciante):
        # Filtra a lista para a atlética não poder denunciar a si própria
        outras_atleticas = [a for a in self.__atleticas if a != atletica_denunciante]
        
        dados = self.__tela_denuncia.obter_dados_denuncia(outras_atleticas)
        if not dados:
            self.__tela_denuncia.mostrar_mensagem("Registro de denúncia cancelado.")
            return

        nova_denuncia = Denuncia(
            denunciante=atletica_denunciante,
            infratora=dados["infratora"],
            dia=dados["dia"],
            motivo=dados["motivo"]
        )
        self.__denuncias_pendentes.append(nova_denuncia)
        self.__tela_denuncia.mostrar_mensagem(f"Denúncia registrada com sucesso! O Gestor Geral irá avaliar.")

    def avaliar_denuncias(self, gestor_logado):
        if not self.__denuncias_pendentes:
            self.__tela_denuncia.mostrar_mensagem("Não há denúncias pendentes para avaliação no momento.")
            return

        # Puxa a denúncia mais antiga da fila 
        denuncia_atual = self.__denuncias_pendentes[0]
        aprovada = self.__tela_denuncia.exibir_denuncia_pendente(denuncia_atual)

        if aprovada:
            denuncia_atual.infratora.penalidades += 2
            denuncia_atual.status = "Aprovada"
            self.__tela_denuncia.mostrar_mensagem(
                f"[SISTEMA] Denúncia APROVADA! A atlética {denuncia_atual.infratora.nome} recebeu 2 semanas de penalidade."
            )
        else:
            denuncia_atual.status = "Rejeitada"
            self.__tela_denuncia.mostrar_mensagem("[SISTEMA] Denúncia REJEITADA e arquivada por falta de provas.")

        # Remove da fila de pendentes após o veredito
        self.__denuncias_pendentes.pop(0)