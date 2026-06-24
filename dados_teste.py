# dados_teste.py
from entidades.atletica import Atletica
from entidades.membro_atletica import MembroAtletica
from entidades.gestor_geral import GestorGeral
from entidades.gestor_atletica import GestorAtletica
from entidades.ginasio import GinasioFixo
from entidades.quadra import Quadra
from entidades.enums import Semana, Modalidades

def carregar_dados_iniciais():
    eng = Atletica("Engenharia UFSC")
    med = Atletica("Medicina UFSC")
    arq = Atletica("Arquitetura UFSC")
    cce = Atletica("Computação UFSC")
    odo = Atletica("Odontologia UFSC")
    
    dir = Atletica("Direito UFSC")
    dir.penalidades = 1

    atleticas = [eng, med, dir, arq, cce, odo]

    # Gestor Geral do CDS
    gestor_geral = GestorGeral("Kayo (Gestor Geral Liga)", "gestor@ufsc.br", "admin123", "4888888888")

    # Gestores de Atlética (Têm acesso ao botão de cadastrar membros)
    gestor_eng = GestorAtletica("Carlos (Gestor Eng)", "gestor.eng@ufsc.br", "senha123", "4891111111", eng, "Presidente")
    gestor_med = GestorAtletica("Ana (Gestora Med)", "gestor.med@ufsc.br", "senha123", "4892222222", med, "Diretora de Esportes")

    # Membros Comuns (Apenas reservam e denunciam)
    membro_eng = MembroAtletica("João (Membro Eng)", "membro.eng@ufsc.br", "senha123", "4893333333", eng, "Atleta Vôlei")
    membro_dir = MembroAtletica("Pedro (Membro Dir)", "membro.dir@ufsc.br", "senha123", "4894444444", dir, "Atleta Futsal")
    membro_cce = MembroAtletica("Lucas (Membro Comp)", "membro.cce@ufsc.br", "senha123", "4895555555", cce, "Treinador")

    usuarios = [gestor_geral, gestor_eng, gestor_med, membro_eng, membro_dir, membro_cce]

    #ginasios
    ginasio_maior = GinasioFixo("Ginásio Maior CDS", [Modalidades.VOLEI, Modalidades.HANDEBOL, Modalidades.FUTSAL])
    ginasio_menor = GinasioFixo("Ginásio Menor CDS", [Modalidades.FUTSAL, Modalidades.BASQUETE])

    # SEGUNDA-FEIRA
    ginasio_maior.adicionar_quadra(Quadra(Semana.SEGUNDA, Modalidades.VOLEI, "Masculino"))
    ginasio_maior.adicionar_quadra(Quadra(Semana.SEGUNDA, Modalidades.VOLEI, "Feminino"))
    ginasio_menor.adicionar_quadra(Quadra(Semana.SEGUNDA, Modalidades.FUTSAL, "Feminino"))

    # TERÇA-FEIRA
    ginasio_maior.adicionar_quadra(Quadra(Semana.TERCA, Modalidades.HANDEBOL, "Masculino"))
    ginasio_menor.adicionar_quadra(Quadra(Semana.TERCA, Modalidades.BASQUETE, "Feminino"))

    # QUARTA-FEIRA
    ginasio_maior.adicionar_quadra(Quadra(Semana.QUARTA, Modalidades.VOLEI, "Masculino"))
    ginasio_maior.adicionar_quadra(Quadra(Semana.QUARTA, Modalidades.VOLEI, "Feminino"))
    ginasio_menor.adicionar_quadra(Quadra(Semana.QUARTA, Modalidades.FUTSAL, "Feminino"))

    # QUINTA-FEIRA
    ginasio_maior.adicionar_quadra(Quadra(Semana.QUINTA, Modalidades.HANDEBOL, "Feminino"))
    ginasio_menor.adicionar_quadra(Quadra(Semana.QUINTA, Modalidades.BASQUETE, "Masculino"))

    # SEXTA-FEIRA
    ginasio_maior.adicionar_quadra(Quadra(Semana.SEXTA, Modalidades.FUTSAL, "Masculino"))
    ginasio_menor.adicionar_quadra(Quadra(Semana.SEXTA, Modalidades.FUTSAL, "Feminino"))

    ginasios = [ginasio_maior, ginasio_menor]

    return atleticas, usuarios, ginasios