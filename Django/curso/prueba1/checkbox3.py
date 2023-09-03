
# playwright codegen  https://testingqarvn.com.es/prueba-de-campos-checkbox/

import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright



def test_checkbox3(playwright: Playwright, page: Page) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=1000)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    
    page=context.new_page()
    page.goto("https://testingqarvn.com.es/prueba-de-campos-checkbox/")
    expect(page).to_have_title("Prueba de campos Checkbox | TestingQaRvn")
    page.set_default_timeout(5000)

    #Scroll de pagina
    page.mouse.wheel(0,400)
    #Nombre y Apellido
    page.locator("//input[contains(@id,'wsf-1-field-29')]").fill("leonardo")
    page.locator("//input[contains(@id,'wsf-1-field-30')]").fill("Alarcon")

    # Datos Personales
    page.locator("//input[contains(@id,'wsf-1-field-31')]").fill("dima_4444@hotmail.com")
    page.locator("//input[contains(@id,'wsf-1-field-32')]").fill("314 2272019")
    page.locator("//textarea[contains(@id,'wsf-1-field-33')]").fill("Calle 148 # 101-10")

    # Checkbox
#     page.locator("//label[contains(.,'PHP')]").click()
#     page.locator("//label[contains(.,'JS')]").click()
    
#     page.locator("//label[contains(.,'PHP')]").check()
#     page.locator("//label[contains(.,'JS')]").uncheck()

     # Validadores
#     page.locator("//label[contains(.,'PHP')]").check()
#     assert page.locator("//label[contains(.,'PHP')]").is_checked() is True

    for i in range(7,10):
        
#         salida=f"(//label[contains(@class,'wsf-label')])[{i}]"
#         print(salida)
#         page.locator(salida).click()
    
     page.locator(f"(//label[contains(@class,'wsf-label')])[{i}]").click()
    
    context.close()
    browser.close()