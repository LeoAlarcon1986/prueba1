import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import funciones_globales

tiempo=0.7
ruta="Proyecto_2\\Django"  

def test_select1(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    page=context.new_page()
    page.goto("https://testingqarvn.com.es/combobox/")
    expect(page).to_have_title("ComboBox | TestingQaRvn")
    page.set_default_timeout(2000)
    #page.mouse.wheel(0,400)
    
    #creando objeto de tipo funciones globales
    f=funciones_globales(page)
    f.esperar(2)
    f.scroll(0,500,2)
    
    # Datos Personales
    f.Texto_imagen("//input[contains(@id,'wsf-1-field-45')]","leonardo",ruta+"nombre.png",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-46')]","Alarcon",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-47')]","QA@gmail.com",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-48')]","3202375722",tiempo)
    f.Texto("//textarea[contains(@id,'wsf-1-field-49')]","Calle 148#101-00",tiempo)
    
    #checkbox
    f.click("//label[contains(@id,'wsf-1-label-50-row-2')]",tiempo)
    f.click_img("//label[contains(@id,'wsf-1-label-51-row-1')]",ruta+"radio.png",tiempo)
    
    #Combobox
    f.combo_img("//select[contains(@id,'wsf-1-field-53')]","Linux",ruta+"combo.png",tiempo)
    f.combo_label_img("//select[contains(@id,'wsf-1-field-53')]","Mac",ruta+"combo2.png",tiempo)
    
    #submit
    f.click("//button[contains(@id,'wsf-1-field-52')]",tiempo)
    
    #validar url
    f.validar_url("https://testingqarvn.com.es/combobox/",tiempo)
    
    #validar confirmacion
    f.validar_texto("//p[contains(.,'Gracias por tu encuesta.')]","Gracias",tiempo)
    
    
    
    
    
    
    
    
    
    context.close()
    browser.close()
    
    