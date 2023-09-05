import cv2
import numpy as np
import matplotlib.pyplot as plt  # Importando Matplotlib

# O nome da variável "input" foi alterado para "input_file" para evitar conflito com a palavra-chave "input".
input_file = 'mbappe.jpeg'

# Carregar a imagem
imagem = cv2.imread(input_file)

if imagem is not None:
    largura = imagem.shape[1]
    altura = imagem.shape[0]
    num_canais = imagem.shape[2]
    print("Largura da imagem:", largura)
    print("Altura da imagem:", altura)
    print("Número de canais:", num_canais)
else:
    print("Erro ao carregar a imagem.")


def criar_canal_cor(imagem, canal):
    canal_img = np.zeros_like(imagem, dtype=np.uint8)
    canal_img[:, :, canal] = imagem[:, :, canal]
    return canal_img

# Criar canais de cores separados
canal_blue = criar_canal_cor(imagem, 0)
canal_green = criar_canal_cor(imagem, 1)
canal_red = criar_canal_cor(imagem, 2)

def converter_para_preto_e_branco(imagem):
    altura, largura, _ = imagem.shape
    canalPretoBranco = np.zeros((altura, largura), dtype=np.uint8)

    for i in range(altura):
        for j in range(largura):
            canalPretoBranco[i][j] = imagem[i][j].sum() // 3

    return canalPretoBranco

# Chame a função para converter a imagem em preto e branco
imagem_preto_branco = converter_para_preto_e_branco(imagem)

# Salve a imagem em preto e branco
cv2.imwrite("saidapretobranco.jpeg", imagem_preto_branco)



histGrey = [0]*256
histBlue = [0]*256
histGreen = [0]*256
histRed = [0]*256

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         canalPretoBranco[i][j] = (imagem[i][j].sum()//3)
#         histGrey [canalPretoBranco[i][j]]+=1
# print(histGrey, end='')

for i in range(canalBlue.shape[0]):
    for j in range(canalBlue.shape[1]):
        histBlue [imagem[i][j][0]]+=1
print(histBlue, end='')

for i in range(canalRed.shape[0]):
    for j in range(canalRed.shape[1]):
        histRed [imagem[i][j][1]]+=1
print(histRed, end='')

for i in range(canalGreen.shape[0]):
    for j in range(canalGreen.shape[1]):
        histGreen [imagem[i][j][2]]+=1
print(histGreen, end='')


#HISTOGRAMA CANAL CINZA
#criar o eixo x
pixel = [0]*256
for i in range(256):
    pixel[i] = i

#Título do gráfico
plt.xlabel('Pixel')
plt.ylabel('Quantidade') 
plt.title('Histograma da Imagem em tons de CINZA')
plt.bar(pixel, histGrey, color='grey');



# #Título do gráfico
# plt.xlabel('Pixel')
# plt.ylabel('Quantidade') 
# plt.title('Histograma da Imagem em tons de AZUL')
# plt.bar(pixel, histBlue, color='blue');

# #Título do gráfico
# plt.xlabel('Pixel')
# plt.ylabel('Quantidade') 
# plt.title('Histograma da Imagem em tons de VERMELHO')
# plt.bar(pixel, histRed, color='red');

# #Título do gráfico
# plt.xlabel('Pixel')
# plt.ylabel('Quantidade') 
# plt.title('Histograma da Imagem em tons de VERDE')
# plt.bar(pixel, histGreen, color='green');

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]<= 120:
#             canalPretoBranco[i][j] = 255
                       
# cv2.imshow('Canal So Branco', canalPretoBranco)
# cv2.imwrite("ImagemSoBranca.jpg", canalPretoBranco)

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         histGrey[canalPretoBranco[i][j]]+=1
# print(histGrey, end='')


# plt.xlabel('Pixel')
# plt.ylabel('Quantidade') 
# plt.title('Histograma da Imagem Só Branco')
# plt.bar(pixel, histGrey, color='grey');


# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]>= 120:
#             canalPretoBranco[i][j] = 255
                       

# cv2.imshow('Canal So Preto', canalPretoBranco)
# cv2.imwrite("ImagemSoPreta.jpg", canalPretoBranco)


# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         histGrey[canalPretoBranco[i][j]]+=1
# print(histGrey, end='')


# plt.xlabel('Pixel')
# plt.ylabel('Quantidade') 
# plt.title('Histograma da Imagem Só Preto')
# plt.bar(pixel, histGrey, color='grey');

