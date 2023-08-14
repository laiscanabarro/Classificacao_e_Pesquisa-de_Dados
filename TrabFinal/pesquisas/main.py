from arquivos import *
from funcoes import *

print('Processando os dados...')
start = time.time()

processamento(r"dados/rating.csv", 
              r"dados/players.csv",
              r"dados/tags.csv")

end = time.time()
tempo_total = end - start
print(f' {tempo_total:.2f} para processar os dados')

user(4, hash_table_ratings, hash_table_nomes)
posicao(10, 'ST', playerPos)
player('Fer', trie_tree, hash_table_nomes, jogadores)
lista_tags = ['Brazil', 'Dribbler']
tags(lista_tags, lista_tags_jogadores, hash_table_nomes)

