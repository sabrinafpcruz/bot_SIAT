import pyautogui
import time
import mouseinfo
import customtkinter
import tkinter as tk
from tkinter import filedialog
import pyperclip
import os
import pygetwindow as gw

"2013.000195-8"
"Auto de Infração"
"AUTO DE INFRAÇÃO"
"NOTIFICAÇÃO"

#coordenadas do mouse
"""while True:
    print(pyautogui.position())
    time.sleep(1)        
"""
"""
print("Janelas encontradas:")
for window in gw.getAllTitles():
    print(window)
"""
# Variáveis globais
arquivo_excel = None
valor_selecionado = ""
contador_pdfs = 0
caminho_corrigido = ""
tipo_do_processo_normalizado = ""

def normalizar_texto(texto):
    substituicoes = {
        "Ç": "c", "Ã": "a", "Á": "a", "É": "e", "Í": "i", "Ó": "o", "Ú": "u",
        "Â": "a", "Ê": "e", "Î": "i", "Ô": "o", "Û": "u", "À": "a", "È": "e",
        "Ì": "i", "Ò": "o", "Ù": "u", "Ä": "a", "Ë": "e", "Ï": "i", "Ö": "o",
        "Ü": "u", "Ÿ": "y", "Ý": "y", "ç": "c", "ã": "a", "á": "a", "é": "e",
        "í": "i", "ó": "o", "ú": "u", "â": "a", "ê": "e", "î": "i", "ô": "o",
        "û": "u", "à": "a", "è": "e", "ì": "i", "ò": "o", "ù": "u", "ä": "a",
        "ë": "e", "ï": "i", "ö": "o", "ü": "u", "ÿ": "y", "ý": "y"
    }
    texto_normalizado = texto
    for chave, valor in substituicoes.items():
        texto_normalizado = texto_normalizado.replace(chave, valor)
    return texto_normalizado

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

def remover_caracteres(string_original):
    caracteres_indesejados = "-."
    for char in caracteres_indesejados:
        string_original = string_original.replace(char, '')
    return string_original

def ok():
    global numero_processo, processo  # Indica que estamos utilizando a variável global
    processo = n_processo.get().strip()

    if processo:  # Verifica se os campos não estão vazios
        numero_processo = int(remover_caracteres(processo))  # Armazena o número do processo
        janela.destroy()
    else:
        if not processo:
            numero_processo['bg'] = 'pink'
            print('Preencha todos os campos!')

def executar_tarefas():
    executar_contagem()
    ok()

def processar_processo(arquivo):
    pyautogui.click(576, 540)
    pyautogui.press('down', presses=2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(451, 574)
    time.sleep(1)
    pyautogui.press('tab', presses=9)
    pyautogui.press('down', presses=arquivo)
    pyautogui.press('space')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('tab', presses=2)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(2)

#Interface gráfica
janela = customtkinter.CTk()
janela.geometry('500x400')
janela.resizable(False, False)
texto = customtkinter.CTkLabel(janela, text='Enviar processos')
texto.pack(padx=10, pady=10)

n_processo = customtkinter.CTkEntry(janela, placeholder_text='Ex: 2010.000000-0')
n_processo.pack(padx=10, pady=10)

texto = customtkinter.CTkLabel(janela, text='Escolha o caminho com os arquivos do processo')
texto.pack(padx=10, pady=2)

caminho_processo = customtkinter.CTkButton(janela, text='Selecione a Pasta', command=selecionar_pasta)
caminho_processo.pack(padx=10, pady=10)

caminho_entry = customtkinter.CTkEntry(janela, width=360)
caminho_entry.pack(padx=40, pady=10)

resultado_label = tk.Label(janela, text="")
resultado_label.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text='Enviar', command=executar_tarefas)
botao.pack(padx=10, pady=10)

janela.mainloop()

#Alerta para o código começar
pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!')
time.sleep(2)

#Digitar número de processo no SIAT e consultar
pyautogui.click(529, 225)
pyautogui.press('tab')
pyautogui.write(str(numero_processo))
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

#abrir arquivo explorar
pyautogui.press('win')
time.sleep(1)
pyautogui.write('explorar')
pyautogui.press('enter')
time.sleep(3)

#Digitar caminho excel
pyautogui.press('tab',presses=4)
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(r'\\suecia.pmjg.lan\serec\0 - COMPARTILHAMENTO SEREC\PROCESSOS ESCANEADOS E RENUMERADOS')
pyautogui.press('enter')
time.sleep(1)

#Buscar Excel com os processos
pyautogui.press('tab', presses=7)
pyautogui.write('xlsx')
time.sleep(2)
pyautogui.press('tab', presses=2)
pyautogui.press('space')
pyautogui.press('enter')
time.sleep(8)

#Pesquisar processo
pyautogui.hotkey('ctrl', 'l')
time.sleep(1)
pyautogui.write(str(processo))
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('tab', presses=4)
pyautogui.press('enter')

#Pegar tipo processo
time.sleep(2)
pyautogui.press('right', presses=3)
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

pyautogui.getWindowsWithTitle("Excel")[0].minimize()
pyautogui.getWindowsWithTitle("PROCESSOS ESCANEADOS E RENUMERADOS")[0].minimize()
time.sleep(2)        

# Obtém o valor copiado para a área de transferência
tipo_do_processo = pyperclip.paste()
print(tipo_do_processo)
# Imprime o valor após a substituição
tipo_do_processo_normalizado = normalizar_texto(tipo_do_processo)

print(tipo_do_processo_normalizado)
print(contador_pdfs)

# Execução do processo baseado no tipo de processo
tipo_do_processo_normalizado == 'auto de infracao':
print("Processo é 'auto de infracao'")
for arquivo in range(contador_pdfs):
    processar_processo(arquivo)

pyautogui.alert('Todos os arquivos foram enviados com sucesso!')