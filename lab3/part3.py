'''Usando os arquivos f rankenstein counted.txt e war and peace counted.txt da etapa anterior, gere um ranking com
as 1000 palavras mais frequentes de cada livro. Este ranking deve ordenar as palavras das mais frequentes para as
menos frequentes. Para duas palavras de mesmo numero de ocorr ´ encias, imprima elas no ranking usando a ordem ˆ
lexicografica. Gere os arquivos ´ f rankenstein ranked.txt e war and peace ranked.txt,'''


from operator import itemgetter, attrgetter
from collections import OrderedDict

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


      