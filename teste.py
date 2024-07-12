from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.tinus.com.br/csp/JABOATAO/SIAT.csp")

    # Listar todos os iframes na página
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Número de iframes encontrados: {len(iframes)}")

    # Tentar alternar para cada iframe e procurar pelo elemento
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='Pagina']"))
            )
            print("Tela de login detectada no iframe.")
            break
        except:
            print("Elemento não encontrado neste iframe.")
            driver.switch_to.default_content()  # Voltar para o conteúdo principal

except Exception as e:
    print("Tela de login não encontrada.")
    print(e)
finally:
    driver.quit()
