import csv, time
from hash import *
from trie import *
from funcoes import *

''' tratamento de dados do arquivo rating:
    guardar em uma tabela hash as médias de avaliações e total de avaliações para cada jogador
'''
saida_nomes = []
playerPos =[]                               # lista de listas [sofifa_id,nome, globalRating, count, positions]
hash_table_avaliacoes = HashTable(24697)    # value = [sofifa id, global ratng, count]
hash_table_nomes = HashTable(18947)         # value = [sofifa_id, nome, globalRating, count, positions]
hash_table_id = HashTable(18947)
hash_table_ratings = HashTable(138494)      # value = [sofifa_id, rating]
trie_tree = TrieTree()

def processamento(rating, players):

    global hash_table_ratings
    global hash_table_avaliacoes
    global hash_table_nomes
    global playerPos
    # ADICIONANDO RATINGS NA HASH TABLE

    with open(rating, newline='') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)  

        sofifa_id = int(next(reader)[1])
        contador = 1
        soma_avalicoes = 0

        # percorre toda tabela rating, calcula a media de avaliacoes de cada jogador e adiciona os novos dados em uma tabela hash
        for row in reader:
            #row[0] = user_id, row[1] = sofifa_id row[2] = rating
            hash_table_ratings.insere(int(row[0]), [row[1], float(row[2])])
            if sofifa_id == int(row[1]):
                contador += 1
                soma_avalicoes += float(row[2])
            else:
                dados = sofifa_id, (float)(soma_avalicoes/contador), contador
                # sofifa id, global ratng, count
                hash_table_avaliacoes.insere(sofifa_id, dados)
                
                sofifa_id = int(row[1])
                soma_avalicoes = 0
                contador = 1

        # ultimo jogador da tabela rating
        dados = sofifa_id, (float)(soma_avalicoes/contador), contador
        hash_table_avaliacoes.insere(sofifa_id, dados)
        
        arquivo.close()

    # ADICIONANDO NOMES E POSIÇÕES NA HASH TABLE

    # adiciona nome, id e posições na hash
    with open(players, newline='') as arquivo:
        reader = csv.reader(arquivo)
        next(reader)  

        for row in reader:
            #row[0] = sofifa id row[1] = nome row[2] = positions
            #value = [sofifa_id,nome, globalRating, count, positions]
            player = hash_table_avaliacoes.search(int(row[0]), 0)

            if player is not None:
                dados = [int(row[0]), row[1], player[0][1], player[0][2], row[2]]
            else:
                dados = [int(row[0]), row[1], 0, 0, row[2]]

            hash_table_nomes.insere(int(row[0]), dados)

            if dados[3] >= 1000:
                playerPos.append(dados)
    arquivo.close()