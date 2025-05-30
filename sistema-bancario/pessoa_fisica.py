from cliente import Cliente
from registro import Horario

class PessoaFisica(Cliente):
    def __init__(self, nome: str, data_nascimento: str, cpf: str, rua_numero: str, cidade: str, estado: str):
        
        super().__init__(rua_numero, cidade, estado)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = self.verificar_cpf(cpf)

    # Verifica o CPF antes de passar pro SELF.CPF
    def verificar_cpf(self, cpf: str):
        if not cpf.isdigit() or len(cpf) != 11:
            print('CPF inválido. O CPF deve possuir 11 dígitos \n')
            return None
        return cpf

    # Add conta registrando horário
    def adicionar_conta(self, conta):
        hora = Horario()
        hora_atual, data_atual = hora.obter_horario()
        self.contas.append(conta)
        print(f'Olá, {self.nome}! Sua conta foi criada com sucesso.') 
        print(f'Dia:{data_atual} - Hora:{hora_atual} \n')

    def mostrar_clientes(self):
        for c in self.contas:
            print(f"Nome: {self.nome} - CPF: {self.cpf} | \nAgência: {c._agencia} - Saldo R$:{c._saldo:,.2f}")
            print()
            
    def __str__(self):
        return  f"Nome: {self.nome} - CPF: {self.cpf} | Cidade/Estado: {self.cidade}, {self.estado}"