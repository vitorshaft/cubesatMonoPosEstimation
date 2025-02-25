from ultralytics import YOLO
import os
import cv2
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()

    arquivo = filedialog.askopenfilename()
    return arquivo

# Exemplo de uso da função
caminho_arquivo = selecionar_arquivo()
print("Arquivo selecionado:", caminho_arquivo)

diretorio_raiz = 'cubesatMonoPosEstimation/'
#arq_yaml = 'triple_ds.yaml'    #arquivo que deve procurar
arq_yaml = caminho_arquivo
arquivo_config = os.path.join(diretorio_raiz, arq_yaml)
 
# Load the model.
model = YOLO('yolov8n.pt')

# Training.

resultados = model.train(data=arquivo_config, epochs=5, imgsz=640, name='yolov8n_tripleDS')

dir_resultado = os.path.join(diretorio_raiz, '/scripts/runs/detect/yolov8n_tripleDS')

#Continuar treinamento (comentar a partir daqui quando for o 1º treino)

#yolo task=detect mode=train model={dir_resultado}/weights/last.pt data={arquivo_config} epochs=10
#lastpt = '/weights/last.pt')
#modelo_last = os.path.join(dir_resultado,lastpt)
#model_continua = YOLO(modelo_last)
#continuar_train = model.train(data=arquivo_config, epochs=20, imgsz=640, name='yolov8n_tripleDS')

#testar com https://www.youtube.com/watch?v=zfl42B3nWr0
#testar com https://www.youtube.com/watch?v=YoErE4wneiQ (mais curto, menos ruidoso)