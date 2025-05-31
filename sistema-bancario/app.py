from conta_corrente import ContaCorrente
from pessoa_fisica import PessoaFisica
from interface import Deposito, Saque


pessoa = PessoaFisica('Ingrid Alves', '21-11-2002','12345678911','Antônio Padeiro, nº 15', 'Campo Grande', 'SP')
pessoa2 = PessoaFisica('Robson de Souza', '17-07-1970','10101070707','Cleiton Rasta, nº 70', 'Monte Verde', 'MG')

conta_1 = ContaCorrente(pessoa, 0, 1, "0137", 100)
conta_2 = ContaCorrente(pessoa2, 0, 2,"0170", 100)

# Cria uma conta
pessoa.adicionar_conta(conta_1)
pessoa2.adicionar_conta(conta_2)

print('-' *50)
print('=== FAZENDO OPERAÇÕES NA PRÓPRIA CONTA ===')
print('-'*50)
# Realiza operações na própria conta
conta_1.depositar(150)
conta_1.sacar(75)
conta_2.depositar(150)
conta_2.sacar(50) 

print(conta_1.saldo())
print(conta_2.saldo())

# Add valor para transferência
conta_1_deposito = Deposito(50)
conta_2_deposito = Deposito(100)
conta_1_saque = Saque(50)


print('-' *50)
print('=== FAZENDO TRANSFERÊNCIAS ENTRE CONTAS ===')
print('-' *50)

# Realiza transferências para outras contas 
conta_1_deposito.registrar(conta_2)
conta_2_deposito.registrar(conta_1)
conta_1_saque.registrar(conta_2)


print(conta_1.saldo())
print(conta_2.saldo())