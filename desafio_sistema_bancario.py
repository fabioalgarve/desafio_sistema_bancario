#criar 2 funções - cadastrar usuário e criar conta corrente e vincular com o cliente.
#as opções serão funções
#função saque recebe argumentos por nome (keywird only)
#função depósito recebe argumentos por posição
# função extrato recebe argumentos por keyword e posição)
# argumentos posicionais: saldo - argumentos nomeados: extrato
# criar usuário: armazena em lista (nome, nascimento, cpf e endereço (str formato logradouro, nro - bairro - cidade/sigla estado.)) - proibido cadastrar 2 cpf iguais
# criar conta em uma lista (agencia, numero conta, usuario), numero conta é sequêncial, iniciando em 1, numero da agencia é fixo 0001. Um usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuario
import textwrap

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

def menu():
   menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [nu] Novo cliente
    [q] Sair

    => """ 
   return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com o CPF mencionado")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados =[usuario for usuario in usuarios if usuarios["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF do cliente (sem pontos): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("Conta criado com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" + 100)
        print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques= LIMITE_SAQUES,
            )
            

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao =="nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "q":
            break
        
        elif opcao =="lc":
            listar_contas(contas)

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()