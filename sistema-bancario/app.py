from funcoes import menu, depositar, sacar, exibir_extrato

saque_diario = 3
saldo = 0
extrato = []
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
    elif opcao == '0':
        print('Encerrando o programa... Até logo!')
        break
    else:
        print('Operação inválida! Escolha outra operação.')