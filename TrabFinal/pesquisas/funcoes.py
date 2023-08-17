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

    global hash_table_nomes
    global jogadores
    global trie_tree
    output = ['sofifa_id\t\tnome\t\tposições\t\trating\t\tcount']
    print(f'Exibindo os jogadores com prefixo {prefixe} no nome')
    for name in trie_tree.collectWordsPrefix(prefixe):
        for jogador in jogadores:
            if name == jogador[1]:
                player = hash_table_nomes.search(jogador[0], 0)
                print(f"sofifa_id {player[0][0]}, name {name}, player_positions {player[0][4]}, rating {player[0][2]:.6f}, count {player[0][3]}")
                output.append(f"{player[0][0]}\t\t{name}\t\t{player[0][4]}\t\t{player[0][2]:.6f}\t\t{player[0][3]}")
    return output
                

    print('\n')

# 2.2

def user(key):

    global hash_table_nomes
    global hash_table_ratings

    output = hash_table_ratings.table[key]

    if output != None:
        output = ordena(output, 1)

    i = 0
    print(f'Exibindo os 20 jogadores mais bem avaliados pelo usuário de id {key}')
    output2 = ['sofifa_id\t\tname\t\tglobal_rating\t\tcount\t\trating']
    while i < 20 and output:
        fifaID = int(output[i][0])
        print(f"{fifaID}\t\t{hash_table_nomes.search(fifaID, 0)[0][1]}\t\t{hash_table_nomes.search(fifaID, 0)[0][2]:.6f}\t\t{hash_table_nomes.search(fifaID, 0)[0][3]}\t\t{output[i][1]}")
        output2.append(f"{fifaID}\t\t{hash_table_nomes.search(fifaID, 0)[0][1]}\t\t{hash_table_nomes.search(fifaID, 0)[0][2]:.6f}\t\t{hash_table_nomes.search(fifaID, 0)[0][3]}\t\t{output[i][1]}")
        i += 1
    print('\n')
    return output2

# 2.3

def posicao(n, pos):
    global playerPos
    lista = ordena(playerPos, 2)
    output = []
    output2 = ['sofifa_id\t\tname\t\tposições\t\trating\t\tcount']
    for i in lista:
        if pos in i[4].split(', '):
            output.append(i)
    i = 0
    print(f'Exibindo os top {n} jogadores que jogam na posição {pos}')
    while i < n and output:
        print(f'{output[i][0]}\t\t{output[i][1]}\t\t{output[i][4]}\t\t{output[i][2]:.6f}\t\t{output[i][3]}')
        output2.append(f'{output[i][0]}\t\t{output[i][1]}\t\t{output[i][4]}\t\t{output[i][2]:.6f}\t\t{output[i][3]}')
        i += 1
    print('\n')
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
    output = ['sofifa_id\t\tname\t\tposições\t\trating\t\tcount']
    print(f'Exibindo todos os jogadores com as tags {lista_tags}')
    for i in lista_final:
        player = hash_table_nomes.search(i, 0)
        print(f'{player[0][0]}\t\t{player[0][1]}\t\t{player[0][4]}\t\t{player[0][2]}\t\t{player[0][3]}')
        output.append(f'{player[0][0]}\t\t{player[0][1]}\t\t{player[0][4]}\t\t{player[0][2]}\t\t{player[0][3]}')
    print('\n')
    return output
