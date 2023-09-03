import re
from playwright.sync_api import Page, expect

def test_uno(page: Page):
    page.goto("https://demoqa.com/text-box")
    expect(page).to_have_title(re.compile("DEMOQA"))

    buton_uno=page.locator("text=submit")
    page.screenshot(path="imagen/test_uno.png") #toma foto
    #expect(buton_uno).to_have_attribute("href","/docs/intro")
    buton_uno.click()

    page.screenshot(path="imagen/test_uno.png")