import arrayLSE
import csv
from functools import partial
import time

# 2.2

def insereResenhas():
    arr = arrayLSE.ArrLSE()
    print('Inserindo os ratings')
    start_time = time.time()
    with open(r"dados/rating.csv") as arq:
        leitor = csv.DictReader(arq)
        print(f'{time.time() - start_time} seconds para ler csv')
        next(leitor)
        start_time = time.time()
        for linha in leitor:  
             arr.insere(int(linha['user_id']),(linha['sofifa_id'], float(linha['rating'])))
    print(f'{time.time() - start_time} seconds para ler cada linha do csv')
    print('fim')
    return arr


def user(key, arr):
    lse = arr[key - 1]
    lse.imprime(key - 1)

# 2.3