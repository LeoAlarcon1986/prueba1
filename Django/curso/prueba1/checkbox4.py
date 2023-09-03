
# playwright codegen  https://testingqarvn.com.es/prueba-de-campos-checkbox/

import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright



def test_checkbox4(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    context=browser.new_context(
         viewport={"width": 1300, "height":600},
         #record_video_dir="videos/ckeckbox3"
    )
    
    page=context.new_page()
    page.goto("https://datatables.net/extensions/select/examples/initialisation/checkbox.html")
    expect(page).to_have_title("DataTables example - Checkbox selection")
    page.set_default_timeout(2000)

    #Scroll de pagina
    page.mouse.wheel(0,400)
    time.sleep(0.7)
    
    # for i in range (1,11): # el ultimo es para el incremento y los otros dos valores son el rango
    #     page.locator(f"(//td[contains(@class,'  select-checkbox')])[{i}]").click()
        
    #     # limite en el tercer elemento de la pagina
    #     if i==3:
    #         page.locator(f"//a[contains(@data-dt-idx,'1')]").click()
    #     if i==6:
    #         page.locator(f"//a[contains(@data-dt-idx,'2')]").click()
    #     time.sleep(0.7)
    
    for i in range (1,11): # el ultimo es para el incremento y los otros dos valores son el rango
        page.locator(f"(//td[contains(@class,'  select-checkbox')])[{i}]").click()
        
        # limite en el tercer elemento de la pagina
        if i==10:
            page.locator(f"//a[contains(@data-dt-idx,'1')]").click()
            for x in range (1,11):
                page.locator(f"(//td[contains(@class,'  select-checkbox')])[{x}]").click()
                if x==10:
                    page.locator(f"//a[contains(@data-dt-idx,'2')]").click()
                    for y in range (1,11):
                        page.locator(f"(//td[contains(@class,'  select-checkbox')])[{y}]").click()
                    page.locator("//input[contains(@type,'search')]").fill("Je")
                    time.sleep(1)
                    page.locator(f"(//td[contains(@class,'  select-checkbox')])[3]").click()
        
        time.sleep(0.7)











    context.close()
    browser.close()