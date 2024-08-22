import os
import time
import pyautogui
import customtkinter
from selenium import webdriver
from tkinter import filedialog
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Variáveis globais
arquivo_excel = None
valor_selecionado = ""
contador_pdfs = 0
caminho_corrigido = ""
tipo_do_processo_normalizado = ""
login = True
driver = webdriver.Chrome()

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
    global caminho_corrigido, pasta
    pasta = filedialog.askdirectory(title="Selecione uma pasta")
    if pasta:
        caminho_entry.delete(0, customtkinter.END)
        caminho_entry.insert(0, pasta)
        # Substituir barras por barras invertidas
        caminho_corrigido = pasta.replace("/", "\\")

def executar_contagem():
    numero_de_pdfs = contar_pdfs(caminho_corrigido)
    
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
            print('Preencha todos os campos!')

def executar_tarefas():
    executar_contagem()
    ok()

def primeiro_processar_processo(arquivo):
    driver.find_element(By.XPATH, '//*[@id="cboTpDocu"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="botCons"]').click()
    time.sleep(2)

    select_tipo = driver.find_element(By.XPATH, '//*[@id="cboTpDocu"]')
    select = Select(select_tipo)
    select_tipo_processo = driver.find_element(By.XPATH, '//*[@id="cboTpDocu"]/option[3]')
    select.select_by_value('P')
    assert select_tipo_processo.is_selected()

    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    file_input = wait.until(EC.presence_of_element_located((By.ID, 'FileStream')))

    # Usar JavaScript para clicar no elemento
    driver.execute_script("arguments[0].click();", file_input)

    time.sleep(2)

    #Selecionar pasta
    pyautogui.press('tab', presses=5)
    pyautogui.press('enter')
    print(pasta)
    pyautogui.write(rf"{caminho_corrigido}")
    time.sleep(2)
    pyautogui.press('right')
    pyautogui.press('enter')

    time.sleep(2)
    #selecionar arquivos
    pyautogui.press('tab', presses=4)
    pyautogui.press('down', presses=arquivo)
    pyautogui.press('space')
    pyautogui.press('enter')
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="botSalvar"]').click()

    time.sleep(2)

    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()  # Aceita o alerta
    except:
        pass  # Não há alerta ou ocorreu um erro ao tentar capturar o alerta

def processar_processo(arquivo):
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="cboTpDocu"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="botCons"]').click()
    time.sleep(2)

    select_tipo = driver.find_element(By.XPATH, '//*[@id="cboTpDocu"]')
    select = Select(select_tipo)
    select_tipo_processo = driver.find_element(By.XPATH, '//*[@id="cboTpDocu"]/option[3]')
    select.select_by_value('P')
    assert select_tipo_processo.is_selected()

    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    file_input = wait.until(EC.presence_of_element_located((By.ID, 'FileStream')))

    # Usar JavaScript para clicar no elemento
    driver.execute_script("arguments[0].click();", file_input)
    time.sleep(2)

    #selecionar arquivos
    pyautogui.press('tab', presses=9)
    pyautogui.press('down', presses=arquivo)
    pyautogui.press('space')
    pyautogui.press('enter')

    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="botSalvar"]').click()

    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = Alert(driver)
        alert.accept()  # Aceita o alerta
    except:
        pass  # Não há alerta ou ocorreu um erro ao tentar capturar o alerta


def should_stop():
        return pyautogui.position() == (0, 0)

driver.get("https://www.tinus.com.br/csp/JABOATAO/SIAT.csp")

time.sleep(10)

iframe_login = driver.find_element(By.XPATH, '//iframe[@src="login.csp?PM=JAB"]')
driver.switch_to.frame(iframe_login)

while login == True:
    try:
        driver.switch_to.default_content()
        iframe_SIAT = driver.find_element(By.XPATH, '//iframe[@id="iFrame2"]')
        driver.switch_to.frame(iframe_SIAT)

        elemento = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginTable"]/tbody/tr[6]/td[1]/div[1]/a/img'))
        )
        print("O elemento foi encontrado, o usuário fez login com sucesso!")
        login = False
    except:
        print("O elemento não foi encontrado, verificando novamente...")
        driver.switch_to.default_content()
        driver.switch_to.frame(iframe_login)
        time.sleep(5)

time.sleep(1)
driver.switch_to.default_content()
iframe2 = driver.find_element(By.XPATH, '//iframe[@id="iFrame2"]')
driver.switch_to.frame(iframe_SIAT)

time.sleep(1)
iframe_menu = driver.find_element(By.XPATH, '//iframe[@src="menu.csp?PM=JAB"]')
driver.switch_to.frame(iframe_menu)
driver.find_element(By.XPATH, '/html/body/form/div[2]/li[6]/span').click()

time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form/div[2]/ul[7]/table/tbody/tr/td/li[2]').click()

time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form/div[2]/ul[7]/table/tbody/tr/td/ul[2]/li[4]/a').click()

time.sleep(1)
driver.find_element(By.XPATH, '/html/body/form/div[2]/ul[7]/table/tbody/tr/td/ul[2]/li[4]/a').click()
driver.switch_to.default_content()

iframe2 = driver.find_element(By.XPATH, '//iframe[@id="iFrame2"]')
driver.switch_to.frame(iframe_SIAT)

iframe_processos = driver.find_element(By.XPATH, '//iframe[@src="main.csp"]')
driver.switch_to.frame(iframe_processos)

while not should_stop():
    input_element = driver.find_element(By.ID, "txtProc")
    current_title = input_element.get_attribute("title")
    expected_title = "Número do Processo formato <aaaannnnnnd>"

    #Interface gráfica
    janela = customtkinter.CTk()
    janela.geometry('400x300')
    janela.resizable(False, False)
    texto = customtkinter.CTkLabel(janela, text='Enviar processos')
    texto.pack(padx=10, pady=10)

    janela.attributes("-topmost", True)

    n_processo = customtkinter.CTkEntry(janela, placeholder_text='Ex: 2010.000000-0')
    n_processo.pack(padx=10, pady=10)

    texto = customtkinter.CTkLabel(janela, text='Escolha o caminho com os arquivos do processo')
    texto.pack(padx=10, pady=2)

    caminho_processo = customtkinter.CTkButton(janela, text='Selecione a Pasta', command=selecionar_pasta)
    caminho_processo.pack(padx=10, pady=10)

    caminho_entry = customtkinter.CTkEntry(janela, width=200)
    caminho_entry.pack(padx=40, pady=10)

    botao = customtkinter.CTkButton(janela, text='Enviar', command=executar_tarefas)
    botao.pack(padx=10, pady=10)

    janela.mainloop()

    #Alerta para o código começar
    pyautogui.alert('O código vai começar. Não utilize nada do computador até o código finalizar!') 
    time.sleep(2)

    if current_title == expected_title:
        #Digitar número de processo no SIAT e consultar
        driver.find_element(By.XPATH, '//*[@id="txtProc"]').send_keys(str(numero_processo))
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="botCons"]').click()
        time.sleep(1)

        # Execução do processo baseado no tipo de processo
        for arquivo in range(contador_pdfs):
            if arquivo == 0:
                primeiro_processar_processo(arquivo)
            else:
                processar_processo(arquivo)
    else:
        # Execução do processo baseado no tipo de processo
        for arquivo in range(contador_pdfs):
            if arquivo == 0:
                primeiro_processar_processo(arquivo)
            else:
                processar_processo(arquivo)


    pyautogui.alert('Todos os arquivos foram enviados com sucesso!') 

driver.quit()
