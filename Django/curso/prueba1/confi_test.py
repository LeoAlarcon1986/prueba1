import re
import time
import random
import pytest
import sys
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import funciones_globales

#playwright show-trace trace.zip
#pytest Multiples_test.py::test_upload
#pytest multiples_test.py -s -v

tiempo=0.5
ruta="Proyecto_2/Django/"  
pdf1="C:/Proyecto_2/Django/curso/prueba1/pdf/Pensión Juan Agosto 2023.pdf"
url="https://www.saucedemo.com/v1/"


#@pytest.mark.skipif(tiempo>=1.5, reason="no se ejecuta por tiempo")
#@pytest.fixture(scope="function")
@pytest.fixture(scope="session")
def set_up(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    context.tracing.start(screenshots=True,snapshots=True,sources=True)
    page=context.new_page()
    f=funciones_globales(page)
    page.goto(url)
    page.set_default_timeout(2000)
    page.mouse.wheel(0,400)
    
    f.Texto("//input[contains(@id,'user-name')]","standard_user",tiempo)
    f.Texto("//input[contains(@id,'password')]","secret_sauce",tiempo)
    f.click("//input[contains(@id,'login-button')]",tiempo)
    
        
    yield page
    context.tracing.stop(path="trace2.zip")
    context.close()
    browser.close()
    
    
@pytest.fixture(scope="session")
def set_up_val_num(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    context.tracing.start(screenshots=True,snapshots=True,sources=True)
    page=context.new_page()
    f=funciones_globales(page)
    page.goto(url)
    page.set_default_timeout(2000)
    page.mouse.wheel(0,400)
    
    f.Texto("//input[contains(@id,'user-name')]","standard_user2",tiempo)
    f.Texto("//input[contains(@id,'password')]","secret_sauce",tiempo)
    f.click("//input[contains(@id,'login-button')]",tiempo)
    
        
    yield page
    context.tracing.stop(path="trace2.zip")
    context.close()
    browser.close()
    
@pytest.fixture(scope="session")
def set_up_val_pass(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    context.tracing.start(screenshots=True,snapshots=True,sources=True)
    page=context.new_page()
    f=funciones_globales(page)
    page.goto(url)
    page.set_default_timeout(2000)
    page.mouse.wheel(0,400)
    
    f.Texto("//input[contains(@id,'user-name')]","standard_user",tiempo)
    f.Texto("//input[contains(@id,'password')]","secret_saucee",tiempo)
    f.click("//input[contains(@id,'login-button')]",tiempo)
    
        
    yield page
    context.tracing.stop(path="trace2.zip")
    context.close()
    browser.close()
    
@pytest.fixture(scope="function")
def set_up_excel(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=tiempo)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    context.tracing.start(screenshots=True,snapshots=True,sources=True)
    page=context.new_page()
    f=funciones_globales(page)
    url="https://testingqarvn.com.es/datos-personales/"
    page.goto(url)
    page.set_default_timeout(2000)
    page.mouse.wheel(0,400)
    
        
    yield page
    context.tracing.stop(path="trace2.zip")
    context.close()
    browser.close()