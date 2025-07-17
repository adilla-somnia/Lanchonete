from cardapio import cardapio
from stack import Stack

contas = {} # são as contas pendentes de pagamento, um dicionário que contem mesa e uma lista de pedidos com os itens
notas_fiscais = Stack()  # simula a pilha de notas fiscais da lanchonete. são as contas fechadas

def adicionar_pedido(mesa, itens):
    contas.setdefault(mesa, []).append(itens) # verifica se a mesa existe, e cria se não existir. adiciona os itens na lista de pedidos da mesa

def fechar_conta(mesa):
    if mesa not in contas or not contas[mesa]: # verifica se a mesa tem pedidos
        print("Nenhum pedido para esta mesa.")
        return
    total = sum(cardapio[i]["preco"] for pedido in contas[mesa] for i in pedido) # soma o preço de todos os itens de cada pedido da mesa
    nota = {"mesa": mesa, "pedidos": contas[mesa], "total": total} # cria a nota fiscal
    notas_fiscais.push(nota) # adiciona a nota à pilha de notas fiscais
    contas.pop(mesa) # retira a conta da mesa do dic de contas à pagar
    print(f"Conta da mesa {mesa} fechada. Total: R${total:.2f}")

def ver_conta(mesa):
    if mesa not in contas: # verifica se a mesa tem pedidos
        print("Mesa sem pedidos.")
        return
    print(f"\nConta da mesa {mesa}:")
    total = 0
    for pedido in contas[mesa]: # pega todos os pedidos que a mesa tiver
        nomes = [cardapio[i]["nome"] for i in pedido] # pega os nomes de cada item do pedido
        subtotal = sum(cardapio[i]["preco"] for i in pedido) # soma os preços dos itens desse pedido
        total += subtotal # soma o subtotal do pedido com os subtotais dos outros pedidos
        print(" - " + ", ".join(nomes) + f" → R${subtotal:.2f}") # mostra os nomes dos itens separados por ", " e o valor do subtotal
    print(f"Total: R${total:.2f}") # mostra o total da conta da mesa
    input("\nPressione ENTER para voltar.")

def ver_historico():
    if len(notas_fiscais) == 0: # verifica o tamanho da pilha
        print("Nenhuma nota fiscal registrada.")
        return
    print("Notas fiscais (mais recentes primeiro):")
    for nota in notas_fiscais: # mostra o histórico sem tirar notas da pilha
        print(f"Mesa {nota['mesa']} - R${nota['total']:.2f}")
    input("\nPressione ENTER para voltar.")

def desfazer_ultima_venda():
    nota = notas_fiscais.pop() # pega a nota fiscal do topo
    if nota: # verifica se existe algum dado na variável
        contas[nota["mesa"]] = nota["pedidos"] # faz a conta que tinha paga voltar para o dicionario de contas pendentes de pagamento
        print(f"Última venda desfeita (mesa {nota['mesa']}).")
    else:
        print("Nenhuma nota para desfazer.")
