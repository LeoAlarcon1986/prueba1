import re
from playwright.sync_api import Page,expect



def test_dos(page:Page):
    page.goto("https://demoqa.com/")
    expect(page).to_have_title("DEMOQA")


    page.locator("text= Elements").click()
    #page.screenshot(path="imagen/boton_uno.png")
    #btn_uno=page.locator("text= Elements").click()
    # page.screenshot(path="imagen/boton_uno.png")
    # btn_uno.click()
    # page.screenshot(path="imagen/boton_uno_click.png")
            # validador de la pagina a la que avanza 

    expect(page).to_have_url(re.compile(".*elements"))
    page.locator("text= Text Box").click()
    #page.screenshot(path="imagen/boton_dos.png")

            # primer texto campo nombre
    expect(page).to_have_url(re.compile(".*text-box"))
    #page.locator("#userName").fill("leonardo")
    page.locator("//input[@id='userName']").fill("leonardo")
    #page.screenshot(path="imagen/boton_dos.png")
    page.locator("//input[@id='userEmail']").fill("leonardo77710@gmail.com")
    page.locator("#currentAddress").fill("Calle 148#101-10--- Antiguo Refous")
    page.locator("//textarea[@id='permanentAddress']").fill("Torre 6 Apto 204 -- Preguntar por canela")
    page.locator("//button[@id='submit']").click()
    page.screenshot(path="imagen/boton_submit.png")
