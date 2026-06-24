# controladores/controlador_reservas.py
from limites.tela_reserva import TelaReserva
from entidades.reserva import Reserva
from entidades.lista_espera import ListaEspera
from entidades.enums import Semana

class ControladorReservas:
    def __init__(self, lista_ginasios):
        self.__tela_reserva = TelaReserva()
        self.__ginasios = lista_ginasios 

    def solicitar_reserva(self, atletica_solicitante):
        # Pede o Dia
        dia_enum = self.__tela_reserva.selecionar_dia(list(Semana))

        # Descobre quais modalidades existem NESSE dia específico
        modalidades_do_dia = []
        for ginasio in self.__ginasios:
            for quadra in ginasio.obter_quadras_disponiveis():
                if quadra.semana == dia_enum and quadra.modalidade not in modalidades_do_dia:
                    modalidades_do_dia.append(quadra.modalidade)

        if not modalidades_do_dia:
            self.__tela_reserva.mostrar_mensagem("Não há modalidades cadastradas para este dia.")
            return

        # Pede a modalidade
        modalidade_enum = self.__tela_reserva.selecionar_modalidade(modalidades_do_dia)

        # Descobre quais naipes existem para ESSA modalidade NESSE dia
        naipes_da_modalidade = []
        for ginasio in self.__ginasios:
            for quadra in ginasio.obter_quadras_disponiveis():
                if quadra.semana == dia_enum and quadra.modalidade == modalidade_enum:
                    if quadra.naipe not in naipes_da_modalidade:
                        naipes_da_modalidade.append(quadra.naipe)

        # Pede o naipe
        naipe_str = self.__tela_reserva.selecionar_naipe(naipes_da_modalidade)

        # Procura a quadra exata que o usuário acabou de montar
        quadra_encontrada = None
        for ginasio in self.__ginasios:
            for quadra in ginasio.obter_quadras_disponiveis():
                if quadra.semana == dia_enum and quadra.modalidade == modalidade_enum and quadra.naipe == naipe_str:
                    quadra_encontrada = quadra
                    break
            if quadra_encontrada:
                break

        # Lotado e Fila de Espera com Prioridade
        
        vai_para_espera = False
        
        # Define se a atlética precisa ir para a fila (por penalidade ou por lotação)
        if atletica_solicitante.penalidades > 0:
            vai_para_espera = True
        elif len(quadra_encontrada.reservas) >= 3:
            vai_para_espera = True

        if vai_para_espera:
            nova_espera = ListaEspera(0) # Posição temporária, será recalculada
            
            if atletica_solicitante.penalidades > 0:
                # É punida? Vai para o fim ABSOLUTO da lista
                quadra_encontrada.espera.append(atletica_solicitante)
                quadra_encontrada.lista_espera.append(nova_espera)
            else:
                # É limpa, mas a quadra está lotada
                idx_insercao = len(quadra_encontrada.espera)
                
                # Procura o primeiro penalizado na fila
                for i, atl in enumerate(quadra_encontrada.espera):
                    if atl.penalidades > 0:
                        idx_insercao = i # Descobriu onde começam os penalizados
                        break
                
                # Insere a atlética limpa logo ANTES do primeiro penalizado
                quadra_encontrada.espera.insert(idx_insercao, atletica_solicitante)
                quadra_encontrada.lista_espera.insert(idx_insercao, nova_espera)
                
            atletica_solicitante.listas_espera.append(nova_espera)
            
            # Recalcula e atualiza a posição de TODA A FILA (Posição 1, 2, 3...)
            for i, item_espera in enumerate(quadra_encontrada.lista_espera, start=1):
                item_espera.posicao_lista = i
                
            # Mostra a mensagem com a posição final correta
            posicao_final = nova_espera.posicao_lista
            if atletica_solicitante.penalidades > 0:
                self.__tela_reserva.mostrar_mensagem(
                    f"AVISO: A atlética {atletica_solicitante.nome} possui penalidades. "
                    f"Ela foi jogada para o FIM GERAL da lista de espera (Posição {posicao_final})."
                )
            else:
                self.__tela_reserva.mostrar_mensagem(
                    f"Quadra lotada (3/3). A atlética {atletica_solicitante.nome} entrou na lista de espera (Posição {posicao_final})."
                )
                
        else:
            # Tudo certo: Sem penalidade e com vaga disponível
            nova_reserva = Reserva(atletica_solicitante, modalidade_enum, naipe_str, quadra_encontrada, dia_enum)
            quadra_encontrada.reservas.append(nova_reserva)
            atletica_solicitante.reservas.append(nova_reserva)
            
            vagas_restantes = 3 - len(quadra_encontrada.reservas)
            self.__tela_reserva.mostrar_mensagem(f"Sucesso! Reserva confirmada. Restam {vagas_restantes} vaga(s) nesta quadra.")
    def cancelar_reserva(self, atletica_solicitante):
        # Pede para a tela mostrar as reservas da atlética logada
        reserva_cancelar = self.__tela_reserva.listar_e_selecionar_reserva(atletica_solicitante.reservas)
        
        if not reserva_cancelar:
            return # Usuário desistiu de cancelar ou não tem reservas
            
        quadra = reserva_cancelar.quadra

        # Remove a reserva das listas
        quadra.reservas.remove(reserva_cancelar)
        atletica_solicitante.reservas.remove(reserva_cancelar)
        reserva_cancelar.status = "Cancelada"
        
        self.__tela_reserva.mostrar_mensagem(f"Reserva de {reserva_cancelar.semana.value} cancelada com sucesso!")

        # Redistribuição automática para a Lista de Espera
        self.__processar_fila_espera(quadra)

    def __processar_fila_espera(self, quadra):
        # Fica tentando preencher a vaga enquanto houver gente na fila e vagas na quadra
        while len(quadra.reservas) < 3 and len(quadra.espera) > 0:
            
            # Puxa o primeiro da fila
            proxima_atletica = quadra.espera.pop(0)
            item_lista_espera = quadra.lista_espera.pop(0)
            
            # Remove o objeto ListaEspera do histórico da atlética
            if item_lista_espera in proxima_atletica.listas_espera:
                proxima_atletica.listas_espera.remove(item_lista_espera)

            # Notifica e pergunta se a atlética quer assumir a vaga
            aceitou = self.__tela_reserva.solicitar_aceite_vaga(
                proxima_atletica.nome, 
                quadra.semana.value, 
                quadra.modalidade.value
            )

            if aceitou:
                nova_reserva = Reserva(proxima_atletica, quadra.modalidade, quadra.naipe, quadra, quadra.semana)
                quadra.reservas.append(nova_reserva)
                proxima_atletica.reservas.append(nova_reserva)
                self.__tela_reserva.mostrar_mensagem(f"Vaga preenchida! A atlética {proxima_atletica.nome} assumiu a quadra.")
            else:
                self.__tela_reserva.mostrar_mensagem(f"A atlética {proxima_atletica.nome} recusou a vaga. Passando para o próximo da fila...")
                
        # Atualiza a posição de quem sobrou na fila de espera
        for i, item_espera in enumerate(quadra.lista_espera, start=1):
            item_espera.posicao_lista = i

    def visualizar_disponibilidade(self):
        cronograma_formatado = {}
        
        for ginasio in self.__ginasios:
            for quadra in ginasio.obter_quadras_disponiveis():
                dia = quadra.semana.value
                
                # Inicializa a lista para o dia, se ainda não existir
                if dia not in cronograma_formatado:
                    cronograma_formatado[dia] = []
                
                # Calcula a lotação e fila de espera
                vagas_ocupadas = len(quadra.reservas)
                tamanho_fila = len(quadra.espera)
                
                status_lotacao = f"{vagas_ocupadas}/3 vagas ocupadas"
                if vagas_ocupadas >= 3:
                    status_lotacao += f" | Fila de Espera: {tamanho_fila} atlética(s)"
                    
                # Formata a linha de exibição
                linha = f"  -> {ginasio.nome}: {quadra.modalidade.value} ({quadra.naipe}) - {status_lotacao}"
                cronograma_formatado[dia].append(linha)
                
        # Envia para a tela mostrar
        self.__tela_reserva.mostrar_disponibilidade(cronograma_formatado)