import asyncio
from logging import handlers
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://demoqa.com/text-box")
        #await page.screenshot(path="screenshot.png")
        print(await page.title)
        await browser.close()

asyncio.run(main())

