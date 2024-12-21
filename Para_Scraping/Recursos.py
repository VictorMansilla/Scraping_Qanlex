from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

from Base_de_datos.Recursos_base_datos import Tabla_recursos

def informacion_tabla_recursos(driver, Expediente):
    espera = WebDriverWait(driver, 10)
    pagina_de_tabla_accion = 0

    while True:        
        html = driver.page_source
        html_parseado = BeautifulSoup(html, 'html.parser')
        tabla_accion = html_parseado.find(id="expediente:recursosTable")

        if tabla_accion != None:
            elementos_tr_extraidos = tabla_accion.find_all('tr')

            if elementos_tr_extraidos:

                for elemento in elementos_tr_extraidos:
                    elementos_td_extraidos = elemento.find_all('td')

                    if len(elementos_td_extraidos) == 6:
                        Recurso = elementos_td_extraidos[0].get_text(strip=True) if elementos_td_extraidos[0].get_text(strip=True) != "" else None
                        Oficina_de_evaluacion = elementos_td_extraidos[1].get_text(strip=True) if elementos_td_extraidos[1].get_text(strip=True) != "" else None
                        Fecha_de_presentacion = elementos_td_extraidos[2].get_text(strip=True) if elementos_td_extraidos[2].get_text(strip=True) != "" else None
                        Tipo_de_recurso = elementos_td_extraidos[3].get_text(strip=True) if elementos_td_extraidos[3].get_text(strip=True) != "" else None
                        Estado_actual = elementos_td_extraidos[4].get_text(strip=True) if elementos_td_extraidos[4].get_text(strip=True) != "" else None

                        Tabla_recursos(Expediente, Recurso, Oficina_de_evaluacion, Fecha_de_presentacion, Tipo_de_recurso, Estado_actual)
                        #print({"Recurso":Recurso, "Oficina_de_evaluacion":Oficina_de_evaluacion, "Fecha_de_presentacion":Fecha_de_presentacion, "Tipo_de_recurso":Tipo_de_recurso, "Estado_actual":Estado_actual})
            
            if pagina_de_tabla_accion <= 5:
                pagina_de_tabla_accion += 1
            id = f"expediente:j_idt366:j_idt251:{pagina_de_tabla_accion}:j_idt253"
            boton_siguiente = html_parseado.find(id=id)

            if boton_siguiente != None:
                espera.until(EC.element_to_be_clickable((By.ID, id))).click()
                time.sleep(2)

            else:break

        else:
            #print('No hay tabla aquí')
            break