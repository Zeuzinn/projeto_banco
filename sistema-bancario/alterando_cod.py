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
    def __init__(self, nome: str, idade: int, cpf: str, rua_numero: str, cidade: str, estado: str):
        
        super().__init__(rua_numero, cidade, estado)
        self.nome = nome
        self.idade = idade
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
            print(f"Nome: {self.nome} - CPF: {self.cpf} | \nAgência: {c._agencia} - Saldo R$:{c._saldo:.2f}")
            print()
            
    def __str__(self):
        return  f"Nome: {self.nome} - CPF: {self.cpf} | Cidade/Estado: {self.cidade}, {self.estado}"


class Conta:
    def __init__(self, cliente: Cliente, saldo: float, numero: int, agencia: str):
        self._cliente = cliente
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia        

    def saldo(self) -> float: 
        return self._saldo
    
    def depositar(self, valor: float):
        if valor <= 0:
            print('O depósito deve ser maior que R$0,00')
            return self._saldo  
        else:
            self._saldo += valor
            # hora, dia = obter_data_e_hora()
            # extrato.append({'dinheiro': +deposito, 'hora': hora, 'dia': dia})
            print('Processando...')
            print('Depósito efetuado com sucesso!')
            return self._saldo
        
    def sacar(self, valor: float):
        if valor > 500:
            print('Processando...')
            print('Saque negado! O valor deve ser menor ou igual a R$500,00')
        
        elif valor > self._saldo:
            print('Processando...')
            print('Saldo indisponível.')

        else:
            self._saldo -= valor
            """ Criar classe EXTRATO para ter histórico de transações """
            
            # hora, dia = obter_data_e_hora()
            # extrato.append({'dinheiro': -valor, 'hora': hora, 'dia': dia})
            
            print('Saque realizado com sucesso!')
        return self._saldo

    def __str__(self):
        return f"\nAgência: {self._agencia} | Nº: {self._numero} | Saldo: {self.saldo()}"


class ContaCorrente(Conta):
    ...



pessoa = PessoaFisica('Ingrid Alves de Jesus', 23,'12345678911','Antônio Padeiro, nº 15', 'Campo Grande', 'SP')
pessoa2 = PessoaFisica('Robson de Souza', 70,'00033344470','Rua 7, nº 70', 'Jalapão', 'TO')



conta = Conta(pessoa, 500, 1, "0137")
conta2 = Conta(pessoa, 700, 70, "0137")

# Add PessoaFisica dentro da lista de contas
pessoa.adicionar_conta(conta)
pessoa2.adicionar_conta(conta2)

pessoas =[pessoa, pessoa2]

# Exibe a lista de clientes
for pessoa in pessoas:
    pessoa.mostrar_clientes()



""" Interface """
def nova_conta(self, cliente: Cliente, numero: int):
        nome = input('Nome completo:').title()
        idade = int(input('Idade: '))
        cpf = input('CPF: ')
        
        rua = input('Rua e nº: ')
        cidade = input('Cidade: ')
        estado = input('Estado(sigla): ')