#quando a imagem tem mais de dois objetos cinzas diferentes, em um fundo mais escuro, 
#pode ser usada a técnica de limiarização multinivel (multilevel thresholding)
# entre 80 e 120 transformar em branco  e menor que 25 e maior que 235

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]>= 80 and canalPretoBranco[i][j]<= 120:
#             canalPretoBranco[i][j] = 255
                       

# cv2.imshow('Transforma cinza em branco', canalPretoBranco)
# cv2.imwrite("TransformaCinzaEmBranco.jpg", canalPretoBranco)

# # for i in range(imagem.shape[0]):
# #     for j in range(imagem.shape[1]):
# #         histGrey[canalPretoBranco[i][j]]+=1
# # print(histGrey, end='')


# # plt.xlabel('Pixel')
# # plt.ylabel('Quantidade') 
# # plt.title('Histograma da Imagem Cinza em Branco')
# # plt.bar(pixel, histGrey, color='grey');



# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]<= 25 or canalPretoBranco[i][j]>= 225:
#             canalPretoBranco[i][j] = 255
                       

# cv2.imshow('Transforma cores em branco', canalPretoBranco)
# cv2.imwrite("TransformaCoresEmBranco.jpg", canalPretoBranco)

# # for i in range(imagem.shape[0]):
# #     for j in range(imagem.shape[1]):
# #         histGrey[canalPretoBranco[i][j]]+=1
# # print(histGrey, end='')


# # plt.xlabel('Pixel')
# # plt.ylabel('Quantidade') 
# # plt.title('Histograma da Imagem Só Preto')
# # plt.bar(pixel, histGrey, color='grey');


# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]<= 25 or canalPretoBranco[i][j]>= 225:
#             canalPretoBranco[i][j] = 150
                       

# cv2.imshow('Transforma cores em cinza', canalPretoBranco)
# cv2.imwrite("TransformaCoresEmCinza.jpg", canalPretoBranco)



# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]<= 80 and canalPretoBranco[i][j]=> 120
#             canalPretoBranco[i][j] = 255
                       

# cv2.imshow('Cinza e o resto branco', canalPretoBranco)
# cv2.imwrite("CinzaRestoBranco.jpg", canalPretoBranco)

#c contraste, r= pixel da imagem original , l = lumininosidade, s= pixel da imagem mudada
#f(r) = s = cr + l
c = 1
l = 500


imagemDestino =  np.zeros((imagem.shape[0], imagem.shape[1]), dtype = np.uint8)

# y = 256*[0]
# x = 256*[0]
# for i in range(256):
#     x[i] = i
#     y[i] = i
#     y[i] = c*y[i] + l
#     if y[i]>255:
#         y[i] = 255
#     if y[i] < 0:
#         y[i]=0

# # plt.figure()

# plt.xlabel('Origem - R')
# plt.ylabel('Destino - S') 
# plt.title('Curva de Tom de Brilho e Contraste')
# plt.plot(x, y, color='blue');
# plt.show()


# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]>255:
#             canalPretoBranco[i][j] = 255
#         if canalPretoBranco[i][j]< 0:
#             canalPretoBranco[i][j] = 0
#         imagemDestino[i][j] = c*canalPretoBranco[i][j] + l

# cv2.imwrite("ImagemBrilhoConstraste.jpg", imagemDestino)
# cv2.waitKey(0) #só pode ter um  waitkey no programa

# y = 256*[0]
# x = 256*[0]
# for i in range(256):
#     x[i] = i
#     y[i] = i
#     y[i] = 2*y[i]
#     if y[i]>255:
#         y[i] = 255
#     if y[i] < 0:
#         y[i]=0

# plt.figure()

# plt.xlabel('Origem - R')
# plt.ylabel('Destino - S') 
# plt.title('Curva de Tom Dobro Constraste')
# plt.plot(x, y, color='black');
# plt.show()

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]>255:
#             canalPretoBranco[i][j] = 255
#         if canalPretoBranco[i][j]< 0:
#             canalPretoBranco[i][j] = 0
#         imagemDestino[i][j] = 2*canalPretoBranco[i][j]
         
# cv2.imwrite("ImagemDobroConstraste.jpg", imagemDestino)


# y = 256*[0]
# x = 256*[0]
# for i in range(256):
#     x[i] = i
#     y[i] = i
#     y[i] = y[i] + 100
#     if y[i]>255:
#         y[i] = 255
#     if y[i] < 0:
#         y[i]=0


# plt.xlabel('Origem - R')
# plt.ylabel('Destino - S') 
# plt.title('Curva de Tom Luminosidade 100')
# plt.plot(x, y, color='pink');
# plt.show()


# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]>255:
#             canalPretoBranco[i][j] = 255
#         if canalPretoBranco[i][j]< 0:
#             canalPretoBranco[i][j] = 0
#         imagemDestino[i][j] = canalPretoBranco[i][j] + 100
         
