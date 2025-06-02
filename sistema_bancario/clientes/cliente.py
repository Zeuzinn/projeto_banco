from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, rua_numero: str, cidade: str, estado: str):
        self.rua_numero = rua_numero
        self.cidade = cidade
        self.estado = estado
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        conta.historico.adicionar_transacao(transacao)

    @abstractmethod
    def adicionar_conta(self, conta): 
        pass
    
    @abstractmethod
    def mostrar_clientes(self):
        pass