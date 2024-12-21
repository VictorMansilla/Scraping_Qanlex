import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Acceder import acceder
from Acceder_a_elementos import acceder_a_elementos
from Base_de_datos.Tabla_expedientes import Tabla_expedientes

#Ajustes para iniciar la ventana
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#Url del sitio
driver.get("http://scw.pjn.gov.ar/scw/home.seam")

#Función que automatiza el inicio
acceder(driver)

#20 segundos para completar el chaptcha
time.sleep(20)

contador = 0

#Ciclo while que recorre todas las páginas
while True:
    #Extrae el html de la página actual
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #Buscar todos los elementos tr en la página
    elementos_tr = soup.find_all('tr')

    #Recorre los elementos obtenidos del tr
    for elemento in elementos_tr:
        
        if len(elemento) == 13:
            #Buscar todos los elementos td en la página
            elementos_td = elemento.find_all('td')

            #Si hay elementos dentro de td eextrae la información
            if elementos_td:
                Expediente = elementos_td[0].get_text(strip=True) if elementos_td[0].get_text(strip=True) != "" else None
                Dependencia = elementos_td[1].get_text(strip=True) if elementos_td[1].get_text(strip=True) != "" else None
                Caratula = elementos_td[2].get_text(strip=True) if elementos_td[2].get_text(strip=True) != "" else None
                Situacion = elementos_td[3].get_text(strip=True) if elementos_td[3].get_text(strip=True) != "" else None
                Ultima_actualizacion = elementos_td[4].get_text(strip=True) if elementos_td[4].get_text(strip=True) != "" else None
                link = str(elementos_td[5].find_all(onclick=True)[0]).split('"')[5]

                #Se cargan los expedientes a la base de datos
                Tabla_expedientes(Expediente=Expediente,
                                  Dependencia=Dependencia,
                                  Caratula=Caratula,
                                  Situacion=Situacion,
                                  Ultima_actualizacion=Ultima_actualizacion)

                #print({"Expediente":Expediente, "Dependencia":Dependencia, "Caratula":Caratula, "Situacion":Situacion, "Ultima_actualizacion":Ultima_actualizacion})

                #Accede a cada expediente en particular para extaer la información y cargarla a la base de datos
                acceder_a_elementos(driver, link, Expediente)

                contador += 1
                #print(f"Este es el elemento principal: {contador}")
                #print('____________________________________________________________________________________________________________________________________________________________________________________')

    #Obtiene el link para ir a la siguiente página
    html = driver.page_source
    link_pagina_siguiente = BeautifulSoup(html, 'html.parser')
    id_del_boton_siguiente = link_pagina_siguiente.find_all('a', id=True, onclick=True)
    boton_siguiente_o_no = id_del_boton_siguiente[0].get_text(strip=True)
    id = id_del_boton_siguiente[0].get('id')

    #Si no existe una página siguiente cierra el ciclo while
    if boton_siguiente_o_no != 'Siguiente' or boton_siguiente_o_no == 'Anterior':
        #print('Fin del bucle while\n')
        break

    espera = WebDriverWait(driver, 10)
    espera.until(EC.element_to_be_clickable((By.ID, id))).click()

    #print('Llendo a la siguiente pestaña')
    #Tiempo de recarga de la siguiente página
    time.sleep(1.5)

#Cierra la ventana luego de 5000 segundos de terminar de scrapear
time.sleep(5000)
driver.quit()