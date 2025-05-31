from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente


clientes = []

def menu():
    print('='*30)
    print('=== BIG BANK - MENU ===')
    print('='*30)
    print('[1] - Criar cliente')
    print('[2] - Criar nova conta (apenas com CPF existente)')
    print('[3] - Depositar')
    print('[4] - Sacar')
    print('[5] - Extrato')
    print('[6] - Listar clientes')
    print('[0] - Sair')
    print('='*30)


def cadastrar_cliente (clientes):
    cpf = input('CPF (Apenas dígitos):')
    cpf_verificado = verificar_cpf(cpf)
    if not cpf_verificado:
        return
    
    nome = input('Nome completo: ').title().lstrip()
    data_nascimento = input('Data de nascimento - ex::(03/07/2010): ')

    rua_numero = input('Rua e Número: ')
    cidade = input('Cidade: ').title()
    estado = input('Estado - ex:(MG): ').upper()
    
    pessoa = PessoaFisica(nome, data_nascimento, cpf_verificado, rua_numero, cidade, estado)
    
    clientes.append(pessoa)

    """ APÓS O CADASTRO, CRIA UMA CONTA AUTOMÁTICA PARA O CLIENTE """
    _criar_conta(pessoa)


def _criar_conta(pessoa):
    gerar_conta = ContaCorrente(pessoa, saldo= 0, numero= 1, agencia= "0537",limite_saque= 500)
    pessoa.adicionar_conta(gerar_conta)


def verificar_cpf(cpf):
    """ VERIFICAÇÃO BÁSICA DE CPF """
    if len(cpf) != 11:
        print('CPF inválido!')
        print('CPF deve possui 11 dígitos(apenas números)')
        return
    return cpf


def nova_conta(clientes):
    """ CRIA CONTA PARA UM CPF EXISTENTE """

    cpf = input('Digite seu CPF: ')
    cpf_verificado = verificar_cpf(cpf)
    if not cpf_verificado:
        return

    for cliente in clientes:
        if cliente.cpf == cpf_verificado:
            numero_conta = len(cliente.contas) + 1 

            nova_conta = ContaCorrente(cliente, saldo= 0, numero= numero_conta, agencia= "0537", limite_saque= 500)
            
            cliente.adicionar_conta(nova_conta)
            return
        
    print('CPF não encontrado. Cliente não cadastrado.')

  
def _deposito(clientes):
    """ REALIZA DEPÓSITOS NA CONTA DO TÍTULAR """
    cpf = input('Digite o CPF do titular da conta (apenas números):')
    cpf_verificado = verificar_cpf(cpf)

    if not cpf_verificado:
        print("CPF não encontrado.")
        return
    
    # VERIFICA SE O CPF ESTÁ NA LISTA DE CLIENTES
    for cliente in clientes:
        if cliente.cpf == cpf_verificado:
            if not cliente.contas:
                print("Cliente não possui nenhuma conta.")
                return
            
            # EXIBE AS CONTAS DO TITULAR DO CPF
            print("Contas disponíveis:")
            for i, conta in enumerate(cliente.contas):
                print(f"[{i}] Agência: {conta._agencia} | Nº: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
            
            print("\nDigite o índice da conta que deseja fazer depósito")
            print("Ex: [3] ")
            
            indice = int(input("\nÍndice: "))

            # VERIFICAÇÃO DE SEGURANÇA, EVITA QUE DIGITE UM NÚMERO FORA DA LISTA
            if 0 <= indice < len(cliente.contas):
                conta_escolhida = cliente.contas[indice]
                
                valor = float(input('Valor para depósito R$'))
                conta_escolhida.depositar(valor)

            else:
                print("Índice inválido! Nenhuma conta com esse número.")


def _saque(clientes):
    """ REALIZA SAQUES NA CONTA DO TÍTULAR """

    cpf = input('Digite o CPF do titular da conta (apenas números):')
    cpf_verificado = verificar_cpf(cpf)

    if not cpf_verificado:
        print("CPF não encontrado.")
        return
    
    for cliente in clientes:
        if cliente.cpf == cpf_verificado:
            if not cliente.contas:
                print("Cliente não possui nenhuma conta.")
                return
            
            print("Contas disponíveis:")
            for i, conta in enumerate(cliente.contas):
                print(f"[{i}] Agência: {conta._agencia} | Nº: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
            
            print("\nDigite o índice da conta que deseja realizar saque")
            print("Ex: [3] ")
            
            indice = int(input("\nÍndice: "))
            
            if 0 <= indice < len(cliente.contas):
                conta_escolhida = cliente.contas[indice]

                valor = float(input('Valor para saque R$'))
                conta_escolhida.sacar(valor)

            else:
                print("Índice inválido! Nenhuma conta com esse número.")


def _extrato(clientes):
    cpf = input('Digite o CPF do titular da conta (apenas números):')
    cpf_verificado = verificar_cpf(cpf)
    
    if not cpf_verificado:
        print("CPF não encontrado.")
        return
    
    for cliente in clientes:
        if cliente.cpf == cpf_verificado:
            if not cliente.contas:
                print("Cliente não possui nenhuma conta.")
                return
            
            print("Contas disponíveis:")
            for i, conta in enumerate(cliente.contas):
                print(f"[{i}] Agência: {conta._agencia} | Nº: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
            
            """ EXIBE O EXTRATO DA CONTA ESCOLHIDA """
            print("\nDigite o índice da conta que deseja ver o extrato")
            print("Ex: [3] ")
            
            indice = int(input("\nÍndice: "))
            
            if 0 <= indice < len(cliente.contas):
                conta_escolhida = cliente.contas[indice]
                conta_escolhida.exibir_extrato()    
            else:
                print("Índice inválido!")
            return 


def _listar_clientes(clientes):
    if not clientes:
        print("Não possui nenhum clientes.")
        return
    
    print("\n=== LISTA DE CLIENTES ===")
    for i, cliente in enumerate(clientes, 1):
        print(f"\nCliente {i}:")
        cliente.mostrar_clientes()


def main():
    while True:
        menu()
        opcao = input('Escolha uma operação: ')
        if opcao == '1':
            cadastrar_cliente(clientes)
        elif opcao == '2':
            nova_conta(clientes)
        elif opcao == '3':
            _deposito(clientes)
        elif opcao == '4':
            _saque(clientes)
        elif opcao == '5':
            _extrato(clientes)
        elif opcao == '6':
            _listar_clientes(clientes)
        

if __name__ == "__main__":
    main()