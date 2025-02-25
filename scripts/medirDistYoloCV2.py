import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from ultralytics import YOLO
import funcoes_desenho

# Obtém o diretório atual do script
dir_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho correto para o modelo ONNX
onnx = 'best.onnx'

# Verifica se o arquivo realmente existe
if not os.path.exists(onnx):
    raise FileNotFoundError(f"Modelo ONNX não encontrado: {onnx}")

# Carrega o modelo
model = YOLO(onnx)

def mostrar(img):
    fig = plt.gcf()
    fig.set_size_inches(8, 5)
    plt.axis('off')
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

# Corrigir caminhos das mídias
caminho_img = os.path.join(dir_atual, 'media', 'frame_19.jpg')
caminho_vid = os.path.join(dir_atual, 'media', 'video.mp4')

# Verifica se os arquivos existem antes de carregar
if not os.path.exists(caminho_img):
    raise FileNotFoundError(f"Imagem não encontrada: {caminho_img}")
if not os.path.exists(caminho_vid):
    raise FileNotFoundError(f"Vídeo não encontrado: {caminho_vid}")

# Carrega imagem e vídeo
img = cv2.imread(caminho_img)
cap = cv2.VideoCapture(caminho_vid)

# Loop principal
while True:
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo ou erro na captura.")
        break
    
    resultados = model.predict(source=frame, conf=0.6)
    resultado_img = funcoes_desenho.desenha_caixas(frame, resultados[0].boxes.data)
    
    try:
        caixa = resultados[0].boxes.data
        texto = str(caixa[3] - caixa[1])
        print(texto)
    except:
        pass
    
    # Redimensiona a imagem antes de exibir
    frame_resized = cv2.resize(resultado_img, (1024, 768))

    cv2.imshow("Detector", frame_resized)

    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
