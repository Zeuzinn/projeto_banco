from pessoa_fisica import PessoaFisica
from conta_corrente import ContaCorrente
from interface import Deposito, Saque

clientes = []

def menu():
    print('\n=== BIG BANK ===\n')
    print('[1] - Criar cliente')
    print('[2] - Criar nova conta (apenas com CPF existente)')
    print('[3] - Depositar/ Sacar')
    print('[4] - Extrato')
    print('[5] - Listar clientes')


def cadastrar_cliente (clientes):
    cpf = input('CPF (Apenas dígitos):')
    cpf_verificado = verificar_cpf(cpf)
    if not cpf_verificado:
        return
    
    nome = input('Nome completo: ').title().lstrip()
    data_nascimento = input('Data de nascimento - ex::(03/07/2010): ')

    rua_numero = input('Rua e Número: ')
    cidade = input('Cidade: ')
    estado = input('Estado - ex:(MG): ')
    pessoa = PessoaFisica(nome, data_nascimento, cpf_verificado, rua_numero, cidade, estado)
    clientes.append(pessoa)
    criar_conta(pessoa)


def criar_conta(pessoa):
    gerar_conta = ContaCorrente(pessoa, saldo= 0, numero= 1, agencia= "0537",limite_saque= 500)
    pessoa.adicionar_conta(gerar_conta)


def verificar_cpf(cpf):
    if len(cpf) != 11:
        print('CPF INVÁLIDO, DEVE POSSUIR 11 CARACTERES')
        return
    return cpf


def nova_conta(clientes):
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
    cpf = input('Digite seu CPF: ')
    cpf_verificado = verificar_cpf(cpf)
    if not cpf_verificado:
        return
    
    for cliente in clientes:
        if cliente.cpf == cpf_verificado:
            if not cliente.contas:
                print("Cliente não possui nenhuma conta.")
                return
            
            print("Contas disponíveis:")
            for i, conta in enumerate(cliente.contas):
                print(f"[{i}] Agência: {conta._agencia} | Nº: {conta._numero} | Saldo: R$ {conta._saldo:.2f}")
            return

    print("CPF não encontrado.")



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
        elif opcao == '4':...
        elif opcao == '5':...
        

if __name__ == "__main__":
    main()