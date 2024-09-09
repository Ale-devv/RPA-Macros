import os
import sys
import tkinter as tk
import pyautogui
import time

def resource_path(relative_path):
    """ Obtém o caminho absoluto para os recursos. """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def mostrar_erro(mensagem): #mensagens trazidas do arquivo interface.py das funcoes no ambiente (e) de erro.
    # Função para exibir uma mensagem de erro em uma nova janela
    root = tk.Tk()  # Cria uma nova janela Tkinter
    root.title("Erro")  # Define o título da janela
    label = tk.Label(root, text=f"Ocorreu um erro:\n{mensagem}")
    # Cria um rótulo com a mensagem de erro
    label.pack(padx=20, pady=20)  # Adiciona o rótulo à janela com padding
    button = tk.Button(root, text="OK", command=root.destroy)# Cria um botão "OK" que fecha a janela ao ser clicado
    
    button.pack(pady=10)  # Adiciona o botão à janela com padding
    root.mainloop()  # Inicia o loop principal da janela de erro

def achar_excel(imagens, texto_para_escrever):# dados capturados pelo interface como parametro, unica funcao com paramentro de string = EXCEL
    # Função que realiza a busca por um programa (neste caso, Excel) com base nas imagens fornecidas e escreve o texto fornecido
    procurar = True  # Variável de controle para continuar a busca
    tentativas_maximas = 3  # Número máximo de tentativas para cada imagem
    tentativas_globais = 0  # Contador de tentativas globais
    
    for imagem in imagens:
        # Loop para cada imagem na lista
        tentativas = 0  # Contador de tentativas para a imagem atual
        while procurar and tentativas < tentativas_maximas:
            # Loop para tentar localizar a imagem um número máximo de vezes
            try:
                img = pyautogui.locateCenterOnScreen(imagem, confidence=0.7)
                # Tenta localizar a imagem na tela com 70% de confiança
                
                if img is not None:
                    # Se a imagem for encontrada
                    pyautogui.click(img.x, img.y)  # Clica no centro da imagem encontrada
                    time.sleep(1)  # Espera 1 segundo
                    pyautogui.write(texto_para_escrever)  # Escreve o texto fornecido
                    
                    procurar = False  # Define procurar como False para parar a busca
                    break  # Sai do loop while quando a imagem é encontrada
                else:
                    # Se a imagem não for encontrada
                    time.sleep(1)  # Espera 1 segundo
                    print(f"Imagem {imagem} não encontrada na tentativa {tentativas + 1}")
                    # Imprime mensagem de que a imagem não foi encontrada
                    tentativas += 1  # Incrementa o contador de tentativas para a imagem atual
                    tentativas_globais += 1  # Incrementa o contador de tentativas globais
            except pyautogui.ImageNotFoundException:
                # Exceção específica do pyautogui quando a imagem não é encontrada
                time.sleep(1)  # Espera 1 segundo
                print(f"Imagem {imagem} não encontrada na tentativa {tentativas + 1}")
                # Imprime mensagem de que a imagem não foi encontrada
                tentativas += 1  # Incrementa o contador de tentativas para a imagem atual
                tentativas_globais += 1  # Incrementa o contador de tentativas globais
            except Exception as e:
                # Captura outras exceções
                raise Exception(f"Ocorreu um erro ao processar imagem {imagem}: {e}")
                # Lança uma nova exceção com uma mensagem de erro detalhada
        if not procurar:
            # Se a imagem foi encontrada, sai do loop principal
            break
    
    if procurar:
        # Se nenhuma imagem foi encontrada após todas as tentativas
        print("Nenhuma imagem encontrada após várias tentativas.")
        mostrar_erro("Programa não encontrado - Entre em contato com o suporte")

def entrar_excel(imagens): #Função somente para receber duas imagens como parametro das outras funções de interface.py, 
    #esta função é chamada varias vezes e sendo reutilizada quantas vezes forem necessarios
    # Função que realiza a busca por um programa (neste caso, Excel) com base nas imagens fornecidas
    procurar = True  # Variável de controle para continuar a busca
    tentativas_maximas = 3  # Número máximo de tentativas para cada imagem
    tentativas_globais = 0  # Contador de tentativas globais
    
    for imagem in imagens:
        # Loop para cada imagem na lista
        tentativas = 0  # Contador de tentativas para a imagem atual
        while procurar and tentativas < tentativas_maximas:
            # Loop para tentar localizar a imagem um número máximo de vezes
            try:
                img = pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
                # Tenta localizar a imagem na tela com 70% de confiança 
                
                if img is not None:
                    # Se a imagem for encontrada
                    pyautogui.click(img.x, img.y)  # Clica no centro da imagem encontrada
                    time.sleep(0.2)  # Espera 1 segundo
                    
                    procurar = False  # Define procurar como False para parar a busca
                    break  # Sai do loop while quando a imagem é encontrada
                else:
                    # Se a imagem não for encontrada
                    time.sleep(0.2)  # Espera 1 segundo
                    print(f"Imagem {imagem} não encontrada na tentativa {tentativas + 1}")
                    # Imprime mensagem de que a imagem não foi encontrada
                    tentativas += 1  # Incrementa o contador de tentativas para a imagem atual
                    tentativas_globais += 1  # Incrementa o contador de tentativas globais
            except pyautogui.ImageNotFoundException:
                # Exceção específica do pyautogui quando a imagem não é encontrada
                time.sleep(0.2)  # Espera 1 segundo
                print(f"Imagem {imagem} não encontrada na tentativa {tentativas + 1}")
                # Imprime mensagem de que a imagem não foi encontrada
                tentativas += 1  # Incrementa o contador de tentativas para a imagem atual
                tentativas_globais += 1  # Incrementa o contador de tentativas globais
            except Exception as e:
                # Captura outras exceções
                raise Exception(f"Ocorreu um erro ao processar imagem {imagem}: {e}")
                # Lança uma nova exceção com uma mensagem de erro detalhada
        if not procurar:
            # Se a imagem foi encontrada, sai do loop principal
            break
    
    if procurar:
        # Se nenhuma imagem foi encontrada após todas as tentativas
        print("Nenhuma imagem encontrada após várias tentativas.")
        mostrar_erro("Programa não encontrado - Entre em contato com o suporte")



# Modificação para buscar as imagens na pasta 'imagens' # toda vez que adicionar mais funções no interface.py
# que chame a funcao entrar_excel() do principal, sempre atualize a lista de imagens que precisão ser lidas.
if __name__ == "__main__":
    imagens = [
        resource_path('imagens\excel.png'),
        resource_path('imagens\excel2.png'),
        resource_path('imagens\opcoes.png'),
        resource_path('imagens\opcoes2.png'),
        resource_path('imagens\ctrf.png'),
        resource_path('imagens\ctrf1.png'),
        resource_path('imagens\cfgctrf.png'),
        resource_path('imagens\cfgctrf1.png'),
        resource_path('imagens\lconf.png'),
        resource_path('imagens\lconf2.png'),
        resource_path('imagens\permitlconf.png'),
        resource_path('imagens\permitlconf2.png'),
        resource_path('imagens\adcnovoloc.png'),
        resource_path('imagens\adcnovoloc2.png'),
        resource_path('imagens\documentos.png'),
        resource_path('imagens\documentos2.png'),
        resource_path('imagens\_dir.png'),
        resource_path('imagens\_dir2.png'),
        resource_path('imagens\_local.png'),
        resource_path('imagens\_local2.png'),
        resource_path('imagens\marcsubs.png')
             ]
    
    achar_excel(imagens, 'Excel')
    entrar_excel(imagens)
    
