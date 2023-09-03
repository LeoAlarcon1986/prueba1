import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright



def test_checkbox(playwright: Playwright, page: Page) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=1000)
    #context=browser.new_context()
    #context=browser.new_context(record_video_dir="video_checkbox/ckeckbox")
    #time.sleep(3)
    context=browser.new_context(
         viewport={"width": 1300, "height":800}
    )
    #context=browser.new_context(record_video_dir="videos/input_1")
    #page.set_viewport_size({"width": 1500, "height":800})
    page=context.new_page()
    page.goto("https://demoqa.com/checkbox")
   
    page.set_default_timeout(2000)
    
#     che1= page.locator("//button[contains(@aria-label,'Toggle')]")
#     expect(che1).to_be_visible()
#     che1.click()

#     page.locator("(//button[contains(@aria-label,'Toggle')])[2]").click()
#     page.locator("text=Commands").click()
           
    context.close()
    browser.close()