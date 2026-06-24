from limites.tela_login import TelaLogin

class ControladorLogin:
    def __init__(self, lista_usuarios):
        self.__tela_login = TelaLogin()
        self.__usuarios = lista_usuarios 
        self.__usuario_logado = None

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    def realizar_login(self):
        dados = self.__tela_login.solicitar_dados_login()
        email_digitado = dados["email"]
        senha_digitada = dados["senha"]

        for usuario in self.__usuarios:
            # Chama o método login da classe Pessoa
            if usuario.login(email_digitado, senha_digitada):
                self.__usuario_logado = usuario
                self.__tela_login.exibir_mensagem(f"Login realizado com sucesso! Bem-vindo(a), {usuario.nome}.")
                return usuario
        
        # Se percorrer toda a lista e não encontrar correspondência
        self.__tela_login.exibir_mensagem("Erro: Email ou senha incorretos. Tente novamente.")
        return None
        
    def realizar_logout(self):
        if self.__usuario_logado:
            nome = self.__usuario_logado.nome
            self.__usuario_logado = None
            self.__tela_login.exibir_mensagem(f"Logout de {nome} realizado com sucesso.")
        else:
            self.__tela_login.exibir_mensagem("Nenhum usuário logado no momento.")