import re
import time
import random
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import funciones_globales

tiempo=0.5
ruta="Proyecto_2/Django/"  
pdf1="C:/Proyecto_2/Django/curso/prueba1/pdf/Pensión Juan Agosto 2023.pdf"

def test_select2(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    page=context.new_page()
    page.goto("https://testingqarvn.com.es/upload-files/")
    page.set_default_timeout(2000)
    #page.mouse.wheel(0,400)
    
    #creando objeto de tipo funciones globales
    f=funciones_globales(page)
    f.esperar(2)
    f.scroll(0,500,2)
    
    # Datos Personales
    f.Texto("//input[contains(@id,'wsf-1-field-80')]","leonardo",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-81')]","Alarcon",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-82')]","QA@gmail.com",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-83')]","3202375722",tiempo)
    f.Texto("//textarea[contains(@id,'wsf-1-field-84')]","Calle 148#101-00",tiempo)
    
    #checkbox
    f.click("//label[contains(@id,'wsf-1-label-85-row-1')]",tiempo)
    f.click("//label[contains(@id,'wsf-1-label-86-row-1')]",tiempo)
    
    #Combobox
    #f.combo_value("//select[contains(@id,'wsf-1-field-73')]","Mac",tiempo)
    #f.combo_label_img("//select[contains(@id,'wsf-1-field-53')]","Mac",ruta+"combo2.png",tiempo)
    
    #Metodo random
    numA=random.sample(range(1,4),1)
    print(numA[0])
    f.combo_label("//select[contains(@id,'wsf-1-field-87')]","Linux",tiempo)
    
    if numA[0]==1:
      print("es el uno")
      f.combo_label("//select[contains(@id,'wsf-1-field-89')]","Ubuntu",tiempo)
    elif numA[0]==2:
      print("es el dos")
      f.combo_label("//select[contains(@id,'wsf-1-field-89')]","Debian",tiempo)
    elif numA[0]==3:
      print("es el tres")
      f.combo_label("//select[contains(@id,'wsf-1-field-89')]","Read Hat",tiempo)
      
    #calendarios 1
    f.click("//input[@id='wsf-1-field-91']",tiempo)
    f.click("(//div[contains(.,'25')])[9]")
    #page.mouse.click(0,50)  # cordenadas de donde hacer click en X,Y
    #f.esperar(3)
    
    #calendarios 2 
    f.click("//input[contains(@id,'wsf-1-field-92')]",tiempo)
    f.click("(//div[contains(.,'26')])[18]")
      
      
    # Hacer click en otra area
    #page.mouse.click(0,50)  # cordenadas de donde hacer click en X,Y
    #f.esperar(3)
      
    # hacer tab en vex de click en una xpath
    # page.keyboard.press("Tab")
    f.Tab(1)
      
    # upload file
    f.upload_file("//input[contains(@id,'wsf-1-field-94')]",pdf1,tiempo)
    
    #remove file
    f.upload_file_remove("//input[contains(@id,'wsf-1-field-94')]",tiempo)
    
    #submit
    f.click("//*[@id='wsf-1-field-93']",tiempo)
    time.sleep(2)
    
    #validar url
    #f.validar_url("https://testingqarvn.com.es/upload-files/",tiempo)
    
    #validar confirmacion
    #f.validar_texto("//p[contains(.,'Gracias por tu encuesta.')]","Gracias",tiempo)
    
   
    
    
    
    
    
    
    
    context.close()
    browser.close()
    
    