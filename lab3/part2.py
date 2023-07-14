'''
Usando os arquivos f rankenstein sorted.txt e war and peace sorted.txt da etapa anterior, conte quantas vezes cada
palavra acontece, e imprima em ordem cada palavra seguida de sua contagem. Gere os arquivos f rankenstein counted.txt
e war and peace counted.txt.
A sa´ıda deve seguir o formato:
palavra1 #ocorrencias_1
palavra2 #ocorrencias_2
palavra3 #ocorrencias_3
'''
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

