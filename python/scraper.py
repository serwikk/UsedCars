from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver_path = '../chromedriver-linux64/chromedriver'

service = Service(driver_path)

driver = webdriver.Chrome(service = service, options=chrome_options)

all_results = []

driver.get("https://es.wallapop.com/coches-segunda-mano")

time.sleep(3)

ul_elements = driver.find_elements(By.XPATH, '//ul[@aria-label="Items list"]')

# Para cada <ul>, encuentra los enlaces <a> dentro de él
for ul in ul_elements:
    li_elements = ul.find_elements(By.XPATH, './li')  # Encuentra todos los <li> hijos directos
    for li in li_elements:
        # Extraer datos específicos de cada <li>
        try:
            price = li.find_element(By.XPATH, './/strong[@data-testid="card-info-price"]').text
        except:
            price = "N/A"

        try:
            title = li.find_element(By.XPATH, './/h3').text
        except:
            title = "N/A"

        try:
            additional_info = li.find_element(By.XPATH, './/p[contains(@class, "additionalInfo")]').text
        except:
            additional_info = "N/A"

        try:
            description = li.find_element(By.XPATH, './/p[contains(@class, "description")]').text
        except:
            description = "N/A"

        try:
            link = li.find_element(By.XPATH, './/a').get_attribute('href')
        except:
            link = "N/A"

        # Imprimir los datos extraídos
        # print(f"Precio: {price}")
        # print(f"Título: {title}")
        # print(f"Información adicional: {additional_info}")
        # print(f"Descripción: {description}")
        # print(f"Link: {link}")
        # print("-" * 40)

        result = {
            "price" : price,
            "title": title,
            "additional_info" : additional_info,
            "description" : description,
            "link" : link
        } 

        all_results.append(result)



# Cerrar el navegador
driver.quit()


import csv

with open("wallapop_cars.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["price", "title", "additional_info", "description", "link"])
    writer.writeheader()
    writer.writerows(all_results)

print("Datos guardados en 'wallapop_cars.csv'.")