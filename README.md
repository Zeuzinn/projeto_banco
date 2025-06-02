# Sistema Bancário em Python 🏦

## 🎯 Desafio 

Desenvolvido como parte de um desafio proposto pela **[DIO - Digital Innovation One](https://web.dio.me/)**, este projeto simula um sistema bancário completo com **cadastro de clientes**, **contas bancárias**, e operações como **depósito**, **saque** e **extrato**, utilizando os princípios da **Programação Orientada a Objetos (POO)**.


---

## ⚙️ Funcionalidades 

- ✅ Cadastro de clientes (com validação de CPF - 11 dígitos).
- ✅ Criação automática ou manual de contas para clientes existentes.
- ✅ Depósitos com validação de valores.
- ✅ Saques limitados a R$500,00 por operação.
- ✅ Exibição de extrato com data e hora de cada transação.
- ✅ Interface de menu interativo no terminal.
- ✅ Listagem de clientes e suas contas.
---

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos (POO)
  - Classes: `Pessoa`, `PessoaFisica`, `Conta`, `ContaCorrente`, `Historico`
  - Encapsulamento e composição de objetos
- Estruturas de controle (`if`, `for`, `while`)
- Modularização do código com múltiplos arquivos e pastas
- Geração automática de número de conta com `itertools.count`
- Manipulação de datas e horas com `datetime`
- Práticas de organização e manutenção do código
---

## 🗂️ Estrutura do Projeto

```
📁 projeto_banco/
├── bigbank/
│ ├── clientes/
│ │ ├── pessoa.py
│ │ └── pessoa_fisica.py
│ ├── contas/
│ │ ├── conta.py
│ │ └── conta_corrente.py
│ ├── historico/
│ │ └── historico.py
│ ├── transacoes/
│ │ ├── transacao.py
│ │ ├── deposito.py
│ │ └── saque.py
│ └── interface/
│ └── menu_interacao.py
├── main.py
└── README.md
```
---

## ▶️ Exemplo de Uso
```
=== BIG BANK - MENU ===

[1] - Criar cliente
[2] - Criar nova conta (apenas com CPF existente)
[3] - Depositar
[4] - Sacar
[5] - Extrato
[6] - Listar clientes
[0] - Sair

Escolha uma operação: 1
CPF (Apenas dígitos): 12345678901
Nome completo: Anderson Daronco
...

Cliente e conta criados com sucesso!
```
---

