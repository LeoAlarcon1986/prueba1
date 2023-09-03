import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

class funciones_globales:
    #constructor
    def __init__(self,page):
        self.page=page 
        
    def esperar(self,tiempo):
        time.sleep(tiempo)
        
    def scroll(self,x,y,tiempo):
        self.page.mouse.wheel(x,y)
        time.sleep(tiempo)
        
    def Texto(self,selector,texto,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()    # Hace que el texto se vea azul , es como un comentario
        t.fill(texto)   # Escribe en el selector del navegador
        time.sleep(tiempo)
        
        
    def Texto_imagen(self,selector,texto,ruta,tiempo=0.5):   # funcion que envie foto del nombre 
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        expect(t).to_be_empty()
        t.highlight()    # Hace que el texto se vea azul , es como un comentario
        t.fill(texto)   # Escribe en el selector del navegador
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def click(self,selector,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        time.sleep(tiempo)
        
    def click_img(self,selector,ruta,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def combo_value(self, selector, valor,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(valor)
        time.sleep(tiempo)
        
    def combo_img(self,selector,valor,ruta,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(valor)
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def combo_label(self, selector, valor,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(label=valor)
        time.sleep(tiempo)
        
    def combo_label_img(self, selector, valor,ruta,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.select_option(label=valor)
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def validar_url(self,texto,tiempo=0.5):
        expect(self.page).to_have_url(re.compile(texto))
        time.sleep(tiempo)
        
    def validar_texto(self,selector,texto,tiempo=0.5):
        t=self.page.locator(selector)
        expect(t).to_contain_text(texto)
        time.sleep(tiempo)
    
    def mouse_xy(self,x,y,tiempo=0.5):
        self.page.mouse.click(x.y)
        time.sleep(tiempo)
        
    def Tab(self,tiempo=0.5):
        self.page.keyboard.press("Tab")
        time.sleep(tiempo)
        
    def upload_file(self,selector,archivo,tiempo=0.5):
        self.page.locator(selector).set_input_files(archivo)
        time.sleep(tiempo)
        
    def upload_file_img(self,selector,archivo,ruta,tiempo=0.5):
        self.page.locator(selector).set_input_files(archivo)
        self.page.screenshot(path=ruta)
        time.sleep(tiempo)
        
    def upload_file_remove(self,selector,tiempo=0.5):
        self.page.locator(selector).set_input_files([])
        time.sleep(tiempo)