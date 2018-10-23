def TelaLogin(clasCli):
    while True:
        login = input("Login: ")
        senha = input("Senha: ")
        dados = login + ":" + senha
        clasCli.enviarRequisicao(dados)
        data = clasCli.recebeResposta()
        print(data)
        if data == "Achei":
            print(clasCli.recebeResposta())
            return