import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Para_Scraping.Actuaciones import informacion_tabla_accion ,informacion_tabla_notas
from Para_Scraping.Intervenientes import informacion_tabla_partes, informacion_tabla_fiscales
from Para_Scraping.Vinculados import informacion_tabla_viculados
from Para_Scraping.Recursos import informacion_tabla_recursos

def acceder_a_elementos(driver, link, Expediente):
    #Variable de espera, hasta 10 segundos
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@onclick=\"{link}\"]"))).click()

    #Tiempo para cargar el html de cada página
    time.sleep(1)

    #Sección de 'actuaciones'
    #print('Actuaciones')
    informacion_tabla_accion(driver, Expediente)
    #print('Notas')
    informacion_tabla_notas(driver, Expediente)

    #Espera a que cargue el botón 'intevinientes'
    wait.until(EC.element_to_be_clickable((By.ID, "expediente:j_idt261:header:inactive"))).click()
    time.sleep(1)

    #print('Intervinientes')
    #print('Partes')
    informacion_tabla_partes(driver, Expediente)
    #print('Fiscales')
    informacion_tabla_fiscales(driver, Expediente)

    #Espera a que cargue el botón 'Vinculados'
    wait.until(EC.element_to_be_clickable((By.ID, "expediente:j_idt339:header:inactive"))).click()
    time.sleep(1)
    
    #print('Vinculados')
    informacion_tabla_viculados(driver, Expediente)
    
    #Espera a que cargue el botón 'Recursos'
    wait.until(EC.element_to_be_clickable((By.ID, "expediente:j_idt371:header:inactive"))).click()
    time.sleep(1)
    
    #print('Recursos')    
    informacion_tabla_recursos(driver, Expediente)

    #Espera a que cargue el botón para volver al inicio
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@onclick=\"history.go(-1); return false;\"]"))).click()
   