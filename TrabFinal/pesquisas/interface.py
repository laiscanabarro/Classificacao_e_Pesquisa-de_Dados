import tkinter as tk
import requests
from funcoes import player, user, tags, posicao
from arquivos import *
import time
from PIL import ImageTk
from PIL import Image
from io import BytesIO

titulo = voltar_button = textoWidget = labelImagem = None


def obter_dados_jogador(nome_jogador):
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={nome_jogador}"
    response = requests.get(url)
    data = response.json()
    
    if 'player' in data and data['player']:
        return data['player'][0]
    else:
        return None

def exibe_foto_jogador(nome_jogador):

    jogador = obter_dados_jogador(nome_jogador)
    
    foto_url = jogador['strThumb']

    try:
        response = requests.get(foto_url)
        imgData =response.content
        img = Image.open(BytesIO(imgData))
        img = img.resize((50,50))
        img=ImageTk.PhotoImage(img)
    except requests.exceptions.MissingSchema:
        img = ImageTk.PhotoImage(file = 'semFoto.jpg')

    # Atualizar o rótulo com a nova imagem

    global labelImagem
    labelImagem = tk.Label(root)
    labelImagem.config(image=img)
    labelImagem.image = img  # Mantenha uma referência para evitar a coleta de lixo
    return img

# Função para realizar a ação de acordo com o comando inserido
def processar_comando():

    for i in widgetsIniciais:
        i.pack_forget()
   
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
                textoWidget.image_create(tk.END, image = exibe_foto_jogador(i[5]))
                for j in range(len(i)-1):
                    textoWidget.insert(tk.END, i[j] + '\n')

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
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\tags.csv",
              "playersExtras.csv")

end = time.time()
tempo_total = end - start
print(f' {tempo_total:.2f}s para processar os dados')


# Criar a janela principal
root = tk.Tk()
root.title('Consulta aos Jogadores')
root.geometry(f'{800}x{600}')

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

widgetsIniciais = [titulo_label, subtitulo_label, comando_label, menu_label, comando_entry, iniciar_button, encerrar_button]

for i in widgetsIniciais:
    i.pack()

# Iniciar a interface
root.mainloop()
