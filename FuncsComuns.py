def TelaLogin(clasCli, tipo):
    while True:
        login = input("Login: ")
        senha = input("Senha: ")
        dados = login + ":" + senha + ":" + tipo
        clasCli.enviarRequisicao(dados)
        data = clasCli.recebeResposta() 
        if data == ".":            
            return
        else:
            print(data)