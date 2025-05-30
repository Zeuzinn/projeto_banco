class Historico:
    def __init__(self):
        self._transacoes = [] 

    def adicionar_transacao(self, transacao_data: dict):
        self._transacoes.append(transacao_data)

    # Exibe transações
    def exibir_extrato(self): 
        if not self._transacoes:
            print('Você não realizou nenhuma movimentação.')
        else:
            print('\n=== EXTRATO ===\n')
            for ex in self._transacoes:
                print(f"R${ex['valor']:,.2f} - Hora: {ex['hora']}")
        