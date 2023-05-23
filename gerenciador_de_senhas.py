import json

senha_mestre = 'mpe123'
cofres = {}


def login():
    print("Sócrates e Luiz Guilherme")
    senha1 = input("Insira a senha de acesso: ")
    if senha1 != senha_mestre:
        print("Não é possível fazer login sem a senha mestre.")
        return False
    return True


def menu():
    print("Gerenciador de Senhas")
    print("---------------------------------")
    print("1 --> Criar novo cofre.")
    print("2 --> Mostrar cofres existentes.")
    print("3 --> Cadastrar uma nova descrição.")
    print("4 --> Listar todas as descrições salvas.")
    print("5 --> Atualizar uma descrição.")
    print("6 --> Apagar uma descrição.")
    print("---------------------------------")
    operador = int(input("Escolha a operação -->: "))
    return operador


def criar_novo_cofre():
    nome_cofre = input("Digite o nome do novo cofre: ")
    cofre = {"descrições": {}}
    cofres[nome_cofre] = cofre
    with open(nome_cofre + ".json", "w") as f:
        json.dump(cofre, f)
    print("Novo cofre criado com sucesso!")


def mostrar_cofres_existentes():
    if not cofres:
        print("Não existem cofres criados no momento.")
    else:
        print("--> Cofres Existentes <--")
        for nome_cofre in cofres:
            print(nome_cofre)
        print("-------------------------")


def cadastrar_nova_descricao():
    if not cofres:
        print("Não existem cofres criados no momento.")
        return

    mostrar_cofres_existentes()
    nome_cofre = input("Digite o nome do cofre onde deseja cadastrar a descrição: ")
    if nome_cofre in cofres:
        descricao = input("Descrição da plataforma: ")
        if descricao in cofres[nome_cofre]["descrições"]:
            print("Essa descrição já existe no cofre.")
        else:
            login = input("Login: ")
            senha = input("Senha: ")
            if login and senha:
                cofres[nome_cofre]["descrições"][descricao] = {"Login": login, "Senha": senha}
                with open(nome_cofre + ".json", "w") as f:
                    json.dump(cofres[nome_cofre], f)
                print("Nova descrição cadastrada com sucesso!")
            else:
                print("Não é possível cadastrar uma descrição sem login ou senha.")
    else:
        print("Cofre não encontrado.")


def listar_descricoes_salvas():
    if not cofres:
        print("Não existem cofres criados no momento.")
        return

    nome_cofre = input("Digite o nome do cofre que deseja listar as descrições: ")
    if nome_cofre in cofres:
        cofre = cofres[nome_cofre]
        if cofre["descrições"]:
            print("--> Descrições Salvas <--")
            for descricao, dados in cofre["descrições"].items():
                print("Plataforma:", descricao)
                print("Login:", dados["Login"])
                print("Senha:", dados["Senha"])
                print("-------------------------")
        else:
            print("O cofre não possui nenhuma descrição cadastrada.")
    else:
        print("Cofre não encontrado.")


def atualizar_descricao():
    if not cofres:
        print("Não existem cofres criados no momento.")
        return

    mostrar_cofres_existentes()
    nome_cofre = input("Digite o nome do cofre onde deseja atualizar a descrição: ")
    if nome_cofre in cofres:
        cofre = cofres[nome_cofre]
        descricao = input("Digite a descrição da plataforma que deseja atualizar: ")
        if descricao in cofre["descrições"]:
            print("--> Dados atuais <--")
            print("Descrição:", descricao)
            print("Login:", cofre["descrições"][descricao]["Login"])
            print("Senha:", cofre["descrições"][descricao]["Senha"])
            print("--------------------")
            print("Digite o novo login:")
            login = input("Login: ")
            senha = input("Senha: ")
            cofre["descrições"][descricao]["Login"] = login
            cofre["descrições"][descricao]["Senha"] = senha
            with open(nome_cofre + ".json", "w") as f:
                json.dump(cofre, f)
            print("Descrição atualizada com sucesso!")
        else:
            print("A descrição da plataforma não foi encontrada.")
    else:
        print("Cofre não encontrado.")


def apagar_descricao():
    if not cofres:
        print("Não existem cofres criados no momento.")
        return

    mostrar_cofres_existentes()
    nome_cofre = input("Digite o nome do cofre onde deseja apagar a descrição: ")
    if nome_cofre in cofres:
        cofre = cofres[nome_cofre]
        descricao = input("Digite a descrição da plataforma que deseja apagar: ")
        if descricao in cofre["descrições"]:
            del cofre["descrições"][descricao]
            with open(nome_cofre + ".json", "w") as f:
                json.dump(cofre, f)
            print("Descrição apagada com sucesso!")
        else:
            print("A descrição da plataforma não foi encontrada.")
    else:
        print("Cofre não encontrado.")


while True:
    if not login():
        break

    op = menu()

    if op == 1:
        criar_novo_cofre()
    elif op == 2:
        mostrar_cofres_existentes()
    elif op == 3:
        cadastrar_nova_descricao()
    elif op == 4:
        listar_descricoes_salvas()
    elif op == 5:
        atualizar_descricao()
    elif op == 6:
        apagar_descricao()

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        print("Encerrando o programa. Sócrates e Luiz Guilherme agradecem.")
        break
