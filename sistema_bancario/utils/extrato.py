class Historico:
    def __init__(self):
        self._transacoes = [] 

    def adicionar_transacao (self, transacao_data: dict):
        self._transacoes.append(transacao_data)

    # Exibe transações
    def mostar_transacoes (self, nome_cliente: str, saldo_atual: float):
        if not self._transacoes:
            print("\nVocê não realizou nenhuma movimentação.")
        else:
            print(f"\n=== EXTRATO COMPLETO DE {nome_cliente.upper()} ===\n")
            for t in self._transacoes:
                valor = t['valor']
                data = t['data']
                hora = t['hora']
                tipo = "Depósito" if valor > 0 else "Saque"
                print(f"{tipo}: R$ {valor:,.2f} | Data: {data} | Hora: {hora}")

        print(f"\nSaldo atual: R$ {saldo_atual:,.2f}\n")
        