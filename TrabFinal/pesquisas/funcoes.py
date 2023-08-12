import csv
from hash import *

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


# 2.2

def user(key, table, tableNomes):
    output = table.table[key]

    output = ordena(output, 1)

    i = 0
    print(f'Exibindo os 20 jogadores mais bem avaliados pelo usuário de id {key}')
    while i < 20 and output:
        fifaID = int(output[i][0])
        print(f"sofifa_id {fifaID}, name {tableNomes.search(fifaID, 0)[0][1]}, global_rating {tableNomes.search(fifaID, 0)[0][2]:.6f}, count {tableNomes.search(fifaID, 0)[0][3]}, rating {output[i][1]}")
        i += 1
    print('\n')
# 2.3

def posicao(n, pos, lista):
    lista = ordena(lista, 2)
    output = []
    for i in lista:
        if pos in i[4].split(', '):
            output.append(i)
    i = 0
    print(f'Exibindo os top {n} jogadores que jogam na posição {pos}')
    while i < n and output:
        print(f'sofifa_id {output[i][0]}, name {output[i][1]}, player_positions {output[i][4]}, rating {output[i][2]:.6f}, count {output[i][3]}')
        i += 1
    print('\n')

