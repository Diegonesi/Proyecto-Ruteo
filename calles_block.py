from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#https://www.transporteinforma.cl/estado_de_transito/restriccion-de-la-pista-derecha-en-carlos-antunez-entre-marchant-pereira-y-av-ricardo-lyon-entre-las-0930-y-1730-horas-por-trabajos-en-la-via-trabajos-se-extenderan-hacia-av-tobalaba-con-fecha-de/

link = 'https://www.transporteinforma.cl/'
edge_service = Service('C:/Users/diego/Downloads/edgedriver_win64/msedgedriver.exe') #Cambia dependiendo del pc, se descarga el driver https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads
edge_options = Options()
edge_options.add_argument("--headless") 
driver = webdriver.Edge(service=edge_service, options=edge_options)

# Abre la página web
driver.get(f'{link}')

try:
   # Espera a que todos los enlaces sean visibles
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'trafficCondition__list__item'))
    )
    
    # Recorre todos los elementos encontrados
    for element in elements:
        # Extrae el href de cada enlace
        href = element.get_attribute('href')

        # Extrae el texto de la clase de cada enlace
        link_text = element.text.strip()

        # Muestra los datos extraídos
        print(f"Href: {href}")
        print(f"Información: {link_text}")
        print('---' * 10)  # Separador entre elementos

finally:
    # Cierra el navegador
    driver.quit()



