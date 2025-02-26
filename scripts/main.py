import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import monoCV
from ultralytics import YOLO    #instalar com pip install ultralytics
import csv
import tkinter as tk
from tkinter import filedialog
import os

h = 0.1 #altura do cubesat é 10 cm
w = 0.1 #largura também
fx = monoCV.mat[0][0]  #1.14637048e+03
fy = monoCV.mat[1][1]  #1.13737781e+03
Cx = monoCV.mat[0][2]  #9.08576457e+02
Cy = monoCV.mat[1][2]  #5.68368717e+02
#alpha = 1920.00/1080.00
resolution = [1280,720]
alpha = 2448.00/2048.00
Sx = 5.555e-3 #2.2e-3
Sy = 3.125e-3 #2.2e-3
Fnet = 940  #valor de 94 mm encontrado em https://al-voip.com/products/logitech-c930e#:~:text=Maximum%20Focal%20Length%3A%2094%20Millimeters

caminho_vid = "C:/Users/vitor/OneDrive/Documentos One Drive/Python"

# Solicitar nome do arquivo CSV e vídeo
nome_arquivo = input("Nome do CSV e vídeo: ")
output_folder = nome_arquivo
nome_video = nome_arquivo + ".mp4"

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do tkinter
    arquivo = filedialog.askopenfilename(title="Selecione o vídeo de entrada", filetypes=[("Vídeos", "*.mp4 *.avi")])
    return arquivo

# Selecionar o arquivo de vídeo
caminho_vid = selecionar_arquivo()
if not caminho_vid:
    print("Nenhum vídeo selecionado. Encerrando...")
    exit()

def salvar_em_csv(tempo, x, y, w, h, X, Y, Z):
    # Lista dos parâmetros
    parametros = [tempo, x, y, w, h, X, Y, Z]
    nome_csv = nome_arquivo+".csv"
    # Abrir o arquivo CSV em modo de escrita
    with open(nome_csv, 'a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)

        # Escrever os parâmetros na nova linha do arquivo CSV
        escritor_csv.writerow(parametros)

def plotar(frame, texto1, texto2, ):
    # Copiar o frame para evitar modificá-lo diretamente
    frame_exibicao = frame.copy()

    # Obter as dimensões do frame
    altura, largura, _ = frame_exibicao.shape
    
    # Definir as configurações do texto
    fonte = cv.FONT_HERSHEY_SIMPLEX
    escala = 0.5
    espessura = 1
    cor = (0, 255, 0)  # Cor do texto (verde)

    # Calcular as posições dos textos
    posicao_texto1 = (10, altura - 20)
    posicao_texto2 = (10, altura - 5)

    x, y = 0, altura-35  # Top-left corner coordinates
    width, height = 500, altura  # Width and height of the rectangle

    # Define the rectangle color (BGR format)
    color = (0, 0, 0)  # Green color

    # Draw the filled rectangle
    cv.rectangle(frame_exibicao, (x, y), (x + width, y + height), color, -1)

    # Adicionar os textos ao frame de exibição
    cv.putText(frame_exibicao, texto1, posicao_texto1, fonte, escala, cor, espessura, cv.LINE_AA)
    cv.putText(frame_exibicao, texto2, posicao_texto2, fonte, escala, cor, espessura, cv.LINE_AA)

    # Exibir o frame em uma janela do OpenCV
    #print(largura,altura)
    #frame_exibicao = cv.resize(frame_exibicao,(largura/2.,altura/2.))
    #frame_exibicao = cv.resize(frame_exibicao,(574,480))
    frame_exibicao = cv.resize(frame_exibicao,(resolution[0],resolution[1]))
    #out.write(frame_exibicao)
    # Gerar o nome do arquivo para a imagem
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    filename = os.path.join(output_folder, f"frame_{amostras}.jpg")

    # Salvar o frame como uma imagem
    cv.imwrite(filename, frame_exibicao)
    
    cv.imshow("Position Estimator", frame_exibicao)


def Yolo(cap): 
    iteracoes=0
    try:
        frame, pose = monoCV.detectar(cap)
        if pose is not None:
            u,v,W,H = pose[0],pose[1],pose[2],pose[3]
            t1,t2 = obterVariaveis(u,v,W,H,iteracoes)
            plotar(frame,t1,t2)
            return True
            
    except:
        print("EXCEPTION")
        ret, frame = cap.read()
        #alt, larg, canais = frame.shape
        t1 = ''
        t2 = ''
        #menor = cv.resize(frame,(574,480))
        menor = cv.resize(frame,(resolution[0],resolution[1]))
        #menor = cv.resize(frame,(int(larg/2.),int(alt/2.)))
        #menor = frame
        '''
        if ret:
            menor = cv.resize(frame,(574,480))
            cv.imshow("Sem deteccao", menor)
            cap.release()
        '''
        plotar(menor,t1,t2)
        return False

def obterVariaveis(u,v,W,H,i):
    iteracoes = 0
    #x e y (minusculos) são posições normalizadas no quadro da camera (entre 0.0 e 1.0)
    Fx = fx*Sx
    Fy = fy*Sy
    U = u*2448  #u*1920. #correcao feita para usar o pixel do frame original
    V = v*2048  #v*1080. #correcao feita para usar o pixel do frame original
    x = ((U - Cx)/(Fnet*alpha))
    y = ((V - Cy)/Fnet)
    
    Z = distanciaCameraCubsat(W,H,w,h)
    Z = Z/10
    #apaguei mas acabou precisando (veja no artigo, eq 2.2):
    #x = X/Z ; y = Y/Z. Logo:
    X = x*Z
    Y = y*Z*-1
    #X = X/10
    #Y = Y/10
    print('X', end=' -> ')
    print(X)
    print('Y', end=' -> ')
    print(Y)
    print('Distancia Z:', end=' -> ')
    print(Z)

    texto = "position relative to camera(cm): (%.2f, %.2f, %.2f)"%(X,Y,Z)
    tamanho = "u, v, x, y: (%.2f, %.2f,%.2f, %.2f)"%(U,V,x,y)
    salvar_em_csv(i,x,y,W,H,X,Y,Z)
    
    return (texto,tamanho)

def distanciaCameraCubsat(W,H,w,h):
    #por algum motivo, so funciona com distancia focal normalizada
    Fx = fx*Sx
    Fy = fy*Sy
    f = (fx+fy)/2
    s = (w+h)/2
    S = (W+H)/2
    Z = ((f * s)/S)

    return (Z)

camera = cv.VideoCapture(caminho_vid)
#rodando = True

amostras = 0

while (True):

    status, frame = camera.read()
    if Yolo(camera):
        amostras +=1

    if not status or cv.waitKey(1) & 0xff == ord('q') or amostras >= 100:
        #rodando = False
        break

import gerador_video
gerador_video.create_video(output_folder,nome_video)
# Libera os recursos
camera.release()
cv.destroyAllWindows()