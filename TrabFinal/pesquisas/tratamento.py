import csv, time
import hash, trie, funcoes

''' tratamento de dados do arquivo rating:
    guardar em uma tabela hash as médias de avaliações e total de avaliações para cada jogador
'''
saida_nomes = []
hash_table_avaliacoes = hash.HashTable(24697)
hash_table_nomes = hash.HashTable(18947)
hash_table_id = hash.HashTable(18947)
trie_tree = trie.TrieTree()

start = time.time()

with open("dados/rating.csv", newline='') as arquivo:
    reader = csv.reader(arquivo)
    next(reader)  

    sofifa_id = int(next(reader)[1])
    contador = 1
    soma_avalicoes = 0

    # percorre toda tabela rating, calcula a media de avaliacoes de cada jogador e adiciona os novos dados em uma tabela hash
    for row in reader:
      if sofifa_id == int(row[1]):
        contador += 1
        soma_avalicoes += float(row[2])
      else:
        dados = sofifa_id, (float)(soma_avalicoes/contador), contador
        hash_table_avaliacoes.insert(sofifa_id, dados)
        sofifa_id = int(row[1])
        soma_avalicoes = 0
        contador = 1

    # ultimo jogador da tabela rating
    dados = sofifa_id, (float)(soma_avalicoes/contador), contador
    hash_table_avaliacoes.insert(sofifa_id, dados)
    
    arquivo.close() 

arr = funcoes.insereResenhas()
funcoes.user(4, arr)

end = time.time()
tempo_total = end - start
print(tempo_total)

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
