class Node:
    def __init__(self, key, value):
      self.key = key
      self.value = value
      self.next = None

class ArrLSE:
  def __init__(self):
    self.arr = [None] * 138493

# index = user_id, dados = (sofifa_id,rating)

  def insere(self,index, dados):

    nodo = self.arr[index - 1]

    # Não foi armazenado nenhuma resenha
    if nodo == None:
      nodo = Node(index, dados)
      return

    # Já foi armazenada uma resenha
    novo = Node(index, dados)

    if dados[1] >= nodo.value[1]:
      novo.next = nodo
      return
    
    tam = 0
    while nodo.next != None and nodo.next.value[1] > dados[1]:
      nodo = nodo.next
      tam += 1
      if tam > 20:
        return
    novo.next = nodo.next
    nodo.next = novo

  def imprimir(self):
    for i in self.arr:
      if i != None:
        while i.node != None:
          print(i.node.value)
          i.node = i.node.next
  