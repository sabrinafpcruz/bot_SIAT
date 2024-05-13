import pyautogui
import time
import mouseinfo
import customtkinter
from tkinter import *
from tkinter import filedialog
"""
#coordenadas do mouse
    while True:
    print(pyautogui.position())
    time.sleep(1)     

#inserir dados
numero_processo = None
arquivo_excel = None
def __init__():
    pass"""
def abrir_pasta():
    arquivo_excel = filedialog.askdirectory()
    return arquivo_excel
def ok():
    global numero_processo  # Indica que estamos utilizando a variável global
    processo = n_processo.get().strip()

    if processo:  # Verifica se os campos não estão vazios
        numero_processo = int(processo)  # Armazena o número do processo
        janela.destroy()
    else:
        if not processo:
            n_processo['bg'] = 'pink'
            print('Preencha todos os campos!')

janela = customtkinter.CTk()
janela.geometry('500x300')
janela.resizable(False, False)
texto = customtkinter.CTkLabel(janela, text='N° Processo')
texto.pack(padx=10, pady=10)

n_processo = customtkinter.CTkEntry(janela, placeholder_text='Número do Proceso')
n_processo.pack(padx=10, pady=10)

texto = customtkinter.CTkLabel(janela, text='Escolha o arquivo Excel \ncom os caminhos dos processos')
texto.pack(padx=10, pady=2)

caminho_processo = customtkinter.CTkButton(janela, text='Abrir Arquivo', command=abrir_pasta)
caminho_processo.pack(padx=10, pady=10)
print(abrir_pasta())

botao = customtkinter.CTkButton(janela, text='Enviar', command=ok)
botao.pack(padx=10, pady=10)

janela.mainloop()
"""
#alerta para o codigo começar
pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
pyautogui.PAUSE = 1.0

# Digitar número de processo no SIAT e consultar
pyautogui.click(529, 225)
pyautogui.press('tab')
pyautogui.write(filter(str.isalnum(numero_processo)))
pyautogui.press('tab')
pyautogui.press('enter')

#selecionar o tipo de arquivo
pyautogui.press('tab', presses=2)
pyautogui.press(['down', 'down'])
"""
#Abrir pasta dos processos
pyautogui.hotkey('ctrl','o')
time.sleep(1)
pyautogui.press('tab', presses=5)
pyautogui.press('enter')
pyautogui.write(str(abrir_pasta))
pyautogui.press('enter')

#Selecionar arquivo processo
pyautogui.press('tab', presses=4)
pyautogui.press('space')
pyautogui.press('tab', presses=(numero_arquivos))
pyautogui.press('enter')

#Salvar arquivo
pyautogui.press('tab', presses=2)
pyautogui.press('enter')

#selecionar mais arquivos "excel"


"""for a in range(qtd_arquivos):
    #selecionar mais arquivos
    pyautogui.press('tab',presses=3)
    pyautogui.press(['down', 'down'])
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('tab', presses=8)#quantidade de arquivos
"""
"""#enviar para historico
pyautogui.click(798, 680)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(393,377)
pyautogui.click(880, 683)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')"""
