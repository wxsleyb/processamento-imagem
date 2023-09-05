import cv2
import numpy as np
import matplotlib.pyplot as plt

input_file = "img/mbappe.jpeg"
imagem = cv2.imread(input_file) 

def obter_dimensoes_imagem(imagem):
    largura = imagem.shape[1]
    altura = imagem.shape[0]
    num_canais = imagem.shape[2]
    return largura, altura, num_canais

# Obter dimensões da imagem
largura, altura, num_canais = obter_dimensoes_imagem(imagem)
print("Largura em pixels:", largura)
print("Altura em pixels:", altura)
print("Quantidade de canais:", num_canais)


def criar_canal_cor(imagem, canal):
    canal_img = np.zeros_like(imagem, dtype=np.uint8)
    canal_img[:, :, canal] = imagem[:, :, canal]
    return canal_img

# Criar canais de cores separados
canal_blue = criar_canal_cor(imagem, 0)
canal_green = criar_canal_cor(imagem, 1)
canal_red = criar_canal_cor(imagem, 2)

cv2.imwrite("ImagemAzul.jpg", canal_blue)
cv2.imwrite("ImagemVerde.jpg", canal_green)
cv2.imwrite("ImagemVermelha.jpg", canal_red)

def calcular_histograma(imagem, canal):
    hist = [0] * 256

    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            valor_pixel = imagem[i][j][canal]
            hist[valor_pixel] += 1

    return hist

# Calcular histograma para o canal azul
histBlue = calcular_histograma(imagem, 0)

# Calcular histograma para o canal vermelho
histRed = calcular_histograma(imagem, 2)

# Calcular histograma para o canal verde
histGreen = calcular_histograma(imagem, 1)

# Plote os histogramas
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.title("Histograma Azul")
plt.bar(range(256), histBlue, color='blue', alpha=0.7)
plt.subplot(132)
plt.title("Histograma Vermelho")
plt.bar(range(256), histRed, color='red', alpha=0.7)
plt.subplot(133)
plt.title("Histograma Verde")
plt.bar(range(256), histGreen, color='green', alpha=0.7)
plt.show()


# Função para calcular o histograma em tons de cinza
def calcular_histograma_cinza(imagem):
    if len(imagem.shape) == 3:
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        imagem_cinza = imagem
    hist = cv2.calcHist([imagem_cinza], [0], None, [256], [0, 256])
    return hist

# Calcular o histograma em tons de cinza
histGrey = calcular_histograma_cinza(imagem)

# Criar o eixo x
pixel = np.arange(256)

# Título do gráfico
plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da Imagem em Tons de Cinza')
plt.bar(pixel, histGrey.ravel(), color='gray')
plt.show()

# # Função para aplicar a limiarização multinível
# def limiarizacao_multinivel(imagem):
#     imagem_limiarizada = np.copy(imagem)
    
#     for i in range(imagem.shape[0]):
#         for j in range(imagem.shape[1]):
#             pixel = imagem[i][j]
#             if (pixel >= 80 and pixel <= 120) or (pixel < 25 or pixel > 235):
#                 imagem_limiarizada[i][j] = 255
#             else:
#                 imagem_limiarizada[i][j] = 0
    
#     return imagem_limiarizada

# # Aplicar a limiarização multinível
# imagem_limiarizada = limiarizacao_multinivel(imagem)

# # Exibir a imagem limiarizada
# plt.imshow(imagem_limiarizada, cmap='gray')
# plt.title('Imagem Limiarizada')
# plt.axis('off')
# plt.show()


# Função para transformar em branco os valores fora do intervalo (80, 120)
# def transformar_fora_intervalo_em_branco(imagem):
#     imagem_resultado = np.copy(imagem)
    
#     for i in range(imagem.shape[0]):
#         for j in range(imagem.shape[1]):
#             pixel = imagem[i][j]
#             if pixel < 80 or pixel > 120:
#                 imagem_resultado[i][j] = 255
    
#     return imagem_resultado

# # Aplicar a transformação em branco
# imagem_transformada = transformar_fora_intervalo_em_branco(imagem)

