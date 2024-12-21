from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

from Base_de_datos.Actuaciones_base_datos import Tabla_actuaciones, Tabla_Notas

def informacion_tabla_accion(driver, Expediente):
    espera = WebDriverWait(driver, 10)
    pagina_de_tabla_accion = 0

    while True:        
        html = driver.page_source
        html_parseado = BeautifulSoup(html, 'html.parser')
        tabla_accion = html_parseado.find(id="expediente:action-table")

        if tabla_accion != None:
            elementos_tr_extraidos = tabla_accion.find_all('tr')

            if elementos_tr_extraidos:

                for elemento in elementos_tr_extraidos:
                    elementos_td_extraidos = elemento.find_all('td')

                    if elementos_td_extraidos:
                        Oficina = elementos_td_extraidos[1].get_text(strip=True).replace("Oficina:","") if elementos_td_extraidos[1].get_text(strip=True).replace("Oficina:","") != "" else None
                        Fecha = elementos_td_extraidos[2].get_text(strip=True).replace("Fecha:","") if elementos_td_extraidos[2].get_text(strip=True).replace("Fecha:","") != "" else None
                        Tipo = elementos_td_extraidos[3].get_text(strip=True).replace("Tipo actuacion:","") if elementos_td_extraidos[3].get_text(strip=True).replace("Tipo actuacion:","") != "" else None
                        Descipcion_detalle = elementos_td_extraidos[4].get_text(strip=True).replace("Detalle:","") if elementos_td_extraidos[4].get_text(strip=True).replace("Detalle:","") != "" else None
                        AFS = elementos_td_extraidos[5].get_text(strip=True) if elementos_td_extraidos[5].get_text(strip=True) != "" else None

                        Tabla_actuaciones(Expediente, Oficina, Fecha, Tipo, Descipcion_detalle, AFS)
                        #print({"Oficina":Oficina, "Fecha":Fecha, "Tipo":Tipo, "Descipcion_detalle":Descipcion_detalle, "AFS":AFS})
            
            if pagina_de_tabla_accion <= 5:
                pagina_de_tabla_accion += 1
            id = f"expediente:j_idt208:j_idt218:{pagina_de_tabla_accion}:j_idt220"
            boton_siguiente = html_parseado.find(id=id)

            if boton_siguiente != None:
                espera.until(EC.element_to_be_clickable((By.ID, id))).click()
                time.sleep(2)

            else:break

        else:break



def informacion_tabla_notas(driver, Expediente):
    pagina_de_tabla_accion = 0

    espera = WebDriverWait(driver, 10)

    while True:
        html = driver.page_source
        html_parseado = BeautifulSoup(html, 'html.parser')
        tabla_notas = html_parseado.find(id="expediente:notas-table")
        
        if tabla_notas != None:
            elementos_tr_extraidos = tabla_notas.find_all('tr')

            if elementos_tr_extraidos:

                for elemento in elementos_tr_extraidos:
                    elementos_td_extraidos = elemento.find_all('td')

                    if elementos_td_extraidos:
                        Fecha = elementos_td_extraidos[0].get_text(strip=True) if elementos_td_extraidos[0].get_text(strip=True) != "" else None
                        Interviniente = elementos_td_extraidos[1].get_text(strip=True) if elementos_td_extraidos[1].get_text(strip=True) != "" else None
                        Descipcion_detalle = elementos_td_extraidos[2].get_text(strip=True) if elementos_td_extraidos[2].get_text(strip=True) != "" else None

                        Tabla_Notas(Expediente, Fecha, Interviniente, Descipcion_detalle)
                        #print({"Fecha":Fecha, "Interviniente":Interviniente, "Descipcion_detalle":Descipcion_detalle})

            if pagina_de_tabla_accion <= 5:
                pagina_de_tabla_accion += 1
            id = f"expediente:j_idt247:j_idt251:{pagina_de_tabla_accion}:j_idt253"
            boton_siguiente = html_parseado.find(id=id)
            
            if boton_siguiente != None:
                espera.until(EC.element_to_be_clickable((By.ID, id))).click()
                time.sleep(2)

            else:break

        else:break