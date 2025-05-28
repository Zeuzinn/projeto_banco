from registro import obter_data_e_hora

def criar_usuario(usuarios): 
    """ Solicita dados do usuário e adiciona um novo cliente se o CPF não existir. """
    
    cpf = input('Informe o CPF(apenas números): ')
    cpf_verificado = verificar_cpf(cpf)
    if not cpf_verificado:
        print("CPF inválido. Cadastro cancelado.\n")
        return 
    
    usuario = filtrar_cliente(cpf_verificado, usuarios)
    if usuario:
        print("\nJá existe cliente com esse CPF!")
        return
    
    nome = input('Nome: ').title()
    data_nascimento = input('Data de nascimento: ')
    rua = input('Informe a Rua e Número: ')
    bairro = input('Informe o Bairro: ')
    cidade = input('Informe a Cidade e Estado: ')
    hora, data = obter_data_e_hora()
    usuarios.append({
        'nome': nome, 
        'cpf': cpf_verificado, 
        'data_nascimento': data_nascimento, 
        'rua': rua, 
        'bairro': bairro, 
        'cidade': cidade, 
        'hora': hora, 
        'data': data
    })   
    print('Cliente cadastrado!\n')
        

def filtrar_cliente(cpf, usuarios):
    """ Filtro a partir do CPF """
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    """ Solicita o CPF do usuário para poder criar uma conta, caso contrário não cria. """
    
    cpf = input('Informe o CPF (apenas números): ')
    cpf_verificado = verificar_cpf(cpf)
    
    if not cpf_verificado:
        print("CPF inválido. Criação da conta cancelada.\n")
        return
    
    usuario = filtrar_cliente(cpf_verificado, usuarios)
    if usuario:
        print("Conta criada com sucesso!\n")
        return {
        "agencia": agencia, \
        "numero_conta": numero_conta, \
        "usuario": usuario
    }
    

def listar_contas(contas): 
    if not contas:
        print('Não há contas no momento...\n')
    else:
        print('=== CONTAS ===\n')
        for conta in contas:
            titular = conta['usuario']['nome']
            agencia = conta['agencia']
            numero_da_conta = conta['numero_conta']
            data = conta['usuario']['data']
            print(f"Titular: {titular} | Agência: {agencia} | Conta: {numero_da_conta} | Criada: {data} \n")


def verificar_cpf(cpf):
    """ Criar um sistema robusto para verificar CPF. """

    if not cpf.isdigit() or len(cpf) != 11:
        print('CPF inválido. \n')
        return None
    return cpf

