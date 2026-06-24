from entidades.pessoa import Pessoa
from entidades.atletica import Atletica
from datetime import datetime
#import bcrypt

class GestorGeral(Pessoa):    
    def indisponibilizar_quadra(self, quadra, data):
        """Permite marcar quadras como ocupadas para eventos/ feriados."""
        pass

    def CRUD_atletica(self, nome: str):
        """Gerenciamento macro das atléticas vinculadas à UFSC."""
        pass

    def CRUD_gestor_atletica(self, email, nome, senha, tel, atletica, cargo):
        """Atende ao RF11: Gestão de usuários do sistema."""
        pass