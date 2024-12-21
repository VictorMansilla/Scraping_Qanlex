from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

from Base_de_datos.Intervinientes_base_datos import Tabla_partes, Tabla_fiscales

def informacion_tabla_partes(driver, Expediente):
    espera = WebDriverWait(driver, 10)
    pagina_de_tabla_accion = 0

    while True:        
        html = driver.page_source
        html_parseado = BeautifulSoup(html, 'html.parser')
        elementos_tr_extraidos = html_parseado.find_all('tr')

        if elementos_tr_extraidos:

            for elemento in elementos_tr_extraidos:
                elementos_td_extraidos = elemento.find_all('td')

                if len(elementos_td_extraidos) == 4:
                    Tipo =  elementos_td_extraidos[0].get_text(strip=True) if "TIPO :" not in elementos_td_extraidos[0].get_text(strip=True) else elementos_td_extraidos[0].get_text(strip=True).replace("TIPO :","")
                    Nombre = elementos_td_extraidos[1].get_text(strip=True) if "NOMBRE :" not in elementos_td_extraidos[1].get_text(strip=True) else elementos_td_extraidos[1].get_text(strip=True).replace("NOMBRE :","")
                    Tomo_folio = elementos_td_extraidos[2].get_text(strip=True).replace("Tomo:","") if elementos_td_extraidos[2].get_text(strip=True) != "" else None
                    IEJ = elementos_td_extraidos[3].get_text(strip=True) if elementos_td_extraidos[3].get_text(strip=True) != "" else None

                    Tabla_partes(Expediente, Tipo, Nombre, Tomo_folio, IEJ)
                    #print({"Tipo":Tipo, "Nombre":Nombre, "Tipo":Tipo, "Tomo_folio":Tomo_folio, "IEJ":IEJ})
        
        if pagina_de_tabla_accion <= 5:
            pagina_de_tabla_accion += 1
        id = f"expediente:j_idt289:j_idt251:{pagina_de_tabla_accion}:j_idt253"
        boton_siguiente = html_parseado.find(id=id)

        if boton_siguiente != None:
            espera.until(EC.element_to_be_clickable((By.ID, id))).click()
            time.sleep(2)

        else:break



def informacion_tabla_fiscales(driver, Expediente):
    espera = WebDriverWait(driver, 10)
    pagina_de_tabla_accion = 0

    while True:        
        html = driver.page_source
        html_parseado = BeautifulSoup(html, 'html.parser')
        elementos_tr_extraidos = html_parseado.find_all('tr')
        
        if elementos_tr_extraidos:

            for elemento in elementos_tr_extraidos:
                elementos_td_extraidos = elemento.find_all('td')

                if len(elementos_td_extraidos) == 3:
                    Fiscalia = elementos_td_extraidos[0].get_text(strip=True) if elementos_td_extraidos[0].get_text(strip=True) != "" else None
                    Fiscal = elementos_td_extraidos[1].get_text(strip=True) if elementos_td_extraidos[1].get_text(strip=True) != "" else None
                    IEJ = elementos_td_extraidos[2].get_text(strip=True) if elementos_td_extraidos[2].get_text(strip=True) != "" else None

                    Tabla_fiscales(Expediente, Fiscalia, Fiscal, IEJ)
                    #print({"Fiscalia":Fiscalia, "Fiscal":Fiscal, "IEJ":IEJ})
        
        if pagina_de_tabla_accion <= 5:
            pagina_de_tabla_accion += 1
        id = f"expediente:j_idt289:j_idt251:{pagina_de_tabla_accion}:j_idt253"
        boton_siguiente = html_parseado.find(id=id)

        if boton_siguiente != None:
            espera.until(EC.element_to_be_clickable((By.ID, id))).click()
            time.sleep(2)

        else:break