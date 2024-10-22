menu = '''
=========================================
        Bem vindo ao banco XPTO

Por favor digite uma das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[4] sair

Sua opção é: '''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input((menu))

    if opcao == '1':
        print('\nDeposito')
        deposito = float(input('Por favor, digite o valor que deseja depositar: '))

        if deposito > 0:
            extrato.append(deposito)
            saldo += deposito
            print(f'Deposito efetuado com sucesso!!! Seu saldo é R$ {saldo:.2f}')
        else:
            print('Deposito falhou!!! Digite uma informação valida de deposito.')
    elif opcao == '2':
        print('Saque')
        print(f'Seu saldo é R$ {saldo:.2f}')
        saque = float(input('Digite o valor que deseja sacar: '))

        if numero_saques < LIMITE_SAQUES and saque <= limite and saque > 0:
            if saque <= saldo:
                saldo -= saque
                numero_saques += 1
                extrato.append(-saque)
                print(f'Saque efetuado com sucesso!!! Seu saldo é R$ {saldo:.2f}.')
            else:
                print('Não foi possivel realizar o saque devido a saldo insuficiente')
        else:
            print('Não foi possivel realizar seu saque!!')

    elif opcao == '3':
        print('Extrato\n')
        if extrato:                                                 #condição verificando se a lista EXTRATO esta vazia
            for i in extrato:
                print(f'R$ {i}')
            
            print(f'Seu saldo atual é R$ {saldo:.2f}')
        else:
            print('Não foram realizadas movimentações.')
            print(f'Seu saldo atual é {saldo:.2f}')

    elif opcao == '4':
        break
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')
    