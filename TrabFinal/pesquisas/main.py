from arquivos import processamento
import time
import tkinter as tk
from tkinter import ttk
from funcoes import player, user, tags, posicao

titulo = voltar_button = None

# Função para realizar a ação de acordo com o comando inserido
def processar_comando():

    for i in widgetsIniciais:
        i.pack_forget()
   
    global titulo, voltar_button, arvore, scrollbar

    comando = comando_entry.get()
    comando = [x.lower() for x in comando.split()]

    voltar_button = tk.Button(root, text="Realizar nova consulta", command=voltar_tela_anterior)
    flag = True

    try:
        if comando[0] == 'user':
            id = int(comando[1])
            output = user(id)

            titulo = tk.Label(root, text=f'Exibindo os 20 jogadores mais bem avaliados pelo usuário {id}', font=("Helvetica", 16, "bold"))
            colunas = ('FIFA ID', 'Nome', 'Global Rating', 'Count', 'Rating')
            arvore = ttk.Treeview(root, columns = colunas, show='headings')

            for i in colunas:
                arvore.heading(i, text = i)

            arvore.column('FIFA ID', width= 20)
            arvore.column('Global Rating', width = 10)
            arvore.column('Count', width = 10)
            arvore.column('Rating', width = 10)
   


        elif 'top' in comando[0]:
            n = int(comando[0][3:])
            pos = comando[1].upper().replace("'", '')
            output = posicao(n, pos)

            titulo = tk.Label(root, text=f'Exibindo os {n} melhores jogadores da posição {pos}', font=("Helvetica", 16, "bold"))
            
            colunas = ('FIFA ID', 'Nome', 'Posições', 'Rating', 'Count')

            arvore = ttk.Treeview(root, columns = colunas, show='headings')

            for i in colunas:
                arvore.heading(i, text = i)
            arvore.column('FIFA ID', width= 20)
            arvore.column('Rating', width = 10)
            arvore.column('Count', width = 10)
            arvore.column('Posições', width = 30)

        elif comando[0] == 'player':
            prefixo = comando[1].capitalize()

            titulo = tk.Label(root, text=f'Exibindo os jogadores com prefixo {prefixo}', font=("Helvetica", 16, "bold"))

            output = player(prefixo)

            colunas = ('FIFA ID', 'Nome', 'Posições', 'Global Rating', 'Count', 'Nacionalidade', 'Clube', 'Liga')
            arvore = ttk.Treeview(root, columns = colunas, show='headings')

            for i in colunas:
                arvore.heading(i, text = i)

            arvore.column('FIFA ID', width= 20)
            arvore.column('Global Rating', width = 10)
            arvore.column('Count', width = 10)
            arvore.column('Posições', width = 30)
            arvore.column('Nacionalidade', width = 30)


        elif comando[0] == 'tags':
            lista_tags = [x.replace("'", '').capitalize() for x in comando[1:]]
            output = tags(lista_tags)
            formatado = ' '.join([f'{tag}' for tag in lista_tags])

            titulo = tk.Label(root, text=f'Exibindo os jogadores com as tags {formatado}', font=("Helvetica", 16, "bold"))

            colunas = ('FIFA ID','Nome','Posições','Rating','Count','Nacionalidade','Clube','Liga')
            arvore = ttk.Treeview(root, columns = colunas, show='headings')
            for i in colunas:
                arvore.heading(i, text = i)

            arvore.column('FIFA ID', width= 20)
            arvore.column('Rating', width = 20)
            arvore.column('Count', width = 10)
            arvore.column('Posições', width = 30)
            arvore.column('Nacionalidade', width = 30)
        else:
            titulo = tk.Label(root, text=f'Comando inválido!', font=("Helvetica", 16, "bold"))
            titulo.pack()
            voltar_button.pack()
            flag = False

        if flag:
            titulo.pack()
            arvore.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            arvore.pack(fill="both", expand=True)
            scrollbar.config(command=arvore.yview)

            voltar_button.pack()
        
        for i in output:
            arvore.insert('', 'end', values=i)

    except IndexError:
        titulo = tk.Label(root, text=f'Insira um comando ou encerre o programa!', font=("Helvetica", 16, "bold"))
        titulo.pack()
        voltar_button.pack()

    # Limpar a caixa de comando
    comando_entry.delete(0, tk.END)

def voltar_tela_anterior():
    global titulo, voltar_button, arvore, scrollbar

    # Remover os widgets da tela atual
    titulo.pack_forget()
    voltar_button.pack_forget()
    arvore.pack_forget()
    scrollbar.pack_forget()
    
    # Restaurar os widgets da tela anterior
    for i in widgetsIniciais:
        i.pack()

start = time.time()

print('Processando os dados...')
processamento(r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\rating.csv", 
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\players.csv",
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\dados\tags.csv",
              r"C:\Users\biaso\Desktop\UFRGS\semestre3\cpd\Classificacao_e_Pesquisa_de_Dados\TrabFinal\pesquisas\playersExtras.csv")

end = time.time()
tempo_total = end - start
print(f' {tempo_total:.2f}s para processar os dados')


# Criar a janela principal
root = tk.Tk()
root.title('Consulta aos Jogadores')
root.geometry(f'{1300}x{600}')

arvore = ttk.Treeview(root, columns = [], show='headings')
scrollbar = ttk.Scrollbar(root, orient="vertical", command=arvore.yview)

titulo_label = tk.Label(root, text="Consulta aos dados dos jogadores de futebol", font=("Helvetica", 16, "bold"))
subtitulo_label = tk.Label(root, text="Beatriz Soviero e Laís Canabarro", font=("Helvetica", 12))

comando_label = tk.Label(root, text="Comandos disponíveis", font=("Helvetica", 12))


menu_label = tk.Label(root, text=" \
                                1 - player <prefixo> : retorna todos os jogadores com o prefixo informado\n \
                                2 - user <user_id>: retorna os 20 jogadores mais bem avaliados pelo usuário com a ID informada\n \
                                3 - top<n> <posição>: retorna os melhores n jogadores que jogam na posição informada\n \
                                4 - tags <lista de tags>: retorna os jogadores que possuem todas as tags informadas", font=("Helvetica", 10), justify='left')
comando_entry = tk.Entry(root, width=50)
iniciar_button = tk.Button(root, text="Realizar consulta", command=processar_comando)
encerrar_button = tk.Button(root, text="Encerrar programa", command=root.destroy, fg="red")

widgetsIniciais = [titulo_label, subtitulo_label, comando_label, menu_label, comando_entry, iniciar_button, encerrar_button]

for i in widgetsIniciais:
    i.pack()

# Iniciar a interface
root.mainloop()
