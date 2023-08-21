import csv
from hash import *
from trie import *
# from funcoes import *

''' tratamento de dados do arquivo rating:
    guardar em uma tabela hash as médias de avaliações e total de avaliações para cada jogador
'''
playerPos =[]                               # lista de listas [sofifa_id, nome, globalRating, count, positions]
jogadores = []                              # lista de listas [sofifa_if, nome]
lista_tags_jogadores = []                   # lista de listas [sofifa_id, lista_tags]
hash_table_avaliacoes = HashTable(24697)    # value = [sofifa id, global ratng, count]
hash_table_nomes = HashTable(18947)         # value = [sofifa_id, nome, globalRating, count, positions, short]
hash_table_ratings = HashTable(138494)      # value = [sofifa_id, rating]
trie_tree = Trie()

def processamento(rating, players, tags, extras):

    global hash_table_ratings
    global hash_table_avaliacoes
    global hash_table_nomes
    global playerPos
    global jogadores
    global trie_tree
    global lista_tags_jogadores
    global flagFim, flagPlayers, flagRatings, flagTags
    
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
    
    flagRatings = True
    arquivo.close()

    

    # ADICIONANDO NOMES E POSIÇÕES NA HASH TABLE

    # adiciona nome, id e posições na hash
    with open(players, newline='') as arquivo, open(extras, newline='', encoding='utf-8') as arq2:
        reader = csv.reader(arquivo)
        leitor2 = csv.reader(arq2)
        next(reader)
        next(leitor2)  

        for row, linha2 in zip(reader, leitor2):
            #row[0] = sofifa id row[1] = nome row[2] = positions
            #value = [sofifa_id,nome, globalRating, count, positions, nationality, club_name, league_name]
            #linha2 = [sofifa_id, nationality, club_name, league_name]
            trie_tree.insert(row[1])
            player = hash_table_avaliacoes.search(int(row[0]), 0)

            if player is not None:
                dados = [int(row[0]), row[1], player[0][1], player[0][2], row[2], linha2[1], linha2[2], linha2[3]]
            else:
                dados = [int(row[0]), row[1], 0, 0, row[2], linha2[1], linha2[2], linha2[3]]

            hash_table_nomes.insere(int(row[0]), dados)
            jogadores.append([int(row[0]), row[1]])

            if dados[3] >= 1000:
                playerPos.append(dados)
        

    arquivo.close()

    with open(tags, newline='') as arquivo:
        reader = csv.reader(arquivo)
        next(reader) 

        sofifa_id = int(next(reader)[1])
        lista_tags = []

        for row in reader:
            if sofifa_id == int(row[1]):
                lista_tags.append(row[2])
            else:
                jogador = [sofifa_id, lista_tags]
                lista_tags_jogadores.append(jogador)
                lista_tags = []
                sofifa_id = int(row[1])
                lista_tags.append(row[2]) 
    
    arquivo.close()



