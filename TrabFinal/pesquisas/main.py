from arquivos import *
from funcoes import *

print('Processando os dados...')
start = time.time()

processamento(r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\rating.csv", 
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\players.csv")

end = time.time()
tempo_total = end - start
print(f' {tempo_total:.2f} para processar os dados')

user(4, hash_table_ratings, hash_table_nomes)
posicao(10, 'ST', playerPos)
'''
with open("dados/players.csv", newline='') as arquivo:
    reader = csv.reader(arquivo)
    next(reader)
    
    # percorre a tabela players, busca o id do jogador entre as avaliacoes e cria tabelas hash com informacoes complementares do jogador
    for row in reader:
      sofifa_id, name, player_positions = row[0], row[1], row[2]
      trie_tree.insert(name)
      avaliacao_jogador = hash_table_avaliacoes.search(sofifa_id)

      if avaliacao_jogador is None:  # quando o jogador nao tem avaliacoes
        rating, count = 0, 0
      else:
        rating, count = avaliacao_jogador[1], avaliacao_jogador[2]

      dados = sofifa_id, name, player_positions, float(rating), count
      hash_table_nomes.insert(name, dados)
      hash_table_id.insert(sofifa_id, dados)


def pesquisaNomes(busca, trie_tree, hash_table, saida_nomes):      

    for name in trie_tree.words_from_prefixe(busca):
        item = hash_table.search(name)
        saida_nomes.append(item)

    for i in saida_nomes:
       print(i)


busca = input()
pesquisaNomes(busca, trie_tree, hash_table_nomes, saida_nomes)
'''
