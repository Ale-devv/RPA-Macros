import tkinter as tk
import time
import pyautogui
from tkinter import messagebox
from principal import achar_excel, mostrar_erro, entrar_excel, resource_path  # Importa as funções do arquivo princpal.py

def iniciar():
    iniciar_busca()
    #fechar()
    entrar_excelimg()
    entrar_opcoes()
    entrar_ctrf()
    ctrf()
    locaisconfiaveis()
    permitirlocais()
    adclocaisconfiaveis()
    procurarlocais()
    adicionando_documentos()
    okdiretorios()
    subpastas()
    oklocal()

    # barracima()
    mostrar_confirmacao_termino()#penultima funçao chamada após todo o procedimento, toda vez que colocar mais um procedimento, é necessario colocar essa funcao em penultimo
    fechar()#ultima funcao chamada apos o aviso de termino da configuração, chama fechar() e destroi o processo, janelas.

def fechar():

    janela.destroy
def iniciar_busca():
   

    # Função chamada quando o botão "Prosseguir" é clicado


    try:


        imagens = [resource_path('imagens/win1.png'), resource_path('imagens/win.png'),resource_path('imagens/winnot.png'), resource_path('imagens/winnot2.png')]


        achar_excel(imagens, 'Excel')  # Tenta executar a função de busca pelo Excel


    except Exception as e:


        mostrar_erro(str(e))  # Exibe uma mensagem de erro caso ocorra uma exceção
def entrar_excelimg():


    # Função chamada quando o botão "Prosseguir" é clicado


    try:


        imagens = [resource_path('imagens/excel.png'), resource_path('imagens/excel2.png'), resource_path('imagens/excelnot1'),resource_path('imagens/excel_not2')]


        entrar_excel(imagens)  # Tenta executar a função de busca pelo Excel


    except Exception as e:


        mostrar_erro(str(e))  # Exibe uma mensagem de erro caso ocorra uma exceção
def entrar_opcoes():


    # Função chamada quando o botão "Prosseguir" é clicado

    time.sleep(8) #tempo para ele começar a procurar as img de opcoes

    try:


        imagens = [resource_path('imagens/opcoes.png'), resource_path('imagens/opcoes2.png')]


        entrar_excel(imagens)  # Tenta executar a função de busca pelo Excel


    except Exception as e:


        mostrar_erro(str(e))  # Exibe uma mensagem de erro caso ocorra uma exceção
def entrar_ctrf(): # entrando na central de confiabilidade


    try:


        imagens = [resource_path('imagens/ctrf.png'),resource_path('imagens/ctrf1.png')]
        entrar_excel(imagens)


    except Exception as e:


        mostrar_erro(str(e)) # exibiçao de erros
def ctrf():#entrando em cfgs de config


    try:


        imagens = [resource_path('imagens/cfgctrf.png'),resource_path('imagens/cfgctrf1.png')]
        entrar_excel(imagens)


    except Exception as e:


        mostrar_erro(str(e)) # exibiçao de erros    
def locaisconfiaveis():#entrando em locais


    try:


        imagens = [resource_path('imagens/lconf.png'),resource_path('imagens/lconf2.png')]
        entrar_excel(imagens)


    except Exception as e:


        mostrar_erro(str(e)) # exibiçao de erros    
def permitirlocais():#entrando em locais


    try:
        

        imagens = [resource_path('imagens/permitlconf.png'),resource_path('imagens/permitlconf2.png')]
        entrar_excel(imagens)
        pyautogui.press('space')


    except Exception as e:


        mostrar_erro(str(e)) # exibiçao de erros    
def adclocaisconfiaveis():#entrando em locais


    try:


        imagens = [resource_path('imagens/adcnovoloc.png'),resource_path('imagens/adcnovoloc2.png')]
        entrar_excel(imagens)


    except Exception as e:


        mostrar_erro(str(e)) # exibiçao de erros    
def procurarlocais():#procurando locais no usuario


    try:


        imagens = [resource_path('imagens/procurarl.png'),resource_path('imagens/procurarl.png')]
        entrar_excel(imagens)


    except Exception as e:


        mostrar_erro(str(e)) # exibiçao de erros   

def adicionando_documentos():
    time.sleep(2)
    pyautogui.press('tab',8)
    pyautogui.press('up',15)
    try:
        imagens = [resource_path('imagens/documentos.png'), resource_path('imagens/documentos2.png')]
        entrar_excel(imagens)
    except Exception as e:
        mostrar_erro(str(e)) 


def okdiretorios():
    try:
        imagens = [resource_path('imagens/_dir.png'),resource_path('imagens/_dir2.png')]
        entrar_excel(imagens)
    except Exception as e:
        mostrar_erro(str(e))
def subpastas():
    try:
        imagens = [resource_path('imagens/marcsubs.png'),resource_path('imagens/marcsubs.png')]
        entrar_excel(imagens)
    except Exception as e:
        mostrar_erro(stre(e))
def oklocal():
    try:
        imagens = [resource_path('imagens/_local.png)'),resource_path('imagens/_local2.png')]
        entrar_excel(imagens)
    except Exception as e:
        mostrar_erro(str(e))    
def barracima():#barra para cima p documentosExcel


    try:


        imagens = [resource_path('imagens/barraexplorer.png'),resource_path('imagens/barraexplorer2.png')]
        entrar_excel(imagens)


    except Exception as e:


        mostrar_erro(str(e)) # exibiçao de erros    
def mostrar_confirmacao_termino():

    time.sleep(3)

    janelala = tk.Tk

    janela.withdraw()  # Ocultar a janela principal


    messagebox.showinfo("Concluído", "O procedimento foi concluído com sucesso, SEU BOCA ABERTA!!")

    janela.destroy()

# Criando a janela principal

janela = tk.Tk()  # Cria a janela principal Tkinter
janela.title("Configuração Macro")  # Define o título da janela principal
janela.geometry("300x100")  # Define o tamanho da janela principal
# Label e Botão na janela principal
label = tk.Label(janela, text="Clique em Prosseguir para iniciar a busca do Excel.")
# Cria um rótulo com a instrução
label.pack(pady=10)  # Adiciona o rótulo à janela principal com padding
button = tk.Button(janela, text="Prosseguir", command=iniciar)
# Cria um botão "Prosseguir" que chama a função iniciar ao ser clicado
button.pack(pady=10)  # Adiciona o botão à janela principal com padding
janela.mainloop()  # Inicia o loop principal da interface gráfica



