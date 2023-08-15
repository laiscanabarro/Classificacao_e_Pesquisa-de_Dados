from arquivos import *
from funcoes import *

print('Processando os dados...')
start = time.time()

processamento(r"dados/rating.csv", 
              r"dados/players.csv",
              r"dados/tags.csv")

end = time.time()
tempo_total = end - start
print(f' {tempo_total:.2f}s para processar os dados')

# player fer
# user 4
# top10 'ST'
# vtags ‘Brazil’ ‘Dribbler’

while True:
  comando = [x.lower() for x in input('Insira o comando (s/S para encerrar): ').split()]

  if comando[0] == 'user':
    user(int(comando[1]))
  elif 'top' in comando[0]:
    posicao(int(comando[0][3:]), comando[1].upper().replace("'", ''))
  elif comando[0] == 'player':
    prefixo = comando[1]
  elif comando[0] == 'tags':
    tags = comando[1:]
  elif comando[0] == 's':
    print('Programa encerrado')
    break
  else:
    print('Comando inválido!')

<<<<<<< Updated upstream
user(4, hash_table_ratings, hash_table_nomes)
posicao(10, 'ST', playerPos)
player('Fer', trie_tree, hash_table_nomes, jogadores)
lista_tags = ['Brazil', 'Dribbler']
tags(lista_tags, lista_tags_jogadores, hash_table_nomes)
=======
'''
with open("dados/players.csv", newline='') as arquivo:
    reader = csv.reader(arquivo)
    next(reader)
    
    # percorre a tabela players, busca o id do jogador entre as avaliacoes e cria tabelas hash com informacoes complementares do jogador
    for row in reader:
      sofifa_id, name, player_positions = row[0], row[1], row[2]
      trie_tree.insert(name)
      avaliacao_jogador = hash_table_avaliacoes.search(sofifa_id)
>>>>>>> Stashed changes

