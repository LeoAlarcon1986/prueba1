import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright


#def teste_input1(page: Page):
def test_input2(playwright: Playwright, ) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    #context=browser.new_context()
    
    time.sleep(3)
    # context=browser.new_context(
    #     viewport={"width": 1500, "height":800}
    # )
    context=browser.new_context(record_video_dir="videos/input_1")
    #page=context.new_page()



    page.goto("https://testingqarvn.com.es/datos-personales/")
    #expect(page).to_have_title("Datos Personales Básicos")
    # tiempo de espera de salida del ejercicio
    #page.set.default_timeout(5000)
    
    page.locator("#wsf-1-field-21").fill("Leonardo")
    page.screenshot(path="imagen/nombre_1_.png")

    # Aserts o validadores
    apellidos=page.locator("#wsf-1-field-22")
    #visibles
    expect(apellidos).to_be_visible()
    # Enabled
    expect(apellidos).to_be_enabled()
    # empty tiene que estar vacio
    expect(apellidos).to_be_empty()
    #contiene el ID--- sin el #
    expect(apellidos).to_have_id("wsf-1-field-22")

    page.locator("#wsf-1-field-22").fill("Alarcon")


    page.locator("#wsf-1-field-23").fill("leonardo77710@gmail.com")
    # tiempo que fuersa una prueba
    time.sleep(2)
    page.locator("#wsf-1-field-24").fill("3202375722")
    page.locator("#wsf-1-field-28").fill("calle 148 # 101-20")
    page.locator("#wsf-1-field-27").click()
                     #validar si esta visible
    #boton=page.locator("wsf-1-field-27")
    #expect(boton).to_be_visible()

    # if boton:
    #     page.locator("#wsf-1-field-27").click()
    # else:
    #     print("No se encontro boton")

                # cerrar context y navegador
    context.close()
    browser.close()