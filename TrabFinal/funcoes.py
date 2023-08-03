from arrayLSE import *
import csv


# 2.2

def insereResenhas():
    arr = ArrLSE()
    print('Inserindo')
    with open(r'dados\minirating.csv') as arq:
        leitor = csv.reader(arq)
        next(leitor)
        for linha in leitor:
            arr.insere(int(linha[0]),(linha[1], float(linha[2])))
    print('fim')
    return arr


def user(key):
    arr = insereResenhas()
    lse = arr[key - 1]
    lse.imprime(key - 1)

# 2.3