# # Exibir a imagem resultante
# cv2.imshow('Cinza e o resto branco', imagem_transformada)
# cv2.imwrite("CinzaRestoBranco.jpg", imagem_transformada)

# # Esperar até que uma tecla seja pressionada e depois fechar a janela
# cv2.waitKey(0)
# cv2.destroyAllWindows()

imagem = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE) 


# Defina os valores de contraste (c) e luminosidade (l)
c = 1
l = 50

# def aplicar_brilho_contraste(imagem, c, l):
#     # Crie uma imagem de destino com as mesmas dimensões da imagem original
#     imagem_destino = np.zeros_like(imagem, dtype=np.uint8)

#     # Aplicar a transformação de brilho e contraste
#     imagem_destino = cv2.convertScaleAbs(imagem, alpha=c, beta=l)

#     # Certifique-se de que os valores dos pixels estejam no intervalo válido (0-255)
#     imagem_destino = np.clip(imagem_destino, 0, 255)

#     return imagem_destino

# def dobrar_contraste(imagem):
#     # Defina a imagem de destino como o dobro do valor de pixel da imagem original
#     imagem_destino = 2 * imagem

#     # Certifique-se de que os valores dos pixels estejam no intervalo válido (0-255)
#     imagem_destino = np.clip(imagem_destino, 0, 255)

#     return imagem_destino

# def ajustar_luminosidade(imagem, valor):
#     # Crie uma imagem de destino com as mesmas dimensões da imagem original
#     imagem_destino = np.zeros_like(imagem, dtype=np.uint8)

#     # Aplicar o ajuste de luminosidade
#     imagem_destino = imagem + valor

#     # Certifique-se de que os valores dos pixels estejam no intervalo válido (0-255)
#     imagem_destino = np.clip(imagem_destino, 0, 255)

#     return imagem_destino



# # Aplicar as transformações de brilho e contraste, dobrar o contraste e ajustar a luminosidade
# imagem_brilho_contraste = aplicar_brilho_contraste(imagem, 1, 50)
# imagem_dobro_contraste = dobrar_contraste(imagem)
# imagem_luminosidade_100 = ajustar_luminosidade(imagem, 100)

# # Salvar as imagens resultantes
# cv2.imwrite("ImagemBrilhoContraste.jpg", imagem_brilho_contraste)
# cv2.imwrite("ImagemDobroContraste.jpg", imagem_dobro_contraste)
# cv2.imwrite("Imagem100Luminosidade.jpg", imagem_luminosidade_100)

# # Valores de entrada
# entrada = np.arange(256)  # Valores de 0 a 255

# # Função de brilho e contraste
# c_brilho_contraste = 1
# l_brilho_contraste = 50
# saida_brilho_contraste = aplicar_brilho_contraste(entrada, c_brilho_contraste, l_brilho_contraste)

# # Função de dobrar o contraste
# saida_dobro_contraste = dobrar_contraste(entrada)

# # Função de ajustar a luminosidade
# valor_luminosidade = 100
# saida_luminosidade = ajustar_luminosidade(entrada, valor_luminosidade)

# # Plotar as curvas
# plt.figure(figsize=(12, 4))

# plt.subplot(131)
# plt.plot(entrada, saida_brilho_contraste, label='Brilho e Contraste')
# plt.xlabel('Entrada')
# plt.ylabel('Saída')
# plt.title('Curva de Brilho e Contraste')
# plt.legend()

# plt.subplot(132)
# plt.plot(entrada, saida_dobro_contraste, label='Dobrar Contraste', color='orange')
# plt.xlabel('Entrada')
# plt.ylabel('Saída')
# plt.title('Curva de Dobrar Contraste')
# plt.legend()

# plt.subplot(133)
# plt.plot(entrada, saida_luminosidade, label='Ajustar Luminosidade', color='green')
# plt.xlabel('Entrada')
# plt.ylabel('Saída')
# plt.title('Curva de Ajustar Luminosidade')
# plt.legend()

# plt.tight_layout()
# plt.show()


# def aplicar_curva_parabolica(imagem):
#     # Crie uma imagem de destino com as mesmas dimensões da imagem original
#     imagem_destino = np.zeros_like(imagem, dtype=np.uint8)

