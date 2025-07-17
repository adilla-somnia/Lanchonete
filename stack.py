# código de pilha padrão encontrado na internet

class Stack:
    def __init__(self):
        self.itens = []

    def push(self, item):
        self.itens.append(item)

    def pop(self):
        return self.itens.pop() if not self.is_empty() else None

    def peek(self):
        return self.itens[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.itens) == 0

    def __len__(self):
        return len(self.itens)

    def __iter__(self):
        return reversed(self.itens)
