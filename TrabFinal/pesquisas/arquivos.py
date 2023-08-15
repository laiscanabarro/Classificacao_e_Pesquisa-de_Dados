import csv, time
from hash import *
from trie import *
# from funcoes import *

''' tratamento de dados do arquivo rating:
    guardar em uma tabela hash as médias de avaliações e total de avaliações para cada jogador
'''
<<<<<<< Updated upstream
playerPos =[]                               # lista de listas [sofifa_id, nome, globalRating, count, positions]
jogadores = []                              # lista de listas [sofifa_if, nome]
lista_tags_jogadores = []                   # lista de listas [sofifa_id, lista_tags]
=======
playerPos =[]                               # lista de listas [sofifa_id,nome, globalRating, count, positions]
jogadores = {}                              # dicionário com a chave sendo o nome e o valor seu id
>>>>>>> Stashed changes
hash_table_avaliacoes = HashTable(24697)    # value = [sofifa id, global ratng, count]
hash_table_nomes = HashTable(18947)         # value = [sofifa_id, nome, globalRating, count, positions]
hash_table_ratings = HashTable(138494)      # value = [sofifa_id, rating]
trie_tree = Trie()

def processamento(rating, players, tags):

    global hash_table_ratings
    global hash_table_avaliacoes
    global hash_table_nomes
    global playerPos
    global jogadores
    global trie_tree
    global lista_tags_jogadores
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
            trie_tree.insert(row[1])
            player = hash_table_avaliacoes.search(int(row[0]), 0)

            if player is not None:
                dados = [int(row[0]), row[1], player[0][1], player[0][2], row[2]]
            else:
                dados = [int(row[0]), row[1], 0, 0, row[2]]

            hash_table_nomes.insere(int(row[0]), dados)
<<<<<<< Updated upstream
            jogadores.append([int(row[0]), row[1]])
=======
            jogadores[row[1]] = int(row[0])
>>>>>>> Stashed changes

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
                


