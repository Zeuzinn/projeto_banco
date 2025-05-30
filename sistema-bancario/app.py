from conta_corrente import ContaCorrente
from pessoa_fisica import PessoaFisica


pessoa = PessoaFisica('Ingrid Alves', '21-11-2002','12345678911','Antônio Padeiro, nº 15', 'Campo Grande', 'SP')
pessoa2 = PessoaFisica('Robson de Souza', '07-07-1970','00033344470','Rua 7, nº 70', 'Jalapão', 'TO')

conta = ContaCorrente(pessoa, 100, 1, "0137", 200)
conta2 = ContaCorrente(pessoa2, 70, 70, "0137", 500)

# Add Conta dentro da lista de contas
pessoa.adicionar_conta(conta)
pessoa2.adicionar_conta(conta2)
print()

conta.depositar(200)
conta.sacar(150)

conta2.depositar(700)
conta2.sacar(350)

pessoas = [pessoa, pessoa2]
contas = [conta, conta2]


# Exibe a lista de clientes
for pessoa in pessoas:
    pessoa.mostrar_clientes()

for conta in contas:
    conta.exibir_extrato()