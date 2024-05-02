import pyautogui
import time
import mouseinfo
import customtkinter
from tkinter import *

"""while True:
    print(pyautogui.position())
    time.sleep(1)"""       

#inserir dados
numero_processo = None
qtd_volumes = None

def __init__():
    pass
def ok():
    global numero_processo  # Indica que estamos utilizando a variável global

    processo = n_processo.get().strip()
    volumes = qtd_volumes.get().strip()
        
    if processo and volumes:  # Verifica se os campos não estão vazios
        numero_processo = int(processo)  # Armazena o número do processo
        janela.destroy()
    else:
        if not processo:
            n_processo['bg'] = 'pink'
        if not volumes:
            qtd_volumes['bg'] = 'pink'
            print('Preencha todos os campos!')

janela = customtkinter.CTk()
janela.geometry('500x300')
janela.resizable(False, False)
texto = customtkinter.CTkLabel(janela, text='N° Processo')
texto.pack(padx=10, pady=10)

n_processo = customtkinter.CTkEntry(janela, placeholder_text='Número do Proceso')
n_processo.pack(padx=10, pady=10)

qtd_volumes = customtkinter.CTkEntry(janela, placeholder_text='Quantidade de volumes do processo')
qtd_volumes.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='Enviar', command=ok)
botao.pack(padx=10, pady=10)

janela.mainloop()

pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
pyautogui.PAUSE = 1.0

# Digitar número de processo no SIAT e consultar
pyautogui.press('tab',presses=6)
pyautogui.write(str(numero_processo))
pyautogui.click(1012, 254)
time.sleep(1.0)

#selecionar o tipo de arquivo
pyautogui.click(612, 543)
pyautogui.press(['down', 'down'])
pyautogui.press('enter')

#Fazer upload do arquivo
pyautogui.click(402, 581)
pyautogui.press('tab', presses=9)
pyautogui.press('space')
pyautogui.press('enter')

#enviar arquivo
pyautogui.click(798, 680)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(393,377)
pyautogui.click(880, 683)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')
