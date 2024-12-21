from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



def acceder(driver):
    #Variable de espera, hasta 10 segundos
    espera = WebDriverWait(driver, 10)
    
    #Eespera a que el elemento "Por parte" esté visible y hacer clic
    espera.until(EC.element_to_be_clickable((By.ID, 'formPublica:porParte:header:inactive'))).click()

    #Encuentra el menú de opciones
    opciones = espera.until(EC.element_to_be_clickable((By.ID, "formPublica:camaraPartes")))
    #Presiona y despliega el menú de opciones
    opciones.click()

    seleccionar = Select(opciones)

    #Selecciona la opción por el texto visible
    seleccionar.select_by_visible_text("COM - Camara Nacional de Apelaciones en lo Comercial")

    #Presiona la selección
    opciones.click()

    #Espera a que el input esté visible
    espera.until(EC.presence_of_element_located((By.ID, 'formPublica:nomIntervParte')))

    #Ingresa la palabra clave "RESIDUOS" dentro del input
    input_element = driver.find_element(By.ID, 'formPublica:nomIntervParte')
    input_element.send_keys('RESIDUOS')
