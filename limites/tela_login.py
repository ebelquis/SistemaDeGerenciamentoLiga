class TelaLogin:
    def solicitar_dados_login(self):
        print("\n--- Login SGLA - UFSC ---")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        return {"email": email, "senha": senha}

    def exibir_mensagem(self, mensagem):
        print(f"\n{mensagem}")