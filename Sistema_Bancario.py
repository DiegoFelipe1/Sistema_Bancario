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

def deposito():
    global saldo
    print('\nDeposito')
    deposito = float(input('Por favor, digite o valor que deseja depositar: '))
        
    if deposito > 0:
        extrato.append(deposito)
        saldo += deposito
        print(f'Deposito efetuado com sucesso!!! Seu saldo é R$ {saldo:.2f}')
    else:
        print('Deposito falhou!!! Digite uma informação valida de deposito.')

def saque(saque_cliente):
    global saldo, LIMITE_SAQUES, numero_saques
    print(saldo)

    sem_saldo = saldo < saque_cliente
    limite_diario = numero_saques > LIMITE_SAQUES
    limite_de_saque = saque_cliente > limite

    if sem_saldo:
        print('Operação falhou!! Você não possui saldo na sua conta.')
    elif limite_diario:
        print('Operação falhou!! Você excedeu o limite diario para saque.')
    elif limite_de_saque:
        print('Operação falhou!! Por favor, digite um valo menor ou igual a R$ 500,00')
    else:
        numero_saques += 1
        saldo -= saque_cliente
        print(f'Saque efetuado com sucesso. Seu saldo é R$ {saldo:.2f}')
        print(numero_saques)
    
while True:

    opcao = input((menu))

    if opcao == '1':
        deposito()
    elif opcao == '2':
        saque_cliente = (float(input(f'Por favor, digite o valor de saque: ')))
        saque(saque_cliente)
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
    