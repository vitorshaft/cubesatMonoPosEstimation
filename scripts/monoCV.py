#carrega dependencias
import os
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import funcoes_desenho

# Obtém o diretório atual do script
dir_atual = os.path.dirname(os.path.abspath(__file__))

onnx = "monoCVnano250e.onnx"

model = YOLO(onnx, task = "detect")

#Matriz da câmera:
mat = [[1.14637048e+03, 0.00000000e+00, 9.08576457e+02],
 [0.00000000e+00, 1.13737781e+03, 5.68368717e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]
#Coeficientes de distorção:
dist = [[ 0.08493417, -0.22591628,  0.00156742, -0.00557683,  0.17277974]]

def mostrar(img):
  fig = plt.gcf()
  fig.set_size_inches(8,5)
  plt.axis('on')
  plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
  plt.draw()
  plt.pause(0.001)
  plt.clf
  #plt.show()

def corrigir(imagem, mat, dist):

    H,W,canais = imagem.shape
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mat, dist, (W,H), 1, (W,H))

    # undistort
    #corrigida = cv2.undistort(imagem, mat, dist, None, newcameramtx)
    
    # undistort using remapping
    mapx, mapy = cv2.initUndistortRectifyMap(mat, dist, None, newcameramtx, (W,H), 5)
    corrigida = cv2.remap(imagem, mapx, mapy, cv2.INTER_LINEAR)

    # crop the image
    x, y, w, h = roi
    #corrigida = corrigida[y:y+h, x:x+w]
    menor = cv2.resize(corrigida,(int(w/2.),int(h/2.)))
    #cv2.imshow('Imagem com pontos detectados', menor)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return corrigida

def plotar(frame, texto1, texto2):
    # Criar uma figura do Matplotlib
    fig, ax = plt.subplots()

    # Exibir o frame na figura
    ax.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Adicionar os textos no canto inferior da figura
    ax.text(10, frame.shape[0] - 10, texto1, color='white', fontsize=12,
            bbox=dict(facecolor='black', alpha=0.5))
    ax.text(10, frame.shape[0] - 30, texto2, color='white', fontsize=12,
            bbox=dict(facecolor='black', alpha=0.5))

    # Configurar os eixos para ocultar as marcações
    ax.axis('off')

    # Atualizar a figura
    plt.draw()
    plt.pause(0.001)

    # Fechar a figura anterior para evitar acúmulo de figuras
    plt.clf()

caminho_img = os.path.join(dir_atual, 'media', 'frame_19.jpg')
caminho_vid = os.path.join(dir_atual, 'media', 'video.mp4')
img = cv2.imread(caminho_img)
cap = cv2.VideoCapture(caminho_vid)
#cap = cv2.VideoCapture(0)
xyLH = []
def detectar(cap):
    #while True:
# Captura um frame da câmera
    #ret, quadro = cap.read()
    #frame = corrigir(quadro,mat,dist)
    ret, frame = cap.read()
    alt, larg, canais = frame.shape
    resultados = model.predict(source = frame, conf=0.65, verbose=False)
    #resultados = model.predict(source = img, conf=0.8, verbose=False)
    #resultado_img = funcoes_desenho.desenha_caixas(img, resultados[0].boxes.data)
    resultado_img = funcoes_desenho.desenha_caixas(frame, resultados[0].boxes.data)
    
    try:
        caixa = resultados[0].boxes.data
        boxes = resultados[0].boxes
        box = boxes[0]  # returns one box
        uvwh = box.xywh.tolist()[0]
        uvwhn = box.xywhn.tolist()[0]
        xyLH = [uvwhn[0],uvwhn[1],uvwhn[2],uvwhn[3]]
        #print(xyLH)
        #resultado_img = cv2.circle(img,((int(uvwh[0]),int(uvwh[1]))),2,(0,0,255),2)
        resultado_img = cv2.circle(frame,((int(uvwh[0]),int(uvwh[1]))),5,(100,255,0),5)
        # Draw a horizontal line (cross) at the center
        cv2.line(frame, (int(uvwh[0]) - 50, int(uvwh[1])), (int(uvwh[0]) + 50, int(uvwh[1])), (0, 255, 0), 3)
        
        # Draw a vertical line (cross) at the center
        cv2.line(frame, (int(uvwh[0]), int(uvwh[1]) - 50), (int(uvwh[0]), int(uvwh[1]) + 50), (0, 255, 0), 3)
    
        resultado_img = cv2.resize(resultado_img,(853,480))
        mostrar(resultado_img)
        #cv2.imshow("Detector",resultado_img)
        
        return(resultado_img,xyLH)
    except:
        cam_resize = cv2.resize(frame,(853,480))
        cv2.imshow("Detector",cam_resize)
        return(cam_resize,None)
        pass
