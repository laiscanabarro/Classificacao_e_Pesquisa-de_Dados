'''Uma primeira observação é que os dados de jogadores não contêm algumas das informações
a serem retornadas. Por exemplo, deve-se primeiramente guardar em uma tabela hash as
médias de avaliações e total de avaliações para cada jogador. Essas informações devem ser
calculadas e armazenadas em uma etapa de pré-processamento. Para responder esta
pesquisa, deve-se implementar uma árvore trie que busca todos os identificadores de
jogadores que correspondem ao nome ou prefixo dado, e com essa lista de identificadores,
buscar na tabela hash as informações complementares dos jogadores.'''
import csv

class Node:
    def __init__(self, key, value):
      self.key = key
      self.value = value
      self.next = None
      
class HashTable:
    def __init__(self, M):   
        self.M = M
        self.table = [None] * M

    def hash(self, key, M):
        return key % M

    def insere(self, key, value):

        i = self.hash(key, self.M)
        
        if self.table[i] is None:
           self.table[i] = [value]
        
        else:
           self.table[i].append(value)

#indice é o campo que deve ser comparado
    def search(self, key, indice):
        i = self.hash(key, self.M)
        output = []

        if self.table[i] is None:
            return None
        
        for item in self.table[i]:
            if item[indice] == key:
                output.append(item)
            
        if len(output) == 0:
            return None
        else:
            return output
        





