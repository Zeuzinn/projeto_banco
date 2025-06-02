from projeto_banco.sistema_bancario.clientes.pessoa_fisica import PessoaFisica
from projeto_banco.sistema_bancario.contas.conta_corrente import ContaCorrente
from itertools import count

gerador_de_numero_pra_conta = count(start = 1) 
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
    cpf = input('CPF (Apenas dígitos):').strip()
    cpf_verificado = _verificar_cpf(cpf, clientes, True)
    if not cpf_verificado:
        return
    
    nome = input('Nome completo: ').title().lstrip()
    data_nascimento = input('Data de nascimento - ex::(03/07/2010): ')

    rua_numero = input('Rua e Número: ')
    cidade = input('Cidade: ').upper()
    estado = input('Estado - ex:(MG): ').upper()
    
    pessoa = PessoaFisica(
        nome, data_nascimento, cpf_verificado, 
        rua_numero, cidade, estado
    )
    
    clientes.append(pessoa)

    """ Cria conta automaticamente para o cliente """
    _criar_conta(pessoa)


def _criar_conta(pessoa):
    numero_conta = next(gerador_de_numero_pra_conta)
    gerar_conta = ContaCorrente(
        pessoa, saldo= 0, numero= numero_conta, 
        agencia= "0537",limite_saque= 500
    )

    pessoa.adicionar_conta(gerar_conta)


def _verificar_cpf(cpf, clientes= None, checar_cpf_existente=False):
    if len(cpf) != 11 or not cpf.isdigit():
        print('CPF inválido! Deve possuir 11 dígitos numéricos.')
        return None

    # Evita duplicidade de CPF
    if checar_cpf_existente:
        for cliente in clientes:
            if cliente.cpf == cpf:
                print("Já existe um cliente com esse CPF!")
                return None

    return cpf


def nova_conta(clientes):
    """ Cria uma nova conta para um CPF existente """
    cpf = input('Digite seu CPF: ').strip()
    cpf_verificado = _verificar_cpf(cpf, clientes)
    if not cpf_verificado:
        return

    for cliente in clientes:
        if cliente.cpf == cpf_verificado:            
            numero_conta = next(gerador_de_numero_pra_conta)

            nova_conta = ContaCorrente(
                cliente, saldo= 0, numero= numero_conta, 
                agencia = "0537", limite_saque = 500
            )
            cliente.adicionar_conta(nova_conta)
            return
        
    print('CPF não encontrado. Cliente não cadastrado.')

  
def deposito(clientes):
    """ Efetua depósitos na conta do CPF inserido """
    cpf = input('Digite o CPF do titular da conta (apenas números):').strip()
    cpf_verificado = _verificar_cpf(cpf, clientes)

    if not cpf_verificado:
        print("CPF não encontrado.")
        return
    
    # Verifica se o CPF está na lista de clientes
    for cliente in clientes:
        if cliente.cpf == cpf_verificado:
            if not cliente.contas:
                print("Cliente não possui nenhuma conta.")
                return
            
            # Exibe contas do titular do CPF
            print("\n=== Contas disponíveis ===\n")
            for conta in cliente.contas:
                print(f"Agência: {conta._agencia} | Nº: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
            
            try:
                print()
                print('='*30)
                numero = int(input("Número da conta para depósito: "))
            except ValueError:
                print('Erro: Digite apenas o número da conta')
                return
            
            # Busca conta através do número
            conta_encontrada = _buscar_conta_por_numero(cliente, numero)

            if conta_encontrada:
                try: 
                    valor = float(input('Valor para depósito R$'))
                    conta_encontrada.depositar(valor)
                except ValueError:
                    print('Erro: Você precisa digitar um valor numérico.')
            else:
                print("Conta não encontrada.")
            return


def saque(clientes):
    """ Efetua saques na conta do CPF inserido """
    cpf = input('Digite o CPF do titular da conta (apenas números):').strip()
    cpf_verificado = _verificar_cpf(cpf, clientes)

    if not cpf_verificado:
        print("CPF não encontrado.")
        return
    
    for cliente in clientes:
        if cliente.cpf == cpf_verificado:
            if not cliente.contas:
                print("Cliente não possui nenhuma conta.")
                return
            
            print("\n=== Contas disponíveis ===\n")
            for conta in cliente.contas:
                print(f"Agência: {conta._agencia} | Nº: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
            
            try:
                print()
                print('='*30)
                numero = int(input("Número da conta para saque: "))
            except ValueError:
                print('Erro: Digite apenas o número da conta')
                return
            
            conta_encontrada = _buscar_conta_por_numero(cliente, numero)
                
            if conta_encontrada:
                try: 
                    valor = float(input('Valor para saque R$'))
                    conta_encontrada.sacar(valor)
                except ValueError:
                    print('Erro: Você precisa digitar um valor numérico.')
            else:
                print("Conta não encontrada.")
            return


def extrato(clientes):
    cpf = input('Digite o CPF do titular da conta (apenas números):').strip()
    cpf_verificado = _verificar_cpf(cpf, clientes)
    
    if not cpf_verificado:
        print("CPF não encontrado.")
        return
    
    for cliente in clientes:
        if cliente.cpf == cpf_verificado:
            if not cliente.contas:
                print("Cliente não possui nenhuma conta.")
                return
        
            print("\n=== Contas disponíveis ===\n")
            for conta in cliente.contas:
                print(f"Agência: {conta._agencia} | Nº: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
            
            try:
                print()
                print('='*30)
                numero = int(input("Digite o número da conta que deseja ver o extrato: "))
            except ValueError:
                print("Erro: Digite um número válido para a conta.")
                return
            
            conta_escolhida = _buscar_conta_por_numero(cliente, numero)
            
            """ Exibe o extrato da conta escolhida """
            if conta_escolhida:
                conta_escolhida.exibir_extrato()
            else:
                print("Conta não encontrada.")
            return


def listar_clientes(clientes):
    if not clientes:
        print("Não possui nenhum clientes.")
        return
    
    print("\n=== LISTA DE CLIENTES ===")
    for i, cliente in enumerate(clientes, 1):
        print(f"\nCliente {i}:")
        cliente.mostrar_clientes()


def _buscar_conta_por_numero(cliente, numero):
    for conta in cliente.contas:
        if conta._numero == numero:
            return conta
    return None


def main():
    while True:
        menu()
        opcao = input('Escolha uma operação: ')
        print('='*30)
        if opcao == '1':
            cadastrar_cliente(clientes)
        elif opcao == '2':
            nova_conta(clientes)
        elif opcao == '3':
            deposito(clientes)
        elif opcao == '4':
            saque(clientes)
        elif opcao == '5':
            extrato(clientes)
        elif opcao == '6':
            listar_clientes(clientes)
        elif opcao == '0':
            print('Encerrando sistema...')
            break
        else:
            print('Operação inválida')
        