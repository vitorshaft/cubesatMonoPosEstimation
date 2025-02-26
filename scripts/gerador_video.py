import cv2
import os
import tkinter as tk
from tkinter import filedialog

def selecionar_diretorio():
    root = tk.Tk()
    root.withdraw()

    diretorio = filedialog.askdirectory(title="fin folder you typed in")

    return diretorio

# Exemplo de uso da função
pasta_imagens = selecionar_diretorio()
'''
def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()

    arquivo = filedialog.askopenfilename()
    return arquivo

# Exemplo de uso da função
caminho_arquivo = selecionar_arquivo()
print("Arquivo selecionado:", caminho_arquivo)
'''
def create_video(image_folder, video_name):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = frame.shape

    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*"mp4v"), 5, (width, height))
    i = 0
    for image in images:
        i+=1
        video.write(cv2.imread(os.path.join(image_folder, image)))
        print(i," imagens processadas")

    cv2.destroyAllWindows()
    video.release()
""" 
# Defina o diretório das imagens e o nome do vídeo
image_folder = pasta_imagens
video_name = 'video.mp4'

# Crie o vídeo
create_video(image_folder, video_name)
 """