import pyautogui
import time
import mouseinfo
import customtkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import pyperclip

"""
#coordenadas do mouse
    while True:
    print(pyautogui.position())
    time.sleep(1)     
"""
#inserir dados
numero_processo = None
arquivo_excel = None

def selecionar_pasta():
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    if pasta:
        caminho_entry.delete(0, tk.END)
        caminho_entry.insert(0, pasta)
        # Substituir barras por barras invertidas
        caminho_corrigido = pasta.replace("/", "\\")
        pyperclip.copy(caminho_corrigido)

def remover_caracteres(string_original):
    caracteres_indesejados = "-."
    for char in caracteres_indesejados:
        string_original = string_original.replace(char, '')
    return string_original

def ok():
    global numero_processo  # Indica que estamos utilizando a variável global
    processo = n_processo.get().strip()

    if processo:  # Verifica se os campos não estão vazios
        numero_processo = int(remover_caracteres(processo))  # Armazena o número do processo
        janela.destroy()
    else:
        if not processo:
            n_processo['bg'] = 'pink'
            print('Preencha todos os campos!')

#Interface gráfica
janela = customtkinter.CTk()
janela.geometry('500x300')
janela.resizable(False, False)
texto = customtkinter.CTkLabel(janela, text='N° Processo')
texto.pack(padx=10, pady=10)

n_processo = customtkinter.CTkEntry(janela, placeholder_text='Número do Proceso')
n_processo.pack(padx=10, pady=10)

texto = customtkinter.CTkLabel(janela, text='Escolha o caminho com os arquivos do processo')
texto.pack(padx=10, pady=2)

caminho_processo = customtkinter.CTkButton(janela, text='Selecione a Pasta', command=selecionar_pasta)
caminho_processo.pack(padx=10, pady=10)

caminho_entry = customtkinter.CTkEntry(janela, width=180)
caminho_entry.pack(padx=40, pady=10)

botao = customtkinter.CTkButton(janela, text='Enviar', command=ok)
botao.pack(padx=10, pady=10)

janela.mainloop()


#Alerta para o código começar
pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
pyautogui.PAUSE = 1.0

#Digitar número de processo no SIAT e consultar
pyautogui.click(529, 225)
pyautogui.press('tab')
pyautogui.write(str(numero_processo))
pyautogui.press('tab')
pyautogui.press('enter')

#Clicar botão de upload dos processos
pyautogui.press('tab', presses=10)
pyautogui.press('enter')

#Selecionar arquivo processo
pyautogui.press('tab', presses=4)
pyautogui.press('space')
pyautogui.press('tab', presses=qtd_arquivos)
pyautogui.press('enter')

#Selecionar arquivos
pyautogui.press('tab', presses=5)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#Abrir Excel com processos
pyautogui.press('win', 'e')
pyautogui.press('tab', presses=5)
pyautogui.write('xlsx')
pyautogui.press('tab', presses=2)
pyautogui.press('space')
pyautogui.press('enter')

#Pesquisar o processo
pyautogui.hotkey('ctrl', 'l')
pyautogui.write(str(n_processo))
pyautogui.press('enter')
pyautogui.press('tab',presses=4)
pyautogui.press('enter')

#Pegar o tipo de arquivo
pyautogui.press('right', presses=3)
pyautogui.hotkey('Ctrl', 'c')
pyautogui.hotkey('win', 'down')

#Abrir chrome do SIAT


#Selecionar o tipo de arquivo



#Salvar arquivo
pyautogui.press('tab', presses=2)
pyautogui.press('enter')

pyautogui.alert('Seus arquivos foram enviados com sucesso!')
