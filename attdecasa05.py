cadastro = []
senha = []

operacao = 0
while operacao != 4:
    print("\nSelecione a operação:\n"
          "1. Cadastro\n"
          "2. Mostrar usuários\n"
          "3. Login\n"
          "4. Sair\n")

    operacao = int(input("Escolha um número: "))

    if operacao == 1:
        while True:
            novo_usuario = input("Digite um nome de usuário para cadastro: ")
            nova_senha = input("Digite uma senha: ")

            if novo_usuario in cadastro:
                print("Usuário já existe!")
            else:
                cadastro.append(novo_usuario)
                senha.append(nova_senha)
                print("Usuário cadastrado com sucesso!")

            continuar = input("Deseja cadastrar outro usuário? (s/n): ")
            if continuar.lower() != 's':
                break

    elif operacao == 2:
        if len(cadastro) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for i, user in enumerate(cadastro):
                print(f"Usuário {i+1}: {user} - Senha: {senha[i]}")


    elif operacao == 3:
        tentativas = 0
        while tentativas < 3:
            login = input("Digite seu login: ")
            password = input("Digite sua senha: ")
            if login in cadastro:
                index = cadastro.index(login)
                if senha[index] == password:
                    print("Login realizado com sucesso!")
                    break
                else:
                    print("Senha inválida!")
            else:
                print("Usuário não cadastrado!")
            tentativas += 1
            if tentativas == 3:
                print("Número máximo de tentativas excedido. Programa encerrado.")
                operacao = 4  # Define para sair do loop principal
                break

    elif operacao == 4:  # Sair
        print("Obrigado por usar o programa!")
        break

    else:
        print("Opção inválida, tente novamente.")


#append = deseja expandir uma lista com novos elementos sem substituir os que já existem
#enumerate = ele mostra o indice quanto o valor de cada item mais facil sem precisar aumentar o cod
#.index = encontra a posição do login dentro da lista cadastro. n preciso fazer por parte (senha==cadastradasenha) e login
