import asyncio
from lib2to3.pgen2 import driver
import pyautogui
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("https://www.tinus.com.br/csp/JABOATAO/SIAT.csp")

time.sleep(5)

iframe = driver.find_element(By.XPATH, '//iframe[@src="login.csp?PM=JAB"]')

driver.switch_to.frame(iframe)

try:
    elemento = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "txtMatricula"))
    )
    elemento.send_keys("12345")
finally:
    driver.quit()


# Variáveis globais
arquivo_excel = None
valor_selecionado = ""
contador_pdfs = 0
caminho_corrigido = ""
tipo_do_processo_normalizado = ""

"""# Encontre os campos de entrada de nome de usuário e senha (substitua 'nome_campo' pelos nomes reais dos campos)
campo_usuario = driver.find_element(By.XPATH, '/html/body/form/div[2]/table[1]/tbody/tr[1]/td/input').send_keys("12345")
campo_senha = driver.find_element(By.XPATH, '/html/body/form/div[2]/table[1]/tbody/tr[2]/td/input').send_keys("12345")
"""
pyautogui.alert("Arquivos enviados")
#minimizar consulta de pasta e excel
"""    pyautogui.getWindowsWithTitle("Excel")[0].minimize()
    pyautogui.getWindowsWithTitle("PROCESSOS ESCANEADOS E RENUMERADOS")[0].minimize()
    time.sleep(2)"""  

# Execução do processo baseado no tipo de processo
"""
    # Obtém o valor copiado para a área de transferência
    tipo_do_processo = pyperclip.paste()
    print(tipo_do_processo)
    # Imprime o valor após a substituição
    tipo_do_processo_normalizado = normalizar_texto(tipo_do_processo)

    print(tipo_do_processo_normalizado)
    print(contador_pdfs)

    if tipo_do_processo_normalizado == 'auto de infracao':
        print("Processo é 'auto de infracao'")
        for arquivo in range(contador_pdfs):
            processar_processo(arquivo)
    else:
        pyautogui.alert('Tipo do processo não encontrado')"""

#Arquivos com tipos diferentes
"""    #abrir arquivo explorar
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
"""