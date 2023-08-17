import tkinter as tk
from tkinter import font as tkfont
from tkinter import scrolledtext
from funcoes import player, user, tags, posicao
from arquivos import *
import time

titulo = voltar_button = textoWidget = None

# Função para simular a obtenção da foto do jogador
def exibe_foto_jogador():
    # Aqui você pode retornar a imagem do jogador
    pass

# Função para realizar a ação de acordo com o comando inserido
def processar_comando():


    titulo_label.pack_forget()
    subtitulo_label.pack_forget()
    comando_label.pack_forget()
    menu_label.pack_forget()
    comando_entry.pack_forget()
    iniciar_button.pack_forget()
    encerrar_button.pack_forget()

   

    global titulo, voltar_button, textoWidget
    textoWidget = tk.Text(root)

    comando = comando_entry.get()
    comando = [x.lower() for x in comando.split()]
    print(comando)

    voltar_button = tk.Button(root, text="Realizar nova consulta", command=voltar_tela_anterior)

    try:
        if comando[0] == 'user':
            id = int(comando[1])
            output = user(id)
            titulo = tk.Label(root, text=f'Exibindo os 20 jogadores mais bem avaliados pelo usuário {id}', font=("Helvetica", 16, "bold"))
            titulo.pack()
            textoWidget.pack()
            voltar_button.pack()
            textoWidget.delete("1.0", tk.END)
            for i in output:
                textoWidget.insert(tk.END, f'{i}\n')

        elif 'top' in comando[0]:
            n = int(comando[0][3:])
            pos = comando[1].upper().replace("'", '')
            output = posicao(n, pos)
            titulo = tk.Label(root, text=f'Exibindo os {n} melhores jogadores da posição {pos}', font=("Helvetica", 16, "bold"))
            titulo.pack()
            textoWidget.pack()
            voltar_button.pack()
            textoWidget.delete("1.0", tk.END)
            for i in output:
                textoWidget.insert(tk.END, f'{i}\n')

        elif comando[0] == 'player':
            prefixo = comando[1].capitalize()
            titulo = tk.Label(root, text=f'Exibindo os jogadores com prefixo {prefixo}', font=("Helvetica", 16, "bold"))
            output = player(prefixo)
            titulo.pack()
            textoWidget.pack()
            voltar_button.pack()
            textoWidget.delete("1.0", tk.END)
            for i in output:
                textoWidget.insert(tk.END, f'{i}\n')

        elif comando[0] == 'tags':
            lista_tags = [x.replace("'", '').capitalize() for x in comando[1:]]
            output = tags(lista_tags)
            formatado = ' '.join([f'{tag}' for tag in lista_tags])
            titulo = tk.Label(root, text=f'Exibindo os jogadores com as tags {formatado}', font=("Helvetica", 16, "bold"))
            titulo.pack()
            textoWidget.pack()
            voltar_button.pack()
            textoWidget.delete("1.0", tk.END)
            for i in output:
                textoWidget.insert(tk.END, f'{i}\n')
        else:
            titulo = tk.Label(root, text=f'Comando inválido!', font=("Helvetica", 16, "bold"))
            titulo.pack()
            voltar_button.pack()
    except IndexError:
        titulo = tk.Label(root, text=f'Insira um comando ou encerre o programa!', font=("Helvetica", 16, "bold"))
        titulo.pack()
        voltar_button.pack()

    # Limpar a caixa de comando
    comando_entry.delete(0, tk.END)

def voltar_tela_anterior():
    # Aqui você pode adicionar a lógica para voltar à tela anterior
    
    global titulo, voltar_button, textoWidget

    # Primeiro, remova os widgets da tela atual
    titulo.pack_forget()
    voltar_button.pack_forget()
    textoWidget.pack_forget()
    
    # Em seguida, restaure os widgets da tela anterior
    titulo_label.pack()
    subtitulo_label.pack()
    comando_label.pack()
    menu_label.pack()
    comando_entry.pack()
    iniciar_button.pack()
    encerrar_button.pack()

start = time.time()

print('Processando os dados...')
processamento(r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\minirating.csv", 
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
iniciar_button = tk.Button(root, text="Realizar consulta", command=processar_comando)
encerrar_button = tk.Button(root, text="Encerrar programa", command=root.destroy, fg="red")

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
