from abc import ABC, abstractmethod
from projeto_banco.sistema_bancario.clientes.cliente import Cliente
from projeto_banco.sistema_bancario.utils.extrato import Historico 

class Conta(ABC):
    def __init__(self, cliente: Cliente, saldo: float, numero: int, agencia: str):
        self._cliente = cliente     
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia         
        self.historico = Historico() 

    def saldo(self) -> float: 
        return f"Cliente: {self._cliente.nome} - Saldo R${self._saldo:.2f}"

    @abstractmethod
    def depositar(self, valor: float):
        pass

    @abstractmethod     
    def sacar(self, valor: float):
        pass    

    def __str__(self):
        return f"\nAgência: {self._agencia} | Nº: {self._numero} | Saldo: {self.saldo()}"