import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar as imagens com caminhos corrigidos
colorida = cv2.imread('C:/Users/Pedro Franco/Downloads/Histogramas/imagemColorida.jpg')
cinza = cv2.imread('C:/Users/Pedro Franco/Downloads/Histogramas/tonDeCinza.jpg', cv2.IMREAD_GRAYSCALE)

# Verificar se as imagens foram carregadas corretamente
if colorida is None or cinza is None:
    print("Erro ao carregar as imagens. Verifique os caminhos e tente novamente.")
    exit()

# Gerar histograma para a imagem em tons de cinza
hist_cinza = cv2.calcHist([cinza], [0], None, [256], [0, 256])

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cinza, cmap='gray')
plt.title('Imagem em Tons de Cinza')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.plot(hist_cinza, color='black')
plt.title('Histograma - Tons de Cinza')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')

plt.show()

# Gerar histogramas para a imagem colorida (R, G, B)
canais = ('b', 'g', 'r')
plt.figure(figsize=(15, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(colorida, cv2.COLOR_BGR2RGB))
plt.title('Imagem Colorida')
plt.axis('off')

plt.subplot(1, 2, 2)
for i, canal in enumerate(canais):
    hist = cv2.calcHist([colorida], [i], None, [256], [0, 256])
    plt.plot(hist, label=f'Canal {canal.upper()}', color=canal)
plt.title('Histogramas - Canais de Cor (RGB)')
plt.xlabel('Intensidade')
plt.ylabel('Frequência')
plt.legend()

plt.show()
