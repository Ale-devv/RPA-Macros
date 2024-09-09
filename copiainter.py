import tkinter as tk
from copiainter import achar_excel, mostrar_erro, entrar_excel, resource_path, opcoes  # Importa as funções do arquivo buscar_excel.py

def iniciar():
    iniciar_busca()
    entrar_excelimg()
    #entrar_opcoes()

def iniciar_busca():
    # Função chamada quando o botão "Prosseguir" é clicado
    try:
        imagens = [resource_path('imagens/win.png'), resource_path('imagens/win1.png')]
        achar_excel(imagens, 'Excel')  # Tenta executar a função de busca pelo Excel
    except Exception as e:
        mostrar_erro(str(e))  # Exibe uma mensagem de erro caso ocorra uma exceção

def entrar_excelimg():
    # Função chamada quando o botão "Prosseguir" é clicado
    try:
        imagens = [resource_path('imagens/excel.png'), resource_path('imagens/excel2.png')]
        entrar_excel(imagens)  # Tenta executar a função de busca pelo Excel
    except Exception as e:
        mostrar_erro(str(e))  # Exibe uma mensagem de erro caso ocorra uma exceção

def entrar_opcoes():
    # Função chamada quando o botão "Prosseguir" é clicado
    try:
        imagens = [resource_path('imagens/opcoes.png'), resource_path('imagens/opcoes2.png')]
        opcoes(imagens)  # Tenta executar a função de busca pelo Excel
    except Exception as e:
        mostrar_erro(str(e))  # Exibe uma mensagem de erro caso ocorra uma exceção

# Criando a janela principal
root = tk.Tk()  # Cria a janela principal Tkinter
root.title("Configuração Macro")  # Define o título da janela principal
root.geometry("300x100")  # Define o tamanho da janela principal

# Label e Botão na janela principal
label = tk.Label(root, text="Clique em Prosseguir para iniciar a busca do Excel.")
# Cria um rótulo com a instrução
label.pack(pady=10)  # Adiciona o rótulo à janela principal com padding

button = tk.Button(root, text="Prosseguir", command=iniciar,)
# Cria um botão "Prosseguir" que chama a função iniciar ao ser clicado
button.pack(pady=10)  # Adiciona o botão à janela principal com padding

root.mainloop()  # Inicia o loop principal da interface gráfica
