from PIL import Image, ImageDraw, ImageFont

# Criar uma imagem em branco de 75x75 pixels
imagem = Image.new('RGB', (75, 75), (255, 255, 255))  # Fundo branco

# Criar um objeto ImageDraw para desenhar na imagem
draw = ImageDraw.Draw(imagem)

# Especificar a fonte e o tamanho
fonte = ImageFont.load_default()  # Você pode usar outra fonte se preferir

# Escrever "Sem Foto" no centro da imagem
texto = "Sem Foto"
largura_media_caracter = sum(fonte.getsize(char)[0] for char in texto) / len(texto)
altura_caracter = fonte.getsize(texto)[1]
x = (75 - largura_media_caracter * len(texto)) // 2
y = (75 - altura_caracter) // 2
draw.text((x, y), texto, font=fonte, fill=(0, 0, 0))  # Cor do texto: preto

# Salvar a imagem
imagem.save('sem_foto.png')

# Exibir a imagem (opcional)
imagem.show()