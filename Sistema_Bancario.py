import textwrap

def menu():
    menu = '''\n
    =========================================
        Bem vindo ao banco XPTO

    Por favor digite uma das opções abaixo:

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo Usuário
    [5]\tNova Conta
    [6]\tListar Contas
    [7]\tSair

    Sua opção é: '''
    return int(input(textwrap.dedent(menu)))

def depositar(saldo, deposito, extrato, /):
    
    if deposito > 0:
        extrato.append(deposito)
        saldo += deposito
        print(f'\n======== Deposito efetuado com sucesso!!! ========')
        exibir_saldo(saldo)
        return saldo, extrato
    else:
        print('Operação de deposito falhou!!! Digite uma informação valida de deposito.')

def sacar(*, valor, saldo, numero_saques, LIMITE_SAQUES, limite, extrato): # Função keyword only 
    
    sem_saldo = saldo < valor
    limite_diario = numero_saques >= LIMITE_SAQUES
    limite_de_saque = valor > limite

    if sem_saldo:
        print('Operação falhou!! Você não possui saldo na sua conta.')
        return main()
    elif limite_diario:
        print('Operação falhou!! Você excedeu o limite diario para saque.')
        return main()
    elif limite_de_saque:
        print('Operação falhou!! Por favor, digite um valo menor ou igual a R$ 500,00')
        return main()
    elif valor > 0:
        extrato.append(-valor)
        numero_saques += 1
        saldo -= valor
        print(f'Saque efetuado com sucesso!!!')
        return saldo, extrato, numero_saques
    else:
        print('Operação de saque falhou!!! Digite uma informação valida de saque.')

def exibir_extrato(saldo, /, *, extrato):
    
    if extrato:                                                 #condição verificando se a lista EXTRATO esta vazia
        for i in extrato:
            print(f'R$ {i:.2f}')           
        exibir_saldo(saldo)
    else:
        print('Não foram realizadas movimentações.')
        exibir_saldo(saldo)
    
def exibir_saldo(saldo):
    print(f'\nSeu saldo atual é R$ {saldo:.2f}')

def criar_usuario(cliente):
    cpf = input('Por favor, digite seu CPF: ')
    usuario = filtrar_usuario(cpf, cliente)

    if usuario:
        print('Ja existe um usuario com esse CPF')
        return
    
    nome = input('Por favor, digite seu nome completo: ')
    nascimento = input('Por favor, digite a sua data de nascimento (dd-mm-aaaa): ')
    endereço = input('Por favor, digite seu endereço (Rua, numero, bairro, cidade/sigla): ')

    cliente.append({'nome': nome, 'nascimento': nascimento, 'cpf':cpf, 'endereço':endereço})

    print('\nUsario criado com sucesso!!')
    

def filtrar_usuario(cpf, cliente):
    usuario_filtrado = [usuario for usuario in cliente if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None # dar uma olhada a respeito desse codigo

def criar_conta(cliente, agencia, numero_conta,):
    cpf = input('Por favor, digite seu CPF: ')
    usuario = filtrar_usuario(cpf, cliente)

    if usuario:
        print('Conta cadastrada com sucesso!!')
        return({'agencia': agencia, 'conta':numero_conta, 'usuario':usuario})
        
    print('Cliente não encontrado, processo de criação de conta se encerrando')

def listar_contas(conta):
    for contas in conta:
        linha = f'''
        Agência:\t{contas['agencia']}
        C/C:\t{contas['conta']}
        Titular:\t{contas['usuario']['nome']}
        '''
        print(textwrap.dedent(linha))

def main():

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    cliente = []
    conta = []
    AGENCIA = '0001'


    while True:
        
        opcao = menu()

        if opcao == 1: 
            print('\n======== Deposito ========')
            valor = float(input('\nPor favor, digite o valor que deseja depositar: '))
            saldo, extrato = depositar(saldo, valor, extrato )  # retorna os valores da função para a variavel saldo e extrato

        elif opcao == 2:
            print('\n======== Saque ========')
            valor= (float(input(f'Por favor, digite o valor de saque: ')))

            saldo, extrato, numero_saques = sacar(
                valor=valor,
                saldo=saldo,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
                limite=limite,
                extrato=extrato,
            )
        elif opcao == 3:
            print('\n======== Extrato ========')
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            print('\n======== Criação de Usuário ========')
            
            criar_usuario(cliente)

        elif opcao == 5:
            print('\n======== Criação de Conta ========')

            numero_conta = len(conta) + 1
            conta1 = criar_conta(cliente, AGENCIA, numero_conta)

            if conta1:
                conta.append(conta1)

        elif opcao == 6:
            print('\n======== Listando Contas ========')
            listar_contas(conta)
        elif opcao == 7:
            break
        else:
            print('Operação invalida, por favor selecione novamente a operação desejada.')
        
main()