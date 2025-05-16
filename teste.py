from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

'''CONFIGURAÇÕES INICIAIS'''

# Tamanho da tela do monitor
SCREEN_WIDTH  = 1920
SCREEN_HEIGHT = 1080
WINDOW_WIDTH  = SCREEN_WIDTH // 2
WINDOW_HEIGHT = SCREEN_HEIGHT

# Caminhos relativos
INDEX_HTML   = os.path.abspath("index.html")
CREDITO_HTML = os.path.abspath("cartao-de-credito/pagamento-credito.html")

# Converte para formato Unix (/) 
index_url   = "file:///" + INDEX_HTML.replace("\\", "/")
credito_url = "file:///" + CREDITO_HTML.replace("\\", "/")

# Configurações do Chrome para evitar mensagem de automação
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-blink-features=AutomationControlled")


# Inicializando o Chrome com opções
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
driver.set_window_position(SCREEN_WIDTH // 2, 0)

# Opcional: remover a propriedade navigator.webdriver (bypass básico)
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
        """
    }
)

'''Etapas do teste'''

try:
    # 1) Abre a página inicial
    driver.get(index_url)
    print("➜ index.html carregado.")
    time.sleep(2)

    # 2) Clica em “Cartão de Crédito”
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Cartão de Crédito"))
    ).click()
    print("➜ Clicou em Cartão de Crédito.")
    time.sleep(2)

    # 3) Preenche os campos do cartão de crédito
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "numeroCartao"))
    ).send_keys("1234 5678 9101 1121")
    print("✅ Número do cartão preenchido.")
    time.sleep(2)

    driver.find_element(By.ID, "dataValidade").send_keys("12/28")
    print("✅ Data de validade preenchida.")
    time.sleep(2)

    driver.find_element(By.ID, "cvv").send_keys("123")
    print("✅ CVV preenchido.")
    time.sleep(2)

    driver.find_element(By.ID, "nomeTitular").send_keys("Joma")
    print("✅ Nome do titular preenchido.")
    time.sleep(2)

    # 4) Seleciona o parcelamento em 3x
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(., 'Parcelamento em 3x')]"))
    ).click()
    print("✅ Parcelamento em 3x selecionado.")
    time.sleep(2)

    # 5) Exibe o bloco de pagamento e clica em “Fazer Pagamento”
    driver.execute_script("document.getElementById('info-pagamento').style.display = 'block';")
    time.sleep(2)
    
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn-pagamento"))
    ).click()
    print("✅ Botão Fazer Pagamento clicado.")
    time.sleep(2)

    # 6) Verifica o popup de sucesso
    popup = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "popupPagamento"))
    )
    if popup.is_displayed():
        print("🎉 Popup de sucesso visível!")

except Exception as e:
    print("❌ Ocorreu um erro:", e)

finally:
    time.sleep(5)
    driver.quit()
