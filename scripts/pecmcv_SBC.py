#carrega dependencias
import os
import cv2  #instalar com pip install opencv-python
from ultralytics import YOLO    #instalar com pip install ultralytics
import monoCV

#descomentar o modelo de detecção que for usar
onnx = "monoCVnano250e.onnx"

# Obtém o diretório atual do script
dir_atual = os.path.dirname(os.path.abspath(__file__))

#carrega o modelo
model = YOLO(onnx, task = "detect")

#fontes de midia de teste:
caminho_img = os.path.join(dir_atual, 'media', 'frame_19.jpg')
caminho_vid = os.path.join(dir_atual, 'media', 'video.mp4')
#caminho_vid = "C:/Users/vitor/Documents/PPGEA/Artigo_SBC/scripts/cubesat_deploy7s.mp4" #video curto

#faz leitura da imagem
img = cv2.imread(caminho_img)

#leitura de video (descomentar o que for usar: número para webcam, caminho do video para arquivo)
#cap = cv2.VideoCapture(caminho_vid)
cap = cv2.VideoCapture(0)#webcam do notebook é 0

#iteração a cada frame lido do video (ou camera)
while True:
    #print(monoCV.detectar(cap)) #printa resultados (u,v,w,h)[pixels,pixels,porcento,porcento]
    monoCV.detectar(cap)
    if cv2.waitKey(1) == ord('q'):
            break
# Libera os recursos
cap.release()
cv2.destroyAllWindows()