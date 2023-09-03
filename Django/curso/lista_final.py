import re
import time
import random
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import  funciones_globales

#correr de forma normal
#playwright show-trace trace.zip
# set PWDEBUG=1   # Lanzando Debug   se ejecuta pytest nombre del archivo.py -s  /// page.pause()

tiempo=0.5
ruta="Proyecto_2/Django/"  
pdf1="C:/Proyecto_2/Django/curso/prueba1/pdf/Pensión Juan Agosto 2023.pdf"

def test_lista_final(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    #inicia Trace Viewer
    context.tracing.start(screenshots=True,snapshots=True,sources=True)
    
    page=context.new_page()
    page.goto("https://www.google.com/")
    
    page.set_default_timeout(2000)
    page.mouse.wheel(0,400)
    time.sleep(1)
    f=funciones_globales(page)
    #f.validar_titulo_pagina("google")
    f.validar_url("https://www.google.com/")
    f.Texto("//*[@id='APjFqb']","ferra",1)
    f.click("//span[contains(.,'Ferragamo')]",2)
    #f.click_primero("//*[@id='APjFqb']",2)
    f.esperar(3)
    
    
    # cierre trace Viewer
    context.tracing.stop(path="trace.zip")
    
    context.close()
    browser.close()
   