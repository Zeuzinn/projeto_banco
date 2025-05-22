def menu():
    print('\n=== BIG BANK ===\n')
    print('[1] - Depósito')
    print('[2] - Saque')
    print('[3] - Extrato')
    print('[0] - Sair')


def depositar(saldo, extrato):
    deposito = int(input('Digite o valor do depósito R$'))
    if deposito <= 0:
        print('O depósito deve ser maior que R$0,00')
        return saldo  
    else:
        saldo += deposito
        extrato.append(+deposito)
        print('Processando...')
        print(f'Depósito R${deposito:.2f} efetuado com sucesso!')
        return saldo


def sacar(saldo, saque_diario, extrato):
    if saque_diario == 0:
        print('Limite de saque atingido.')
        return saldo, saque_diario
        
    saque = int(input('Valor para saque R$'))
    
    if saque > 500:
        print('Processando...')
        print('Saque negado! O valor deve ser menor ou igual a R$500,00')
    
    elif saque > saldo:
        print('Processando...')
        print('Saldo indisponível.')
        print(f'Saldo atual R${saldo:.2f}')

    else: 
        saldo -= saque
        extrato.append(-saque)
        saque_diario -= 1
        print('Processando...')
        print('Saque realizado!')
        print('Saques disponíveis:', saque_diario)
        return saldo, saque_diario


def exibir_extrato(extrato, saldo):
    if not extrato:
        print('Não foram realizadas nenhuma movimentação.')
    else:
        print('=== TRANSAÇÕES ===')
        for valor in extrato:
            print(f'R${valor:.2f}')
            print()
        print(f'\nSaldo atual: R${saldo:.2f}')