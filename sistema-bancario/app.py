from operacoes_bancarias import menu, depositar, sacar, exibir_extrato
from cadastros import criar_usuario, criar_conta, listar_contas


saque_diario = 3
AGENCIA = "0001"
saldo = 0
extrato = []
usuarios = []
contas = []


while True:
    menu()
    opcao = input('Escolha uma operação: ')
    print()

    if opcao == '1':
        saldo = depositar(saldo, extrato)
    
    elif opcao == '2':
        saldo, saque_diario = sacar(saldo, saque_diario, extrato)
    
    elif opcao == '3':
        exibir_extrato(extrato, saldo)
    
    elif opcao == '4':
        numero_conta = len(contas)+1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        if conta:
            contas.append(conta)
    
    elif opcao == '5':
        criar_usuario(usuarios)

    elif opcao == '6':
        listar_contas(contas)
    
    elif opcao == '0':
        print('Encerrando o programa... Até logo!')
        break
    
    else:
        print('Operação inválida! Escolha outra operação.')