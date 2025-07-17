# Sistema de Lanchonete em Python

Este é um projeto simples de terminal que simula o funcionamento de uma lanchonete. Ele utiliza estruturas de dados fundamentais como **fila**, **pilha**, **dicionário** e **listas** para gerenciar pedidos, contas e histórico de vendas.

## Estrutura do Projeto

- `app.py` → Interface principal do usuário (menu)
- `cardapio.py` → Define o cardápio com itens, preços, tempos de preparo e categorias
- `cozinha.py` → Processamento automático da fila de pedidos com `threading`
- `caixa.py` → Controle de contas por mesa, histórico de notas fiscais, fechamento de conta
- `stack.py` → Implementação da estrutura de pilha (`Stack`)

## Funcionalidades

- Visualizar cardápio por categoria (Lanches, Bebidas, Sobremesas)
- Fazer pedidos para uma mesa
- Processamento automático de pedidos na **fila de preparo**
- O preparo é simulado por tempo e executado em **background**
- Ao finalizar, o pedido vai para a conta da mesa
- Ver a conta da mesa com nomes dos itens e total a pagar
- Fechar a conta (gera uma nota fiscal que é empilhada no histórico)
- Ver histórico de vendas (últimas notas primeiro - pilha)
- Desfazer a última venda (retira a última nota do histórico e devolve à conta)

## Estruturas de Dados Usadas

- **Dicionário**: para representar o cardápio e as contas por mesa
- **Fila**: para pedidos em ordem de chegada (na cozinha)
- **Pilha**: para notas fiscais (último pagamento no topo)
- **Listas**: para armazenar itens de pedidos

## ▶ Como Executar

1. Tenha o Python instalado (3.7+)
2. Salve todos os arquivos na mesma pasta
3. No terminal, execute: python app.py
