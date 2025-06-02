from projeto_banco.sistema_bancario.contas.conta import Conta
from projeto_banco.sistema_bancario.clientes.cliente import Cliente
from projeto_banco.sistema_bancario.utils.data_hora import Horario 

class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, saldo: float, numero: int, agencia: str, limite_saque: float):
        super().__init__(cliente, saldo, numero, agencia)
        self._limite_saque = limite_saque 

    def depositar(self, valor: float):
        if valor <= 0:
            print('O depósito deve ser maior que R$0,00')
            return self._saldo 
        else:
            self._saldo += valor
            hora = Horario()
            hora_atual, data_atual = hora.obter_horario()

            # Registra o depósito no histórico da conta, extrato
            self.historico.adicionar_transacao({'valor': +valor, 'data': data_atual, 'hora': hora_atual})

            print('\nProcessando...')
            print(f'{self._cliente.nome} seu depósito foi efetuado com sucesso!\n')
            return self._saldo

    def sacar(self, valor: float):
        if valor > self._limite_saque:
            print('\nProcessando...')
            print(f'Saque negado! O valor deve ser menor ou igual a R${self._limite_saque} \n')

        elif valor > self._saldo:
            print('\nProcessando...')
            print('Saldo indisponível.\n')

        else:
            self._saldo -= valor
            hora = Horario()
            hora_atual, data_atual = hora.obter_horario()

            """ Registrar o saque no histórico da conta, extrato """
            self.historico.adicionar_transacao({'valor': -valor, 'data': data_atual, 'hora': hora_atual})

            print('\nProcessando...')
            print('Saque realizado com sucesso!\n')
        return self._saldo

    def exibir_extrato(self):
        self.historico.mostar_transacoes(self._cliente.nome, self._saldo)