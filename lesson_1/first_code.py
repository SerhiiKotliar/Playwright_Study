
from playwright.sync_api import sync_playwright, expect
from playwright.async_api import async_playwright, expect
import asyncio

def sync_work():
    # открыть соединение
    with sync_playwright() as p:
        # инициализация браузера (без видимого открытия браузера)
        # browser = p.chromium.launch()

        # инициализация браузера (с явным открытием браузера)
        browser = p.chromium.launch(headless=False)
        # инициализация страницы
        page = browser.new_page()
        # переход по url адресу:
        page.goto('https://whatmyuseragent.com/')
        # сделать скриншот
        page.screenshot(path='demo.png')
        browser.close()


async def async_work():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel='chrome',
            headless=False
        )
        page = await browser.new_page()
        await page.goto('https://whatmyuseragent.com/')
        await page.screenshot(path='demo.png')
        await page.wait_for_timeout(9000)

        await browser.close()


if __name__ == '__main__':
    asyncio.run(async_work())
