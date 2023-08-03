class Node:
    def __init__(self, key, value):
      self.key = key
      self.value = value
      self.next = None

# value = (sofifa_id, name, global_rating, count, rating)

class LSE:
  def __init__(self):
        self.head = None

  def append(self, key, dados):
    novo = Node(key,dados)

    # Não foi armazenada nenhuma resenha
    if not self.head:
      self.head = novo

    # Já foi armazenada uma resenha
    else:
      if dados[1] >= self.head.value[1]:
        novo.next = self.head
        self.head = novo
        return
      
      tam = 1
      atual = self.head
      while atual.next != None and dados[1] < atual.next.value[1]:
        atual = atual.next
        tam += 1
        if tam == 21:
          return
      novo.next = atual.next
      atual.next = novo
  
  def get_at_index(self, index):
    current = self.head
    count = 0
    while current:
        if count == index:
            return current.data
        count += 1
        current = current.next
  
  def imprime(self, index):
     nodo = self.get_at_index(index)
     atual = self.head
     while atual:
        print(f'sofifa_id {atual.value[0]} rating {atual.value[1]}')
        atual = atual.next

class ArrLSE:
  def __init__(self):
    # A key é acessada decrementando 1
    self.arr = [LSE() for i in range(138493)]

  def __getitem__(self, index):
    return self.arr[index]

# index = user_id, dados = (sofifa_id,rating)

  def insere(self,index, dados):
    self.arr[index-1].append(index, dados)
  