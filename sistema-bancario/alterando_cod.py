from abc import ABC, abstractmethod


class Cliente(ABC):
    def __init__(self, rua_numero: str, cidade: str, estado: str):
        self.rua_numero = rua_numero
        self.cidade = cidade
        self.estado = estado
        self.contas = []

    def realizar_transacao(self, conta):
        ...

    @abstractmethod
    def adicionar_conta(self, conta): 
        pass
    
    @abstractmethod
    def mostrar_clientes(self):
        pass


class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, rua_numero: str, cidade: str, estado: str):
        
        super().__init__(rua_numero, cidade, estado)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = self.verificar_cpf(cpf)

    def verificar_cpf(self, cpf: str):
        if not cpf.isdigit() or len(cpf) != 11:
            print('CPF inválido. O CPF deve possuir 11 dígitos \n')
            return None
        return cpf

    def adicionar_conta(self, conta): 
        self.contas.append(conta)
        print('Conta criada!')

    def mostrar_clientes(self):
        for c in self.contas:
            print(f"Nome: {self.nome} - CPF: {self.cpf} | \nAgência: {c._agencia} - Saldo R$:{c._saldo:,.2f}")
            print()
            
    def __str__(self):
        return  f"Nome: {self.nome} - CPF: {self.cpf} | Cidade/Estado: {self.cidade}, {self.estado}"


class Conta(ABC):
    def __init__(self, cliente: Cliente, saldo: float, numero: int, agencia: str):
        self._cliente = cliente    
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia        
        self._extrato = []
    
    def saldo(self) -> float: 
        return self._saldo
    
    @abstractmethod
    def depositar(self, valor: float):
        pass
        
    @abstractmethod    
    def sacar(self, valor: float):
        pass

    def __str__(self):
        return f"\nAgência: {self._agencia} | Nº: {self._numero} | Saldo: {self.saldo()}"


class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, saldo : float, numero: int, agencia: str, limite: float):
        super().__init__(cliente, saldo, numero, agencia)
        self._limite = limite


    def depositar(self, valor: float):
        if valor <= 0:
            print('O depósito deve ser maior que R$0,00')
            return self._saldo  
        else:
            self._saldo += valor
            self._extrato.append({'valor': +valor})
            print('Processando...')
            print(f'{self._cliente.nome} seu depósito efetuado com sucesso!\n')
            return self._saldo
    
    def sacar(self, valor: float):
        if valor > self._limite:
            print('Processando...')
            print(f'Saque negado! O valor deve ser menor ou igual a R${self._limite} \n')
        
        elif valor > self._saldo:
            print('Processando...')
            print('Saldo indisponível.\n')

        else:
            self._saldo -= valor
            self._extrato.append({'valor':-valor})
            print('Processando...')
            print('Saque realizado com sucesso!\n')
        return self._saldo

    def exibir_extrato(self):
        if not self._extrato:
            print('Você não realizou nenhuma movimentação.')
        else:
            print('\n=== EXTRATO ===\n')
            for ex in self._extrato:
                print(f"R${ex['valor']:,.2f}")
        print(f'\n{self._cliente.nome} - Saldo: R${self._saldo:,.2f}')



pessoa = PessoaFisica('Ingrid Alves', '21-11-2002','12345678911','Antônio Padeiro, nº 15', 'Campo Grande', 'SP')
pessoa2 = PessoaFisica('Robson de Souza', '07-07-1970','00033344470','Rua 7, nº 70', 'Jalapão', 'TO')

conta = ContaCorrente(pessoa, 100, 1, "0137", 200)
conta2 = ContaCorrente(pessoa2, 70, 70, "0137", 500)



# Add Conta dentro da lista de contas
pessoa.adicionar_conta(conta)
pessoa2.adicionar_conta(conta2)
print()

conta.depositar(200)
conta.sacar(430)
conta.depositar(300)
conta.sacar(130)

conta2.depositar(700)
conta2.sacar(900)
conta2.depositar(70)
conta2.sacar(450)

pessoas = [pessoa, pessoa2]
contas = [conta, conta2]


# Exibe a lista de clientes
for pessoa in pessoas:
    pessoa.mostrar_clientes()

for conta in contas:
    conta.exibir_extrato()



""" Interface """
def nova_conta():
        nome = input('Nome completo:').title()
        idade = int(input('Idade: '))
        cpf = input('CPF: ')
        
        rua = input('Rua e nº: ')
        cidade = input('Cidade: ')
        estado = input('Estado(sigla): ')
