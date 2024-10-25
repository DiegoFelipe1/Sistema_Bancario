menu = '''
=========================================
        Bem vindo ao banco XPTO

Por favor digite uma das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[4] sair

Sua opção é: '''

saldo_lista = 0
limite = 500
extrato_lista = []
numero_saques = 0
LIMITE_SAQUES = 3

def saldo():
    print(f'Seu saldo atual é R$ {saldo_lista:.2f}')

def deposito():
    global saldo_lista
    print('\nDeposito')
    deposito = float(input('Por favor, digite o valor que deseja depositar: '))
        
    if deposito > 0:
        extrato_lista.append(deposito)
        saldo_lista += deposito
        print(f'Deposito efetuado com sucesso!!!')
        saldo()
    else:
        print('Deposito falhou!!! Digite uma informação valida de deposito.')

def saque(saque_cliente):
    global saldo_lista, LIMITE_SAQUES, numero_saques
    
    sem_saldo = saldo_lista < saque_cliente
    limite_diario = numero_saques > LIMITE_SAQUES
    limite_de_saque = saque_cliente > limite

    if sem_saldo:
        print('Operação falhou!! Você não possui saldo na sua conta.')
    elif limite_diario:
        print('Operação falhou!! Você excedeu o limite diario para saque.')
    elif limite_de_saque:
        print('Operação falhou!! Por favor, digite um valo menor ou igual a R$ 500,00')
    else:
        extrato_lista.append(- saque_cliente)
        numero_saques += 1
        saldo_lista -= saque_cliente
        print(f'Saque efetuado com sucesso!!!')
        saldo()

def extrato():
    print('Extrato\n')
    if extrato_lista:                                                 #condição verificando se a lista EXTRATO esta vazia
        for i in extrato_lista:
            print(f'R$ {i:.2f}')           
        saldo()
    else:
        print('Não foram realizadas movimentações.')
        saldo()
    
while True:

    opcao = input((menu))

    if opcao == '1':
        deposito()
    elif opcao == '2':
        saque_cliente = (float(input(f'Por favor, digite o valor de saque: ')))
        saque(saque_cliente)
    elif opcao == '3':
        extrato()

    elif opcao == '4':
        break
    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')
    