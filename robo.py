import pyautogui
import time
import mouseinfo
import customtkinter
import tkinter as tk
from tkinter import filedialog
import pyperclip
import os

#coordenadas do mouse
"""while True:
    print(pyautogui.position())
    time.sleep(1)        
"""
# Variáveis globais
numero_processo = None
arquivo_excel = None
valor_selecionado = ""
contador_pdfs = 0
caminho_corrigido = ""

def selecionar_pasta():
    global caminho_corrigido
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    if pasta:
        caminho_entry.delete(0, tk.END)
        caminho_entry.insert(0, pasta)
        # Substituir barras por barras invertidas
        caminho_corrigido = pasta.replace("/", "\\")

def executar_contagem():
    if caminho_corrigido:
        numero_de_pdfs = contar_pdfs(caminho_corrigido)
        resultado_label.config(text=f"Número de arquivos PDF: {numero_de_pdfs}")
    else:
        resultado_label.config(text="Por favor, selecione uma pasta primeiro.")

# Função para contar os arquivos PDF no diretório
def contar_pdfs(diretorio):
    global contador_pdfs
    contador_pdfs = 0

    for root, dirs, files in os.walk(diretorio):
        for file in files:
            if file.lower().endswith('.pdf'):
                contador_pdfs += 1

def verificar_selecao(event):
    global indice_selecionado, valor_selecionado
    indice_selecionado = tipo_processo.current()  # Obtém o índice da seleção atual
    valor_selecionado = tipo_processo.get()       # Obtém o valor da seleção atual

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

def executar_tarefas():
    executar_contagem()
    ok()

#Interface gráfica
janela = customtkinter.CTk()
janela.geometry('500x400')
janela.resizable(False, False)
texto = customtkinter.CTkLabel(janela, text='N° Processo')
texto.pack(padx=10, pady=10)

n_processo = customtkinter.CTkEntry(janela, placeholder_text='Número do Proceso')
n_processo.pack(padx=10, pady=10)

texto = customtkinter.CTkLabel(janela, text='Escolha o caminho com os arquivos do processo')
texto.pack(padx=10, pady=2)

caminho_processo = customtkinter.CTkButton(janela, text='Selecione a Pasta', command=selecionar_pasta)
caminho_processo.pack(padx=10, pady=10)

caminho_entry = customtkinter.CTkEntry(janela, width=360)
caminho_entry.pack(padx=40, pady=10)

opcoes = ["Auto de Infração", "Notificação"]

tipo_processo = customtkinter.CTkComboBox(janela, values=opcoes)
tipo_processo.bind("<<ComboboxSelected>>", verificar_selecao)
tipo_processo.pack(padx=10, pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='Enviar', command=executar_tarefas)
botao.pack(padx=10, pady=10)

janela.mainloop()

"""
#Alerta para o código começar
pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
pyautogui.PAUSE = 1.0

#Digitar número de processo no SIAT e consultar
pyautogui.click(529, 225)
pyautogui.press('tab')
pyautogui.write(str(numero_processo))
pyautogui.press('tab')
pyautogui.press('enter')

#Pegar o tipo do excel
#Abrir Excel com processos
pyautogui.hotkey('win', 'e')
pyautogui.press('tab', presses=4)
pyautogui.press('enter')
pyautogui.write(r'\\suecia.pmjg.lan\serec\0 - COMPARTILHAMENTO SEREC\PROCESSOS ESCANEADOS E RENUMERADOS')
pyautogui.press('enter')
pyautogui.press('tab', presses=7)
pyautogui.write('xlsx')
pyautogui.press('tab', presses=2)
pyautogui.press('space')
pyautogui.press('enter')
time.sleep(3)

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
"Auto de Infração"
"""
tipo_do_processo=pyperclip.paste()
time.sleep(7)
pyautogui.click(626,546)
print(tipo_do_processo)
if tipo_do_processo == "Auto de Infração":
        pyautogui.press('down', presses=19)
        
        #Clicar botão de upload dos processos
        pyautogui.press('tab',presses=2)
        pyautogui.press('enter')
        time.sleep(1)

        #Selecionar pasta
        pyautogui.press('tab', presses=5)
        pyautogui.press('enter')
        pyautogui.write(caminho_corrigido)
        pyautogui.press('enter')
        time.sleep(2)

        #Selecionar arquivo
        pyautogui.press('tab',presses=4)
        pyautogui.press('space')
        pyautogui.press('enter')

elif tipo_do_processo == "Notificação": #tipo_do_processo == "Notificação: "
        pyautogui.press('down', presses=115)


        #Clicar botão de upload dos processos
        pyautogui.press('tab',presses=2)
        pyautogui.press('enter')
        time.sleep(2)

        #Selecionar pasta
        pyautogui.press('tab', presses=5)
        pyautogui.write(str(caminho_corrigido))
        pyautogui.press('enter')

        #Selecionar arquivo
        pyautogui.press('tab',presses=4)
        pyautogui.press('space')
        pyautogui.press('enter') 

"""for arquivo in range(contador_pdfs-1):
    #selecionar o tipo
    if tipo_do_processo == "Auto de Infração":
        pyautogui.press('down', presses=19)
        #Clicar botão de upload dos processos
        pyautogui.press('tab',presses=2)
        pyautogui.press('enter')
        time.sleep(2)

        #Selecionar arquivo
        pyautogui.press('tab',presses=4)
        time.sleep(1)

        pyautogui.press('space')
        time.sleep(1)
        pyautogui.press('enter')                


    elif tipo_do_processo == "Notificação":
        pyautogui.press('down', presses=115)
        #Clicar botão de upload dos processos
        pyautogui.press('tab', presses=2)
        pyautogui.press('enter')
        time.sleep(2)

        #Selecionar pasta
        pyautogui.press('tab', presses=5)
        pyautogui.write(str(caminho_corrigido))
        pyautogui.press('enter')

        #Selecionar arquivo
        pyautogui.press('tab',presses=4)
        pyautogui.press('space')
        pyautogui.press('enter')

        #clicar em enviar
        pyautogui.press('tab', presses=2)
        pyautogui.press('enter')
"""
"""
#Abrir chrome do SIAT

#Selecionar o tipo de arquivo

        #clicar em enviar
        time.sleep(1)
        pyautogui.press('tab', presses=2)
        pyautogui.press('enter')

#Salvar arquivo
pyautogui.press('tab', presses=2)
pyautogui.press('enter')

pyautogui.alert('Seus arquivos foram enviados com sucesso!')
"""

""" #Selecionar arquivo
        pyautogui.press('tab',presses=4)
        time.sleep(1)

        pyautogui.press('space')
        time.sleep(1)
        pyautogui.press('enter') """