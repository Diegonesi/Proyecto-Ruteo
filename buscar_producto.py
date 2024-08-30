from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Generar_link(numero):
    producto = input("Ingrese Producto: ")
    link = f'https://www.solotodo.cl/search?categories={numero}&search={producto}'
    return link

while True:
    print("¿Qué desea buscar?\n 1-Procesador\n 2-Tarjeta de video\n 3-Placa Madre\n 4-CPU Cooler\n 5-Disco Duro (HDD)\n 6-Fuente de Poder \n 7-Gabinetes \n 8-RAM \n 9-Monitores \n 10-Ventiladores \n 11-SSD")
    
    opcion = int(input("Ingrese el número de la opción: "))
    
    if opcion == 1:
        print("Has elegido: Procesador")
        link = Generar_link(3)
        break
    elif opcion == 2:
        print("Has elegido: Tarjeta de video")
        link = Generar_link(2)
        break
    elif opcion == 3:
        print("Has elegido: Placa Madre")
        link = Generar_link(5)
        break
    elif opcion == 4:
        print("Has elegido: CPU Cooler")
        link = Generar_link(12)
        break
    elif opcion == 5:
        print("Has elegido: Disco Duro (HDD)")
        link = Generar_link(8)
        break
    elif opcion == 6:
        print("Has elegido: Fuente de Poder")
        link = Generar_link(9)
        break
    elif opcion == 7:
        print("Has elegido: Gabinetes")
        link = Generar_link(10)
        break
    elif opcion == 8:
        print("Has elegido: RAM")
        link = Generar_link(7)
        break
    elif opcion == 9:
        print("Has elegido: Monitores")
        link = Generar_link(4)
        break
    elif opcion == 10:
        print("Has elegido: Ventilador")
        link = Generar_link(87)
        break
    elif opcion == 11:
        print("Has elegido: SSD")
        link = Generar_link(39)
        break
    else:
        print("Opcion no valida. Por favor, intente de nuevo.")


edge_service = Service('C:/Users/diego/Downloads/edgedriver_win64/msedgedriver.exe') #Cambia dependiendo del pc, se descarga el driver https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads
edge_options = Options()
edge_options.add_argument("--headless") 
driver = webdriver.Edge(service=edge_service, options=edge_options)

# Abre la página web
driver.get(f'{link}')

try:
    # Espera a que los elementos sean visibles
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-1g4yje1'))
    )
    
    for product_div in elements:
        try:
            product_link = product_div.find_element(By.TAG_NAME, 'a').get_attribute('href')
            product_name = product_div.find_element(By.CLASS_NAME, 'MuiTypography-h5').text
            product_price = product_div.find_element(By.CLASS_NAME, 'MuiTypography-h2').text
            product_specs = product_div.find_element(By.CLASS_NAME, 'ProductPage_product_specs__pYVnc').text

            print(f"Link: {product_link}")
            print(f"Nombre: {product_name}")
            print(f"Precio: {product_price}")
            print(f"Especificaciones: {product_specs}")
            print('---' * 10)  

        except Exception as e:
            print(f"Error al extraer datos de un producto: {e}")

finally:
    # Cierra el navegador
    driver.quit()
