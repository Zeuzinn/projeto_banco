from registro import obter_data_e_hora


def menu():
    print('\n=== BIG BANK ===\n')
    print('[1] - Depósito')
    print('[2] - Saque')
    print('[3] - Extrato')
    print('[4] - Criar Conta')
    print('[5] - Criar Cliente')
    print('[6] - Listar contas')
    print('[0] - Sair')


def depositar(saldo, extrato):
    deposito = int(input('Digite o valor do depósito R$'))
    if deposito <= 0:
        print('O depósito deve ser maior que R$0,00')
        return saldo  
    else:
        saldo += deposito
        hora, dia = obter_data_e_hora()
        extrato.append({'dinheiro': +deposito, 'hora': hora, 'dia': dia})
        print('Processando...')
        print('Depósito efetuado com sucesso!')
        saldo_atual(saldo)
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
        saldo_atual(saldo)

    else:
        saldo -= saque
        hora, dia = obter_data_e_hora()
        extrato.append({'dinheiro': -saque, 'hora': hora, 'dia': dia})
        saque_diario -= 1
        print('Saque realizado com sucesso!')
        print('Saques disponíveis:', saque_diario)
        saldo_atual(saldo)

    return saldo, saque_diario


def exibir_extrato(extrato, saldo):
    if not extrato:
        print('Não foram realizadas nenhuma movimentação.')
    else:
        print('=== TRANSAÇÕES ===')
        for valor in extrato:
            print(f"R${valor['dinheiro']:.2f} \nData: {valor['dia']} \nHora: {valor['hora']}")
            print('-' *30)
        print(f'\nSaldo atual: R${saldo:.2f}')


def saldo_atual(saldo):
    print()
    print(f'Saldo atual R${saldo:.2f}')
    print('-' *30)