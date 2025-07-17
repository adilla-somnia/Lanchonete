from queue import Queue
from threading import Thread
import time
from cardapio import cardapio
import caixa

fila_preparo = Queue()

def processar_pedidos():
    while True:
        if not fila_preparo.empty():
            pedido = fila_preparo.get() # pega o primeiro pedido da fila
            tempo = sum(cardapio[id]["tempo_preparo"] for id in pedido["itens"]) # soma o tempo de preparo de todos os itens no pedido
            print(f"Preparando pedido da mesa {pedido['mesa']}... ({tempo}s)") # mostra o tempo de preparo de forma estática
            time.sleep(tempo) # aguarda o tempo de preparo do pedido
            caixa.adicionar_pedido(pedido["mesa"], pedido["itens"]) # o pedido foi entregue. e a agora já foi para a conta da mesa
            print(f"Pedido da mesa {pedido['mesa']} entregue.")
        else:
            time.sleep(1) # evita uso excessivo da CPU

Thread(target=processar_pedidos, daemon=True).start() # serve para rodar em paralelo a função de processamento de pedidos
# dessa forma os pedidos começam a ser preparados assim que entram na fila
# loop também acaba com o fechamento do programa(daemon=True)