from cozinha import fila_preparo
from cardapio import cardapio
import caixa

# funções pro user

def mostrar_categorias():
    categorias = set(item["categoria"] for item in cardapio.values()) # o SET é usado para pegar as categorias sem repetições
    print("\nCategorias disponíveis:")
    for i, cat in enumerate(sorted(categorias), start=1): # uso do sorted para manter tudo em ordem alfabética e melhorar a experiência do user
        print(f"{i} - {cat}")
    print("0 - Voltar") # volta para o menu inicial

    escolha = input("Escolha uma categoria: ")
    if escolha == "0":
        return
    try:
        categoria_escolhida = list(sorted(categorias))[int(escolha) - 1] # mantem em ordem alfabetica para pegar o número correspondente, e então, a categoria correspondente ao número
    except (ValueError, IndexError):
        print("Categoria inválida.") # tratamento de erro
        return

    print(f"\n# {categoria_escolhida}")
    for id, item in cardapio.items(): # puxa os itens do cardapio
        if item["categoria"] == categoria_escolhida: # escolhe apenas os itens da categoria selecionada
            print(f"{id} : {item['nome']} - R${item['preco']:.2f} ({item['tempo_preparo']}s)") # imprime os itens da categoria correta

    voltar = input("\nPressione ENTER para voltar.")
    if voltar == "":
        return mostrar_categorias() # volta ao menu das categorias, caso deseje ver outra

def fazer_pedido():
    mesa = input("Número da mesa (0 para voltar): ")
    if mesa == "0": # volta ao menu principal
        return
    try: # verifica o tipo de input
        mesa = int(mesa) # pega a mesa do user
    except ValueError:
        print("Número inválido.") # tratamento de erro
        return

    categorias = set(item["categoria"] for item in cardapio.values()) # mais uma vez faz um SET para mostrar as categorias sem repetições
    print("\n--- CARDÁPIO COMPLETO ---")
    for categoria in sorted(categorias): # dessa vez todas as categorias serão impressas com os seus respectivos itens abaixo
        print(f"\n#{categoria}")
        for id, item in cardapio.items():
            if item["categoria"] == categoria: # imprime apenas os itens da categoria
                print(f"{id} : {item['nome']} - R${item['preco']:.2f} ({item['tempo_preparo']}s)")

    ids = input("\nDigite os IDs dos itens separados por espaço (ou 0 para cancelar): ")
    if ids.strip() == "0": #retorna
        return
    try:
        itens = list(map(int, ids.split())) # divide o input por espaços, transforma em inteiro, e depois transforma em uma lista
        fila_preparo.put({"mesa": mesa, "itens": itens}) # coloca na fila tanto a mesa, quanto os pedidos. o uso do PUT se deve ao padrão do from queue import Queue
        print("🧾 Pedido adicionado à fila.") # a fila vem de cozinha.py, onde os pedidos são preparados
    except ValueError:
        print("IDs inválidos.") # tratamento de erro

def menu():
    while True: # mantem o looping enquanto o user quiser
        print("\n--- MENU ---")
        print("1 - Ver cardápio")
        print("2 - Fazer pedido")
        print("3 - Ver conta de uma mesa")
        print("4 - Fechar conta")
        print("5 - Ver histórico de vendas")
        print("6 - Desfazer última venda")
        print("0 - Sair")
        op = input("Escolha: ")

        if op == "1":
            mostrar_categorias()
        elif op == "2":
            fazer_pedido()
        elif op == "3":
            mesa = input("Número da mesa (ou 0 para voltar): ")
            if mesa != "0":
                try:
                    caixa.ver_conta(int(mesa)) # função vem de caixa.py
                except ValueError:
                    print("Número inválido.") # tratamento de erro
        elif op == "4":
            mesa = input("Número da mesa (ou 0 para voltar): ")
            if mesa != "0":
                try:
                    caixa.fechar_conta(int(mesa)) # função vem de caixa.py
                except ValueError:
                    print("Número inválido.") # tratamento de erro
        elif op == "5":
            caixa.ver_historico() # função vem de caixa.py
        elif op == "6":
            caixa.desfazer_ultima_venda() # função vem de caixa.py
        elif op == "0":
            print("Encerrando...") # tchau thcau
            break
        else:
            print("Opção inválida.") # tratamento de erro

if __name__ == "__main__": # verifica se o script está sendo rodado diretamente
    menu() # inicia o menu