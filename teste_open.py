import cv2
import numpy as np
import pyautogui
import time

procurar = "sim"
time.sleep(2)  # Adiciona um atraso inicial para garantir que a tela esteja pronta

# Carregar a imagem de referência (a imagem que você deseja encontrar)
template = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

while procurar == "sim":
    try:
        # Captura uma captura de tela da área de trabalho
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
        
        # Usa matchTemplate para encontrar a imagem
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8  # Define um limiar de confiança
        loc = np.where(res >= threshold)

        if len(loc[0]) > 0:
            # Se a imagem for encontrada, faz duplo clique na primeira correspondência
            pt = (loc[1][0], loc[0][0])
            pyautogui.doubleClick(pt[0] + w // 2, pt[1] + h // 2)
            procurar = 'não'
        else:
            # Se a imagem não for encontrada, espera um segundo e tenta novamente
            time.sleep(1)
            print("não encontrado")
    except Exception as e:
        # Captura exceções e imprime a mensagem de erro
        print(f"Ocorreu um erro: {e}")
        time.sleep(1)
