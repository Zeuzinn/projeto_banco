from abc import ABC, abstractmethod
from conta import Conta

class Transacao(ABC):
    
    @abstractmethod
    def registrar(self, conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta: Conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor: float):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)
