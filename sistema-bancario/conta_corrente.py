from conta import Conta
from cliente import Cliente
from registro import Horario

class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, saldo : float, numero: int, agencia: str, limite_saque: float):
        super().__init__(cliente, saldo, numero, agencia)
        
        self._limite_saque = limite_saque   # Define um limite de saque por conta

    def depositar(self, valor: float):
        if valor <= 0:
            print('O depósito deve ser maior que R$0,00')
            return self._saldo  
        
        else:
            self._saldo += valor
            hora = Horario()
            hora_atual, data_atual = hora.obter_horario()
            
            self._extrato.append({'valor': +valor, 'data': data_atual, 'hora': hora_atual})
            
            print('Processando...')
            print(f'{self._cliente.nome} seu depósito efetuado com sucesso!\n')
            return self._saldo
    
    def sacar(self, valor: float):
        if valor > self._limite_saque:
            print('Processando...')
            print(f'Saque negado! O valor deve ser menor ou igual a R${self._limite_saque} \n')
        
        elif valor > self._saldo:
            print('Processando...')
            print('Saldo indisponível.\n')

        else:
            self._saldo -= valor
            hora = Horario()
            hora_atual, data_atual = hora.obter_horario()
        
            self._extrato.append({'valor': -valor, 'data': data_atual, 'hora': hora_atual})
            
            print('Processando...')
            print('Saque realizado com sucesso!\n')
        return self._saldo

    def exibir_extrato(self):
        if not self._extrato:
            print('Você não realizou nenhuma movimentação.')

        else:
            print('\n=== EXTRATO ===\n')
            for ex in self._extrato:
                print(f"R${ex['valor']:,.2f} - Hora: {ex['hora']}")
                
        print(f'\n{self._cliente.nome} - Saldo: R${self._saldo:,.2f}')