#     # Aplicar a transformação de curva parabólica
#     imagem_destino = (((1/256) * imagem) ** 2) * 256

#     # Certifique-se de que os valores dos pixels estejam no intervalo válido (0-255)
#     imagem_destino = np.clip(imagem_destino, 0, 255)

#     return imagem_destino

# def aplicar_curva_negativa(imagem):
#     # Crie uma imagem de destino com as mesmas dimensões da imagem original
#     imagem_destino = np.zeros_like(imagem, dtype=np.uint8)

#     # Aplicar a transformação de curva negativa
#     imagem_destino = 255 - imagem

#     return imagem_destino

def plotar_curva_de_tom(x, y, titulo, cor):
    plt.xlabel('Origem - R')
    plt.ylabel('Destino - S') 
    plt.title(titulo)
    plt.plot(x, y, color=cor)
    plt.show()


# # Aplicar a transformação de curva parabólica
# imagem_curva_parabolica = aplicar_curva_parabolica(imagem)
# x = np.arange(256)
# y = (((1/256) * x) ** 2) * 256
# plotar_curva_de_tom(x, y, 'Curva de Tom Parabólica', 'green')

# # Salvar a imagem resultante da curva parabólica
# cv2.imwrite("ImagemParabolica.jpg", imagem_curva_parabolica)

# # Aplicar a transformação de curva negativa
# imagem_curva_negativa = aplicar_curva_negativa(imagem)
# x = np.arange(256)
# y = 255 - x
# plotar_curva_de_tom(x, y, 'Curva de Tom Negativa', 'red')

# # Salvar a imagem resultante da curva negativa
# cv2.imwrite("ImagemNegativa.jpg", imagem_curva_negativa)


def expandir_histograma_c_l(imagem, c, l):
    # Crie uma imagem de destino com as mesmas dimensões da imagem original
    imagem_expandida = np.zeros_like(imagem, dtype=np.uint8)

    # Aplicar a expansão do histograma usando os valores c e l
    imagem_expandida = c * imagem + l

    # Certifique-se de que os valores dos pixels estejam no intervalo válido (0-255)
    imagem_expandida = np.clip(imagem_expandida, 0, 255)

    return imagem_expandida

def expandir_histograma_r1_r2_s1_s2(imagem, r1, r2, s1, s2):
    # Crie uma imagem de destino com as mesmas dimensões da imagem original
    imagem_expandida = np.zeros_like(imagem, dtype=np.uint8)

    # Aplicar a expansão do histograma usando os valores r1, r2, s1 e s2
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            if imagem[i][j] <= r1:
                imagem_expandida[i][j] = (s1 / r1) * imagem[i][j]
            elif imagem[i][j] >= r2:
                imagem_expandida[i][j] = (imagem[i][j] - r2) * ((s2 - s1) / (255 - r2)) + s1
            else:
                imagem_expandida[i][j] = (((imagem[i][j] - r1) * (s2 - s1)) / (r2 - r1)) + s1

    # Certifique-se de que os valores dos pixels estejam no intervalo válido (0-255)
    imagem_expandida = np.clip(imagem_expandida, 0, 255)

    return imagem_expandida

# Aplicar expansão de histograma com c e l
imagem_expandida_cl = expandir_histograma_c_l(imagem, 2, 100)

# Aplicar expansão de histograma com r1, r2, s1 e s2
imagem_expandida_r1_r2_s1_s2 = expandir_histograma_r1_r2_s1_s2(imagem, 50, 230, 500, 3500)

# Plote os histogramas das imagens expandidas
plt.figure(figsize=(12, 4))

plt.subplot(121)
plt.hist(imagem_expandida_cl.ravel(), bins=256, range=(0, 256), color='red', alpha=0.5, label='c=2, l=100')
plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da Imagem Expandida (c e l)')
plt.legend()

plt.subplot(122)
plt.hist(imagem_expandida_r1_r2_s1_s2.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.5, label='r1=50, r2=230, s1=500, s2=3500')
plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da Imagem Expandida (r1, r2, s1, s2)')
plt.legend()

plt.tight_layout()
plt.show()