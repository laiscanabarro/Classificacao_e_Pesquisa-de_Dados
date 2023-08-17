from arquivos import *
from funcoes import *
import time
import tkinter

print('Processando os dados...')
start = time.time()

processamento(r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\rating.csv", 
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\players.csv",
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\tags.csv",
              "playersExtras.csv")

end = time.time()
tempo_total = end - start
print(f' {tempo_total:.2f}s para processar os dados')

while True:
  comando = [x.lower() for x in input('Insira o comando (s/S para encerrar): ').split()]

  if comando[0] == 'user':
    user(int(comando[1]))

  elif 'top' in comando[0]:
    posicao(int(comando[0][3:]), comando[1].upper().replace("'", ''))

  elif comando[0] == 'player':
    prefixo = comando[1].capitalize()
    player(prefixo)

  elif comando[0] == 'tags':
    lista_tags = [x.replace("'", '').capitalize() for x in comando[1:]]
    tags(lista_tags)

  elif comando[0] == 's':
    print('Programa encerrado')
    break
  
  else:
    print('Comando inválido!')

