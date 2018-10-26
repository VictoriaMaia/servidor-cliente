def TelaLogin(clasCli):
    while True:
        login = input("Login: ")
        senha = input("Senha: ")
        dados = login + ":" + senha
        clasCli.enviarRequisicao(dados)
        data = clasCli.recebeResposta() 
        if data == ".":            
            return
        else:
            print(data)