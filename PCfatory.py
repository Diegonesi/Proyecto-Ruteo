from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://www.myshop.cl/producto/monitor-gamer-27-xiaomi-g27i-full-hd-1920x1080-1-ms-165-hz-ips-p27fbb-rggl--52756-p27703'
edge_service = Service('C:/Users/diego/Downloads/edgedriver_win64/msedgedriver.exe') #Cambia dependiendo del pc, se descarga el driver https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads
edge_options = Options()
edge_options.add_argument("--headless") 
driver = webdriver.Edge(service=edge_service, options=edge_options)

# Abre la página web
driver.get(f'{link}')

try:
   # Espera a que el nombre del producto sea visible y lo extrae
    product_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
    ).text
    
    prices = driver.find_elements(By.CLASS_NAME, 'price_box')
    price_efectivo = prices[0].find_element(By.CLASS_NAME, 'current_price').text
    price_credito = prices[1].find_element(By.CLASS_NAME, 'current_price').text
    # Extrae la disponibilidad
    availability = driver.find_element(By.CLASS_NAME, 'product_desc').text.strip()

    # Muestra los datos extraídos

    print(f"Nombre del Producto: {product_name}")
    print(f"Precio Efectivo o Transferencia: {price_efectivo}")
    print(f"Precio Débito o Crédito: {price_credito}")
    print(f"Disponibilidad: {availability}")


finally:
    # Cierra el navegador
    driver.quit()



