import pyautogui
import time



def achar_excel():
    procurar = "sim"
    while procurar == "sim":

        
        try:
            # Tenta localizar a imagem com confiança ajustada
            img = pyautogui.locateCenterOnScreen('win.png','win1.png' confidence=0.7)

                # Se a imagem for encontrada, faz duplo clique
                pyautogui.click(img.x, img.y)
                time.sleep(1)
                pyautogui.write('Excel')
                procurar = 'não'
            else:
                # Se a imagem não for encontrada, espera um segundo e tenta novamente
                time.sleep(1)
                print("nao encontrado")
        except pyautogui.ImageNotFoundException:
            # Captura exceção específica de imagem não encontrada
            time.sleep(1)
            print("Imagem não encontrada")
        except Exception as e:
            # Captura outras exceções e imprime a mensagem de erro
            print(f"Ocorreu um erro: {e}")
            time.sleep(1)

def entrar_excel():
    procurar = "sim"
    while procurar == "sim":
        try:
            # Tenta localizar a imagem com confiança ajustada
            img = pyautogui.locateCenterOnScreen('excel.png', confidence=0.8)

            if img is not None:
                # Se a imagem for encontrada, faz duplo clique
                time.sleep(1)
                pyautogui.doubleClick(img.x, img.y)
                
                
                procurar = 'não'
            else:
                # Se a imagem não for encontrada, espera um segundo e tenta novamente
                time.sleep(1)
                print("nao encontrado")
        except pyautogui.ImageNotFoundException:
            # Captura exceção específica de imagem não encontrada
            time.sleep(1)
            print("Imagem não encontrada")
        except Exception as e:
            # Captura outras exceções e imprime a mensagem de erro
            print(f"Ocorreu um erro: {e}")
            time.sleep(1) 

def opcoes():
    procurar = "sim"
    while procurar == "sim":
        try:
            # Tenta localizar a imagem com confiança ajustada
            img = pyautogui.locateCenterOnScreen('opcoes.png', confidence=0.8)

            if img is not None:
                # Se a imagem for encontrada, faz duplo clique
                time.sleep(1)
                pyautogui.click(img.x, img.y)
                
                
                procurar = 'não'
            else:
                # Se a imagem não for encontrada, espera um segundo e tenta novamente
                time.sleep(1)
                print("nao encontrado")
        except pyautogui.ImageNotFoundException:
            # Captura exceção específica de imagem não encontrada
            time.sleep(1)
            print("Imagem não encontrada")
        except Exception as e:
            # Captura outras exceções e imprime a mensagem de erro
            print(f"Ocorreu um erro: {e}")
            time.sleep(1)    
   

achar_excel()
entrar_excel()
opcoes()