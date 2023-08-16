import tkinter as tk
from tkinter import font as tkfont
from tkinter import scrolledtext
from funcoes import *
from arquivos import *
import time

def encerrar_programa():
    # Lógica para encerrar o programa
    pass

def processar_comando():
    comando = comando_entry.get()
    comando = [x.lower() for x in comando.split()]
    print(comando)

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

    # Limpar a caixa de comando
    comando_entry.delete(0, tk.END)

# Função para simular a obtenção da foto do jogador
def exibe_foto_jogador():
    # Aqui você pode retornar a imagem do jogador
    pass

# Função para exibir os jogadores na área de listagem
def exibir_jogadores(jogadores):
    for jogador in jogadores:
        # Aqui você pode criar um widget para exibir a foto, nome, rating e count do jogador
        # Use a função exibe_foto_jogador() para obter a imagem do jogador
        pass

# Função para realizar a ação de acordo com o comando inserido
def processar_comando():
    comando = comando_entry.get()
    comando = [x.lower() for x in comando.split()]
    print(comando)

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

    # Limpar a caixa de comando
    comando_entry.delete(0, tk.END)

start = time.time()

print('Processando os dados...')
processamento(r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\rating.csv", 
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\players.csv",
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\tags.csv")

end = time.time()
tempo_total = end - start
print(f' {tempo_total:.2f}s para processar os dados')


# Criar a janela principal
root = tk.Tk()

titulo_label = tk.Label(root, text="Consulta aos jogadores de futebol", font=("Helvetica", 16, "bold"))
subtitulo_label = tk.Label(root, text="Beatriz Soviero e Laís Canabarro", font=("Helvetica", 12))

comando_label = tk.Label(root, text="Comandos disponíveis", font=("Helvetica", 12))


menu_label = tk.Label(root, text=" \
                                1 - player <prefixo> : retorna todos os jogadores com o prefixo informado\n \
                                2 - user <user_id>: retorna os 20 jogadores mais bem avaliados pelo usuário com a ID informada\n \
                                3- top<n> <posição>: retorna os melhores n jogadores que jogam na posição informada\n \
                                4- tags <lista de tags>: retorna os jogadores que possuem todas as tags informadas", font=("Helvetica", 10), justify='left')
comando_entry = tk.Entry(root, width=50)
iniciar_button = tk.Button(root, text="Iniciar", command=processar_comando)
encerrar_button = tk.Button(root, text="Encerrar programa", command=encerrar_programa, fg="red")

# Layout dos widgets
titulo_label.pack()
subtitulo_label.pack()
comando_label.pack()
menu_label.pack()
comando_entry.pack()
iniciar_button.pack()
encerrar_button.pack()

# Criar os widgets


# Iniciar a interface
root.mainloop()
