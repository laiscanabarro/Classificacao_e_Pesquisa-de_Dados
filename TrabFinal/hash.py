from arrayLSE import Node

class HashTable:
    def __init__(self, M):
        self.M = M
        self.size = 0
        # Para cada elemento da tabela, cria uma lista encadeada vazia
        self.table = [None] * M

    def hash(self, key, M):
        return key % M

    def insert(self, key, value):

        self.size += 1
        i = self.hash(key, self.M)
        node = self.table[i]

        # Caso em que não há colisão
        if node is None:
          self.table[i] = Node(key, value)
          return

        # Caso em que há colisão, percorre a lista até o fim e adiciona
        ant = node
        while node is not None:
          ant = node
          node = node.next
        ant.next = Node(key, value)

    def search(self, key):
        i = self.hash(key, self.M)

        node = self.table[i]


        # Procura até a posição vazia ou até encontrar a chave pedida
        while node is not None and node.key != key:
          node = node.next

        if node is None:
          # Miss
          return None

        # Encontrou, retorna o valor
        else:
          return node.value[0]