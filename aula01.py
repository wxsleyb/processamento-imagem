import cv2
import numpy
import matplotlib.pyplot as plt #importing matplotlib

#instalar a biblioteca cv2 rodando no console/terminal 
#!pip install OpenCV-python

input = "mbappe.jpeg"

imagem = cv2.imread(input)

#largura imagem (qtd colunas da matriz)
print("Largura em pixels: ", end="")
print(imagem.shape[1]) #largur imagem

#altura da imagem (qtd de linhas matriz)
print("Altura em pixels: ", end='')
print(imagem.shape[0]) #altura imagem

#qtd de canais da imagem - img colorida possui 3 canais rgb
print('Qtde  de canais: ', end= '')
print(imagem.shape[2])


#pra mostrar todas as informaçoes da imagem no console
#imagem.shape #n linhas,colunas,canais img
#imagem.size #tamanho
#imagem.ndim #dimensoes

#retorna os respectivs valors das cores do pixel superior mis  esquerda
#(b ,g ,r ) = imagem[0, 0]
#(b,g,r)


#mostrar em azul

canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)

canalBlue[:,:,0] = imagem[:,:,0]
#cv2.imshow("canalblue.jpg", canalBlue)
#cv2.imwrite("saidaBlue.jpg", canalBlue)



#mostrar em vermelho
canalGreen = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)

canalGreen[:,:,1] = imagem[:,:,1]
#cv2.imshow("canal green", canalGreen)
#cv2.imwrite("saidaRed.jpg", canalGreen)



#mostrar em verde
canalRed = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8)

canalRed[:,:,2] = imagem[:,:,2]
#cv2.imshow("canal red", canalRed)
#cv2.imwrite("saidaGreen.jpg", canalRed)


#transformar a imagem em preto e branco
canalPretoBranco =  numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        canalPretoBranco[i][j] = (imagem[i][j].sum()//3) #tirar a media aritmética dos 3 canais rgb
       #canalPretoBranco[i][j] = numpy.mean(imagem[i][j])
#cv2.imshow('saidapretobranco',canalPretoBranco)
#cv2.imwrite("saidapretobranco.jpeg", canalPretoBranco)

imagemDestino =  numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype = numpy.uint8)


histGrey = [0]*256
histBlue = [0]*256
histGreen = [0]*256
histRed = [0]*256

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        canalPretoBranco[i][j] = (imagem[i][j].sum()//3)
        histGrey [canalPretoBranco[i][j]]+=1
print(histGrey, end='')

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

# #Título do gráfico
# plt.xlabel('Pixel')
# plt.ylabel('Quantidade') 
# plt.title('Histograma da Imagem em tons de CINZA')
# plt.bar(pixel, histGrey, color='grey');

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

#quando a imagem tem mais d edois objetos cinzas diferentes, em um fundo mais escuro, 
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

#c contraste, r= pixel da image original , l = lumininosidade, s= pixel da imagem mudada
#f(r) = s = cr + l
c = 1
l = 1000

#Mexe no contraste e luminosidade da imagem
# imagem_ajustada1 = imagem.copy()

# for i in range(imagem.shape[0]):
#     for j in range(imagem.shape[1]):
#         for channel in range(imagem.shape[2]):  # Iterate through each color channel (assuming RGB)
#             r = imagem[i, j, channel]
#             s = c * r + l

#             # Make sure pixel values are in the valid range (0 to 255)
#             s = max(0, min(s, 255))

#             imagem_ajustada1[i, j, channel] = s

# cv2.imshow('Imagem Ajustada', imagem_ajustada1)
# cv2.imwrite("ImagemAjustada.jpg", imagem_ajustada1)

y = 256*[0]
x = 256*[0]
for i in range(256):
    x[i] = i
    y[i] = i
    y[i] = c*y[i] + l
    if y[i]>255:
        y[i] = 255
    if y[i] < 0:
        y[i]=0

plt.figure()

plt.xlabel('Origem - R')
plt.ylabel('Destino - S') 
plt.title('Curva de Tom de Brilho e Contraste')
plt.plot(x, y, color='blue');
plt.show()


for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if canalPretoBranco[i][j]>255:
            canalPretoBranco[i][j] = 255
        if canalPretoBranco[i][j]< 0:
            canalPretoBranco[i][j] = 0
        imagemDestino[i][j] = c*canalPretoBranco[i][j] + l
         
cv2.imwrite("ImagemBrilhoConstraste.jpg", imagemDestino)

y = 256*[0]
x = 256*[0]
for i in range(256):
    x[i] = i
    y[i] = i
    y[i] = 2*y[i]
    if y[i]>255:
        y[i] = 255
    if y[i] < 0:
        y[i]=0

plt.figure()

plt.xlabel('Origem - R')
plt.ylabel('Destino - S') 
plt.title('Curva de Tom Dobro Constraste')
plt.plot(x, y, color='black');
plt.show()

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if canalPretoBranco[i][j]>255:
            canalPretoBranco[i][j] = 255
        if canalPretoBranco[i][j]< 0:
            canalPretoBranco[i][j] = 0
        imagemDestino[i][j] = 2*canalPretoBranco[i][j]
         
cv2.imwrite("ImagemDobroConstraste.jpg", imagemDestino)


y = 256*[0]
x = 256*[0]
for i in range(256):
    x[i] = i
    y[i] = i
    y[i] = y[i] + 100
    if y[i]>255:
        y[i] = 255
    if y[i] < 0:
        y[i]=0


plt.xlabel('Origem - R')
plt.ylabel('Destino - S') 
plt.title('Curva de Tom Luminosidade 100')
plt.plot(x, y, color='pink');
plt.show()


for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if canalPretoBranco[i][j]>255:
            canalPretoBranco[i][j] = 255
        if canalPretoBranco[i][j]< 0:
            canalPretoBranco[i][j] = 0
        imagemDestino[i][j] = canalPretoBranco[i][j] + 100
         
cv2.imwrite("Imagem100Luminosidade.jpg", imagemDestino)


y = 256*[0]
x = 256*[0]
for i in range(256):
    x[i] = i
    y[i] = i
    y[i] = ((1/256)*y[i])**2
    if y[i]>255:
        y[i] = 255
    if y[i] < 0:
        y[i]=0


plt.xlabel('Origem - R')
plt.ylabel('Destino - S') 
plt.title('Curva de Tom Parabólica')
plt.plot(x, y, color='green');
plt.show()

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if canalPretoBranco[i][j]>255:
            canalPretoBranco[i][j] = 255
        if canalPretoBranco[i][j]< 0:
            canalPretoBranco[i][j] = 0
        imagemDestino[i][j] = (((1/256)*canalPretoBranco[i][j])**2)*256
         
cv2.imwrite("ImagemParabolica.jpg", imagemDestino)


y = 256*[0]
x = 256*[0]
for i in range(256):
    x[i] = i
    y[i] = i
    y[i] = 255-y[i]
    if y[i]>255:
        y[i] = 255
    if y[i] < 0:
        y[i]=0


plt.xlabel('Origem - R')
plt.ylabel('Destino - S') 
plt.title('Curva de Tom Negativa')
plt.plot(x, y, color='red');
plt.show()

for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        if canalPretoBranco[i][j]>255:
            canalPretoBranco[i][j] = 255
        if canalPretoBranco[i][j]< 0:
            canalPretoBranco[i][j] = 0
        imagemDestino[i][j] = 255 - canalPretoBranco[i][j]
         
cv2.imwrite("ImagemNegativa.jpg", imagemDestino)

cv2.waitKey(0) #só pode ter um  waitkey no programa