# cv2.imwrite("Imagem100Luminosidade.jpg", imagemDestino)


# y = 256*[0]
# x = 256*[0]
# for i in range(256):
#     x[i] = i
#     y[i] = i
#     y[i] = ((1/256)*y[i])**2
#     if y[i]>255:
#         y[i] = 255
#     if y[i] < 0:
#         y[i]=0


# plt.xlabel('Origem - R')
# plt.ylabel('Destino - S') 
# plt.title('Curva de Tom Parabólica')
# plt.plot(x, y, color='green');
# plt.show()

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]>255:
#             canalPretoBranco[i][j] = 255
#         if canalPretoBranco[i][j]< 0:
#             canalPretoBranco[i][j] = 0
#         imagemDestino[i][j] = (((1/256)*canalPretoBranco[i][j])**2)*256
         
# cv2.imwrite("ImagemParabolica.jpg", imagemDestino)


# y = 256*[0]
# x = 256*[0]
# for i in range(256):
#     x[i] = i
#     y[i] = i
#     y[i] = 255-y[i]
#     if y[i]>255:
#         y[i] = 255
#     if y[i] < 0:
#         y[i]=0


# plt.xlabel('Origem - R')
# plt.ylabel('Destino - S') 
# plt.title('Curva de Tom Negativa')
# plt.plot(x, y, color='red');
# plt.show()

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]>255:
#             canalPretoBranco[i][j] = 255
#         if canalPretoBranco[i][j]< 0:
#             canalPretoBranco[i][j] = 0
#         imagemDestino[i][j] = 255 - canalPretoBranco[i][j]
         
# cv2.imwrite("ImagemNegativa.jpg", imagemDestino)

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         if canalPretoBranco[i][j]>255:
#             canalPretoBranco[i][j] = 255
#         if canalPretoBranco[i][j]< 0:
#             canalPretoBranco[i][j] = 0
#         imagemDestino[i][j] = c*canalPretoBranco[i][j] + l

####HISTOGRAMA EXPANDIDO
imagemExpandida = np.zeros((imagem.shape[0], imagem.shape[1]), dtype = np.uint8)


for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if canalPretoBranco[i][j]>255:
            canalPretoBranco[i][j] = 255
        if canalPretoBranco[i][j]< 0:
            canalPretoBranco[i][j] = 0
        imagemExpandida[i][j] = c*canalPretoBranco[i][j] + l

cv2.imwrite("img/ImagemBrilhoConstraste.jpg", imagemExpandida)


r1 = 50
r2 = 230
rmax = 255
s1 = 500
s2 = 3500
smax = 4000

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if canalPretoBranco[i][j] <= r1:
             imagemExpandida[i][j]= 0
        elif canalPretoBranco[i][j] >= r2:
            imagemExpandida[i][j] = 255
        else:
            imagemExpandida[i][j] = 255 *((canalPretoBranco[i][j] - r1)/(r2-r1))
cv2.imwrite("img/imagemExpandida.jpg", imagemExpandida)


pixel1 = [0]*256
for i in range(256):
    pixel1[i] = i


histExpandido = [0]*256

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        histExpandido [imagemExpandida[i][j]]+=1
print(histExpandido, end='')

plt.xlabel('Pixel')
plt.ylabel('Quantidade') 
plt.title('Histograma da Imagem Expandido')
plt.bar(pixel1, histExpandido, color='grey');

#########################

imagemExpandida2 = np.zeros((imagem.shape[0], imagem.shape[1]), dtype = np.uint8)
pixel2 = [0]*256
for i in range(256):
    pixel2[i] = i


for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if canalPretoBranco[i][j] <= r1:
             imagemExpandida2[i][j]= (s1/r1)*canalPretoBranco[i][j]
        elif canalPretoBranco[i][j] >= r2:
            imagemExpandida2[i][j] = (canalPretoBranco[i][j] - r2)*((smax-s2)/(rmax-r2))+ s2
        else:
            imagemExpandida2[i][j] = (((canalPretoBranco[i][j] - r1)*(s2-s1))/(r2-r1))+s1
cv2.imwrite("img/imagemExpandida2.jpg", imagemExpandida2)

histExpandido2 = [0]*256

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        histExpandido2 [imagemExpandida2[i][j]]+=1
print(histExpandido2, end='')

plt.xlabel('Pixel')
plt.ylabel('Quantidade') 
plt.title('Histograma da Imagem Expandido2')
plt.bar(pixel2, histExpandido2, color='blue');

cv2.waitKey(0) #só pode ter um  waitkey no programa

