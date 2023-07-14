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


'''
Esta tarefa ira usar arquivos de entrada.txt disponibilizados no arquivos entradas.zip. no Moodle para validar o algo- ´
ritmo Radix Sort MSD. Ao testar um dado arquivo .txt, fac¸a a leitura do mesmo e armazene-o em um vetor de strings
compat´ıvel com o algoritmo Radix Sort MSD implementando na etapa anterior. Inicialmente, teste o algoritmo Radix
Sort MSD com os arquivos test1.txt, test2.txt, test3.txt e test4.txt, verificando a correc¸ao do algoritmo. ˜
Apos validar o algoritmo, teste dois arquivos de duas obras liter ´ arias disponibilizadas publicamente, ´ Frankenstein1
e War and Peace 2
. Ordene os arquivos de texto f rankenstein.txt e war and peace.txt, e gere os arquivos
f rankenstein sorted.txt e war and peace sorted.txt, contendo em cada arquivo as palavras ordenadas em ordem lexicografica, uma palavra por linha. Um exemplo de sa ´ ´ıda do arquivo f rankenstein sorted.txt e listado abaixo:
'''
def ordenaStrings(arquivo):
    with open(arquivo, 'r') as t:
        test = t.read()
    #Cria um vetor com as palavras do arquivo 
    vetorStrings = test.split()
    
    #Ordenada o vetor de palavras em ordem lexicografica
    sort(vetorStrings, len(vetorStrings))
    t.close()
    return vetorStrings

#ordenaStrings('test1.txt')
#ordenaStrings('test2.txt')
#ordenaStrings('test3.txt')
#ordenaStrings('test4.txt')


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

