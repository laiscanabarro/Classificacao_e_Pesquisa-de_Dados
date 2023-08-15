import requests
import tkinter as tk
from PIL import ImageTk
from PIL import Image
from io import BytesIO

def obter_dados_jogador(nome_jogador):
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=Lionel%20Messi"
    response = requests.get(url)
    data = response.json()
    
    if 'player' in data and data['player']:
        return data['player'][0]
    else:
        return None

def exibir_foto_jogador():
    nome_jogador = 'Lionel%20Messi'
    # nome_jogador = entry_nome.get()
    jogador = obter_dados_jogador(nome_jogador)
    foto_url = jogador['strThumb']
    
    response = requests.get(foto_url)
    imgData =response.content
    img = Image.open(BytesIO(imgData))
    img=ImageTk.PhotoImage(img)
    # Atualizar o rótulo com a nova imagem
    label_imagem.config(image=img)
    label_imagem.image = img  # Mantenha uma referência para evitar a coleta de lixo

    

janela = tk.Tk()
janela.title("Exibição de Imagem")

# Criar um rótulo para exibir a imagem
label_imagem = tk.Label(janela)
label_imagem.pack()

# Criar um botão para carregar e exibir a imagem
botao_carregar = tk.Button(janela, text="Carregar Imagem", command=exibir_foto_jogador)
botao_carregar.pack()

# Iniciar o loop principal da janela
janela.mainloop()