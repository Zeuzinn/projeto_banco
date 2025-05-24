# Sistema Bancário em Python 🏦

## 🎯 Desafio 

O desafio proposto pela **[DIO](https://web.dio.me/)** é criar um Sistema Bancário em Python para simular operações de **depósito**, **saque** e **extrato**, com limite diário de saques. 

---

## ⚙️ Funcionalidades 

- Depósito com validação de valores positivos.
- Saque limitado a R$500,00 por operação.
- Limite diário de 3 saques.
- Exibição de extrato com data e hora das transações.
- Interface de menu interativo no terminal.

---

## 🧠 Conceitos Abordados 
Neste projeto, foram aplicados os seguintes recursos:

- Estruturas condicionais (`if`, `else`, `elif`)
- Laços de repetição com controle (`while`)
- Listas e dicionários para controle de operações
- Modularização com `import` de arquivos distintos
- Manipulação de datas e horas com o módulo `datetime`
- Trabalho com Data e Horas
---

## 🗂️ Estrutura do Projeto

```
📁 projeto_banco/
├── app.py          |# Arquivo principal 
├── funcoes.py      |# Lógica das operações bancárias
├── registro.py     |# Gerenciamento de data e hora
└── README.md       |# Documentação
```
---

## ▶️ Exemplo de Uso
```
=== BIG BANK ===

[1] - Depósito
[2] - Saque
[3] - Extrato
[0] - Sair

Escolha uma operação: 1
Digite o valor do depósito R$1000
Depósito efetuado com sucesso!
```
---