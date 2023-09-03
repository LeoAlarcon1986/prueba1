import re
import time
import random
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import funciones_globales

tiempo=0.7
ruta="Proyecto_2\\Django"  

def test_select2(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    page=context.new_page()
    page.goto("https://testingqarvn.com.es/combobox-dependiente/")
    expect(page).to_have_title("ComboBox Dependiente | TestingQaRvn")
    page.set_default_timeout(2000)
    #page.mouse.wheel(0,400)
    
    #creando objeto de tipo funciones globales
    f=funciones_globales(page)
    f.esperar(2)
    f.scroll(0,500,2)
    
    # Datos Personales
    f.Texto_imagen("//input[contains(@id,'wsf-1-field-54')]","leonardo",ruta+"nombre.png",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-55')]","Alarcon",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-56')]","QA@gmail.com",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-57')]","3202375722",tiempo)
    f.Texto("//textarea[contains(@id,'wsf-1-field-58')]","Calle 148#101-00",tiempo)
    
    #checkbox
    f.click("//label[contains(@id,'wsf-1-label-59-row-1')]",tiempo)
    f.click_img("//label[contains(@id,'wsf-1-label-60-row-1')]",ruta+"radio.png",tiempo)
    
    #Combobox
    f.combo_img("//select[contains(@id,'wsf-1-field-61')]","Windows",ruta+"combo.png",tiempo)
    #f.combo_label_img("//select[contains(@id,'wsf-1-field-53')]","Mac",ruta+"combo2.png",tiempo)
    
    #Metodo random
    numA=random.sample(range(1,4),1)
    print(numA[0])
    f.combo_label_img("//select[contains(@id,'wsf-1-field-63')]","Windows",ruta+"combo2.png",tiempo)
    
    if numA[0]==1:
      print("es el uno")
      f.combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows 7",tiempo)
    elif numA[0]==2:
      print("es el dos")
      f.combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows 10",tiempo)
    elif numA[0]==3:
      print("es el tres")
      f.combo_label("//select[contains(@id,'wsf-1-field-63')]","Windows Server",tiempo)
    
    #submit
    f.click("//button[contains(@id,'wsf-1-field-62')]",tiempo)
    
    #validar url
    f.validar_url("https://testingqarvn.com.es/combobox-dependiente/",tiempo)
    
    #validar confirmacion
    #f.validar_texto("//p[contains(.,'Gracias por tu encuesta.')]","Gracias",tiempo)
    
    
    
    
    
    
    
    
    
    context.close()
    browser.close()
    
    