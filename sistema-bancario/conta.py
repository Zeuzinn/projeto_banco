from abc import ABC, abstractmethod
from cliente import Cliente

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
