from operator import itemgetter, attrgetter
from collections import OrderedDict

'''Implementar Radix Sort MSD para strings'''

M=15

#Transforma o caractere em código ASCII
def charAt(s, d):
  if len(s) == d: return -1;
  else: return ord(s[d])

#Chama a função MSD e cria o vetor auxiliar
def sort(a, n):
  aux = [None] * n
  msd(a, 0, n-1, 0,aux)


def less(v, w, d):
  for i in range(d, min(len(v), len(w))):
      if ord(v[i]) < ord(w[i]):
          return True
      if ord(v[i]) > ord(w[i]):
          return False
  return len(v) < len(w)

def insertionSort(a, esq, dir, d):
  for i in range(esq, dir + 1):
    j = i
    while j > esq and less(a[j], a[j-1], d):
      a[j - 1], a[j] = a[j], a[j - 1]
      j -= 1

def msd(a, esq, dir, d, aux):
  if dir <= esq + M:
    insertionSort(a, esq, dir, d)
    return
  count = [0] * 258

  for i in range(esq, dir + 1):
    c = charAt(a[i], d)
    count[c+2] += 1

  for r in range(257):
    count[r + 1] += count[r]

  for i in range(esq, dir + 1):
    c = charAt(a[i], d)
    aux[count[c+1]] = a[i]
    count[c+1] += 1

  for i in range(esq, dir+1):
    a[i] = aux[i - esq]

  for r in range(256):
    msd(a, esq + count[r], esq + count[r+1] - 1, d + 1, aux)


'''Ordenar palavras de um arquivo de entrada usando Radix Sort MSD'''

def ordenaStrings(arquivo):
    with open(arquivo, 'r') as t:
        test = t.read()
    #Cria um vetor com as palavras do arquivo 
    vetorStrings = test.split()
    
    #Ordenada o vetor de palavras em ordem lexicografica
    sort(vetorStrings, len(vetorStrings))
    t.close()
    return vetorStrings

def ordenaArquivo(arquivoEntrada, arquivoSaida):
    #Ordenadas as palavras do arquivo de entrada em ordem lexicografica
    vetorString = ordenaStrings(arquivoEntrada)
    saidaSorted = open(arquivoSaida, 'a')

    #Escreve cada elemento do vetor ordenado em uma linha do arquivo de saida
    for palavra in vetorString:
        saidaSorted.write(f'{palavra}\n')
    saidaSorted.close()

ordenaArquivo('frankestein.txt', 'frankenstein_sorted.txt')
ordenaArquivo('war_and_peace.txt', 'war_and_peace_sorted.txt')


''' Contar as palavras do arquivo ordenado'''

def contadorDePalavras(arquivoOrdenado, arquivoContagem):
    entrada = open(arquivoOrdenado, 'r')
    linhas = entrada.readlines()
    saida = open(arquivoContagem, 'a')

    contagem = 0
    string = linhas[0]
    
    #Conta quantas vezes uma palavra acontece e armazena em ordem cada palavra seguida de sua contagem
    for linha in linhas:
        if linha == string:
            contagem += 1
        else:
            string = string.rstrip("\n")
            saida.write(f'{string} {contagem}\n')
            string = linha
            contagem = 1
    entrada.close()
    saida.close()

contadorDePalavras('frankenstein_sorted.txt', 'frankenstein_counted.txt')
contadorDePalavras('war_and_peace_sorted.txt', 'war_and_peace_counted.txt')


'''Top 1000 palavras mais frequentes'''

def ranking(arquivoContagem, arquivoRanking):
    entrada = open(arquivoContagem, 'r')
    saida = open(arquivoRanking, 'w')
    
    #Cria um vetor de tuplas, que contem no primeiro termo a palavra e no segundo a quantidade de recorrencias dela
    palavras = [(linha.split()[0], int(linha.split()[1])) for linha in entrada.readlines()]

    #Ordena as palavras das mais frequentes para as menos frequentes
    ranking = sorted(palavras, key=itemgetter(1), reverse=True)
    rankingFinal = list(OrderedDict.fromkeys(ranking))

    #Escreve no arquivo de saida as 1000 palavras mais frequentes
    for palavra in rankingFinal[:1000]:
       saida.write(f'{palavra[0]} {palavra[1]}\n')
    entrada.close()
    saida.close()    

    
ranking('frankenstein_counted.txt', 'frankenstein_ranked.txt')
ranking('war_and_peace_counted.txt', ' war_and_peace_ranked.txt')