from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver_path = '../chromedriver-linux64/chromedriver'

service = Service(driver_path)

driver = webdriver.Chrome(service = service)


driver.get("https://es.wallapop.com/coches-segunda-mano")

time.sleep(2)

titulo = driver.find_element(By.TAG_NAME, "h1")

print(titulo.text)

driver.quit()