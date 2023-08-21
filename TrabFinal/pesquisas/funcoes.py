import csv
from hash import *
from trie import *
import tkinter as tk
from arquivos import hash_table_nomes, hash_table_ratings, trie_tree, lista_tags_jogadores, jogadores, playerPos

#position é o campo da sublista que informa por onde deve ser ordenado
def ordena(data, position):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    left_half = ordena(left_half, position)
    right_half = ordena(right_half, position)

    return merge(left_half, right_half, position)

def merge(left, right, position):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][position] >= right[right_index][position]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

def lista_repetidos(lista):
    lista_rep = []

    for i, elemento in enumerate(lista):
        if elemento in lista[i+1:]:
            lista_rep.append(elemento)

    if len(lista_rep) == 0:
        return lista
    else:
        return lista_rep


# 2.1

def player(prefixe):

    global hash_table_nomes #[sofifa_id,nome, globalRating, count, positions, nationality, club_name, league_name]
    # 'FIFA ID\t\tNOME\t\tGlobal Rating\t\tCount\t\tRating\t\tNacionalidade\t\tClube\t\tLiga'
    global jogadores
    global trie_tree
    output = []
    for name in trie_tree.collectWordsPrefix(prefixe):
        for jogador in jogadores:
            if name == jogador[1]:
                player = hash_table_nomes.search(jogador[0], 0)
                output.append((player[0][0],name,player[0][4],player[0][2],player[0][3],player[0][5],player[0][6],player[0][7]))
    return output
            
# value = [sofifa_id, nome, globalRating, count, positions, short]
# 2.2

def user(key):

    global hash_table_nomes
    global hash_table_ratings

    output = hash_table_ratings.table[key]

    if output != None:
        output = ordena(output, 1)
    # 'FIFA ID\t\tNome\t\tGlobal Rataing\t\tCount\t\tRating'
    i = 0
    output2 = []
    while i < 20 and output:
        fifaID = int(output[i][0])
        output2.append((fifaID,hash_table_nomes.search(fifaID, 0)[0][1],hash_table_nomes.search(fifaID, 0)[0][2],hash_table_nomes.search(fifaID, 0)[0][3],output[i][1]))
        i += 1
    return output2

# 2.3

def posicao(n, pos):
    global playerPos
    lista = ordena(playerPos, 2)
    output = []
    output2 = []
    for i in lista:
        if pos in i[4].split(', '):
            output.append(i)
    i = 0
    while i < n and output:
        output2.append((output[i][0],output[i][1],output[i][4],output[i][2],output[i][3]))
        i += 1
    return output2

# 2.4

def tags(lista_tags): 
    lista_ids = []
    
    global lista_tags_jogadores
    global hash_table_nomes

    for i in lista_tags:
        for j in lista_tags_jogadores:
            if i in j[1]:
                lista_ids.append(j[0])

    lista_final = lista_repetidos(lista_ids)
    output = []
    for i in lista_final:
        player = hash_table_nomes.search(i, 0)
        output.append((player[0][0],player[0][1],player[0][4],player[0][2],player[0][3],player[0][5],player[0][6],player[0][7]))
    return output
