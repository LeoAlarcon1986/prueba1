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
    page.goto("https://testingqarvn.com.es/calendarios/")
    page.set_default_timeout(2000)
    #page.mouse.wheel(0,400)
    
    #creando objeto de tipo funciones globales
    f=funciones_globales(page)
    f.esperar(2)
    f.scroll(0,500,2)
    
    # Datos Personales
    f.Texto("//input[contains(@id,'wsf-1-field-66')]","leonardo",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-67')]","Alarcon",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-68')]","QA@gmail.com",tiempo)
    f.Texto("//input[contains(@id,'wsf-1-field-69')]","3202375722",tiempo)
    f.Texto("//textarea[contains(@id,'wsf-1-field-70')]","Calle 148#101-00",tiempo)
    
    #checkbox
    f.click("//label[contains(@id,'wsf-1-label-71-row-2')]",tiempo)
    f.click("//label[contains(@id,'wsf-1-label-72-row-3')]",tiempo)
    
    #Combobox
    #f.combo_value("//select[contains(@id,'wsf-1-field-73')]","Mac",tiempo)
    #f.combo_label_img("//select[contains(@id,'wsf-1-field-53')]","Mac",ruta+"combo2.png",tiempo)
    
    #Metodo random
    numA=random.sample(range(1,4),1)
    print(numA[0])
    f.combo_label("//select[contains(@id,'wsf-1-field-73')]","Mac",tiempo)
    
    if numA[0]==1:
      print("es el uno")
      f.combo_label("//select[contains(@id,'wsf-1-field-76')]","Capitan",tiempo)
    elif numA[0]==2:
      print("es el dos")
      f.combo_label("//select[contains(@id,'wsf-1-field-76')]","Yosemite",tiempo)
    elif numA[0]==3:
      print("es el tres")
      f.combo_label("//select[contains(@id,'wsf-1-field-76')]","Mavericks",tiempo)
      
      #calendarios
      
      f.Texto("//input[@id='wsf-1-field-79']","Agosto 7, 2023",tiempo)
      f.Texto("//input[contains(@id,'wsf-1-field-78')]","Agosto 24, 2023",tiempo)
      time.sleep(2)
      
      # Hacer click en otra area
      # page.mouse.click(0,50)  # cordenadas de donde hacer click en X,Y
      # f.esperar(3)
      
      # hacer tab en vex de click en una xpath
      page.keyboard.press("Tab")
      f.esperar(3)
      
      
    
    #submit
    f.click("//button[contains(@type,'submit')]",tiempo)
    
    #validar url
    #f.validar_url("https://testingqarvn.com.es/combobox-dependiente/",tiempo)
    
    #validar confirmacion
    #f.validar_texto("//p[contains(.,'Gracias por tu encuesta.')]","Gracias",tiempo)
    
   
    
    
    
    
    
    
    
    context.close()
    browser.close()
    
    