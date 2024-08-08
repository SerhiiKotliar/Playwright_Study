import asyncio

from playwright.async_api import async_playwright, expect

args = ['--disable-blink-features=AutomationControlled', "--start-maximized"]


async def async_work():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel='chrome',
            headless=False,
            args=["--start-maximized"]
        )
        context = await browser.new_context(no_viewport=True)
        page = await context.new_page()
        await page.goto('https://whatmyuseragent.com/')

        el = page.locator("#ua")
        await expect(el).to_be_visible()
        ua = await el.inner_text()

        all_links = await page.locator('#navbarNavAltMarkup > div > a').all()

        for link in all_links:
            text = await link.inner_text()
            url = await link.get_attribute('href')
            print(f'{text} -- {url}')

        await page.wait_for_timeout(900000)
        await browser.close()


asyncio.run(async_work())
