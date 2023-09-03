import re
import time
import random
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import  funciones_globales

#playwright codegen https://www.saucedemo.com/v1/
#playwright show-trace trace2.zip

tiempo=0.5
ruta="Proyecto_2/Django/"  
pdf1="C:/Proyecto_2/Django/curso/prueba1/pdf/Pensión Juan Agosto 2023.pdf"

def test_generator(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    #inicia Trace Viewer
    context.tracing.start(screenshots=True,snapshots=True,sources=True)
    
    page=context.new_page()
    page.goto("https://www.saucedemo.com/v1/")
    
    page.set_default_timeout(2000)
    page.mouse.wheel(0,400)
    time.sleep(1)
    
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Tab")
    page.get_by_role("button", name="LOGIN").press("Enter")
    page.locator("div").filter(has_text=re.compile(r"^\$29\.99ADD TO CART$")).get_by_role("button").click()
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="All Items").click()
    page.get_by_role("link", name="1").click()
    page.get_by_role("button", name="REMOVE").click()
    
    context.tracing.stop(path="trace2.zip")
    context.close()
    browser.close()